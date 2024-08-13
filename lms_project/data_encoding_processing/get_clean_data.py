import io
import os
import re
import pandas as pd
import numpy as np
from tqdm import tqdm
import requests
import json
import numpy as np
from bs4 import BeautifulSoup

def encoding_data(file_path):
    # 파일을 바이너리 모드로 읽기
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    # 바이너리 데이터를 'EUC-KR'로 디코딩 (에러는 무시)
    decoded_data = raw_data.decode('euc-kr', errors='ignore')

    # 디코딩된 데이터를 StringIO 객체로 감싸서 Pandas로 읽기
    df = pd.read_csv(io.StringIO(decoded_data), encoding='utf-8-sig')

    print(f"Data from {file_path}")
    return df

def food_info(name):
    url = f"https://www.10000recipe.com/recipe/list.html?q={name}"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else: 
        # print("HTTP response error:", response.status_code)
        return None
    
    food_list = soup.find_all(attrs={'class': 'common_sp_link'})
    if not food_list:
        # print(f"No recipes found for {name}")
        return None
    
    food_id = food_list[0]['href'].split('/')[-1]
    new_url = f'https://www.10000recipe.com/recipe/{food_id}'
    new_response = requests.get(new_url)
    if new_response.status_code == 200:
        html = new_response.text
        soup = BeautifulSoup(html, 'html.parser')
    else: 
        # print("HTTP response error:", response.status_code)
        return None
    
    food_info = soup.find(attrs={'type': 'application/ld+json'})
    if not food_info:
        # print(f"No JSON-LD data found for recipe {food_id}")
        return None
    
    try:
        result = json.loads(food_info.text)
    except json.JSONDecodeError as e:
        # print(f"JSON decode error: {e}")
        return None


    # Check if 'recipeInstructions' key exists and handle it appropriately
    recipe_instructions = result.get('recipeInstructions', [])
    recipe = [instruction['text'] for instruction in recipe_instructions]
    
    for i in range(len(recipe)):
        recipe[i] = f'{i + 1}. ' + recipe[i]

    return recipe


def crawl_data(df):
    col = [] 
    for res_title in tqdm(df['RCP_TTL'], total=df.shape[0],  desc='crawling...'):
        try:
            recipe = food_info(res_title)
            if recipe != None:  # res가 None이 아닌 경우에만 처리
                data = ' '.join([x[3:] for x in recipe])
                # print(data)
                col.append(data)
            else:
                col.append(np.nan)

        except Exception as e:
            # print(f"Error processing {res_title}")
            col.append(np.nan)

    return col

def get_pickle_data(file_path, n):
    df = encoding_data(file_path)

    # 레시피 명이 결측값인 건 사용할 수 없으므로 삭제
    df = df.dropna(subset='CKG_NM')
    # 필요한 컬럼 : [레시피제목(RCP_TTL), 레시피명(CKG_NM), 요리 난이도(CKG_DODF_NM), 요리인분(CKG_INBUN_NM), 주재료(CKG_MTRL_CN), 레시피 상세 내용(), 레시피 카테고리(CKG_KND_ACTO_NM, CKG_MTH_ACTO_NM,CKG_STA_ACTO_NM) ]
    clean_df = df[['RCP_TTL', 'CKG_NM', 'CKG_INBUN_NM', 'CKG_MTRL_CN', 'CKG_DODF_NM','CKG_KND_ACTO_NM', 'CKG_MTH_ACTO_NM', 'CKG_STA_ACTO_NM']].dropna()

    final_df = clean_df.sample(n=n)
    final_df['RCP_CONTENT'] = crawl_data(final_df)
    final_df = final_df.drop('RCP_TTL', axis=1)
    
    os.makedirs('result', exist_ok=True)

    final_df.to_pickle(f'result/clean_df_{n}.pkl')
    print(f"\n*** '{file_path} + crawling data process' is finished. Saved at 'result/clean_df_{n}.pkl'.")
    return f'result/clean_df_{n}.pkl'


def load_data(path):
    df = pd.read_pickle(path)
    df['RCP_CONTENT'] = df['RCP_CONTENT'].replace('', np.nan).replace('nan', np.nan)
    df = df.dropna().reset_index(drop=True)
    return df

def clean_servings(df):
    df['CKG_INBUN_NM'] = df['CKG_INBUN_NM'].str.replace('인분', '')
    df['CKG_INBUN_NM'] = df['CKG_INBUN_NM'].str.replace('이상', '')
    df['CKG_INBUN_NM'] = df['CKG_INBUN_NM'].astype('int')
    return df

def clean_ingredients(df):
    """ 재료 컬럼을 정리합니다. """
    df['CKG_MTRL_CN'] = df['CKG_MTRL_CN'].str.replace('|', ',')
    df['CKG_MTRL_CN'] = df['CKG_MTRL_CN'].str.replace('그램', 'g')
    df['CKG_MTRL_CN'] = df['CKG_MTRL_CN'].str.replace(r'\[.*?\]', '', regex=True)
    df['CKG_MTRL_CN'] = df['CKG_MTRL_CN'].str.replace(r'\(.*?\)', '', regex=True)
    df['CKG_MTRL_CN'] = df['CKG_MTRL_CN'].str.replace('?', '')
    return df

def remove_stopwords(df):
    stopwords = ['-', '_', '꾹꾹', '@6845925', '/'
                '^', '~', '!', 'ㅎ', 'ㅋ', 'ㅌ', '【', ':)',
                    '...', '..', '*', '♡', '♥', '☆','★', '♬', '♪', 'ㅠ', 'ㅜ', 'ㅡ', '[', ']']

    stopwords_pattern = '|'.join(re.escape(word) for word in stopwords)
    zero_width_space_pattern_1 = r'\u200b'
    zero_width_space_pattern_2 = r'\xa0'

    df['RCP_CONTENT'] = df['RCP_CONTENT'].str.replace(zero_width_space_pattern_1, '', regex=True) \
                                            .str.replace(zero_width_space_pattern_2, '', regex=True) \
                                            .str.replace(stopwords_pattern, '', regex=True) \
                                            .str.strip()

    df['CKG_MTRL_CN'] = df['CKG_MTRL_CN'].str.replace(stopwords_pattern, '', regex=True) \
                                            .str.strip()
    print(df.head())
    print(df.info())
    return df

def preprocess_data(path):
    df = load_data(path)
    df = clean_servings(df)
    df = clean_ingredients(df)
    df = remove_stopwords(df)
    # df = adjust_servings_in_dataframe(df)

    os.makedirs('result', exist_ok=True)

    df.to_pickle(f'result/preprocessed_df_{df.shape[0]}.pkl')
    # print(f"\n*** All processing is finished. Saved at 'result/preprocessed_df_{df.shape[0]}.pkl'.")

    return f"\n*** All processing is finished. Saved at 'result/preprocessed_df_{df.shape[0]}.pkl'."


if __name__ =='__main__':
    file_paths = ['TB_RECIPE_SEARCH-220701.csv', 'TB_RECIPE_SEARCH-20231130.csv']
    file_path = os.path.join('data', file_paths[0])
    result = get_pickle_data(file_path, 30000) # 크롤링 데이터 개수

    # preprocess
    preprocess_data(result)