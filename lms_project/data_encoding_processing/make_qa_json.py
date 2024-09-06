import re
import pandas as pd
import json
def remove_units_for_ingredient(text):
    text_without_units = re.sub(r'\d+', '', text)
    text_with_or_replaced = re.sub(r'(or|ｏｒ)', '또는', text_without_units, flags=re.IGNORECASE)
    text_cleaned = re.sub(r'[a-zA-Z0-9]+', '', text_with_or_replaced)
    text_cleaned = text_cleaned.replace('  ', ', ').strip(', ')
    stop_words = ['작은것반개', '좋아하시는분만', '원하는분만', '원하시는만큼', '원하는만큼', '원하는',
                  '살짝 짠 것 적당량', '작은거', '큰거', '약간', '살짝', '조금', '많이', '넉넉히,', '조금씩',
                  '공기', '숟가락', '아빠', '숟갈', '수저', '주먹', '센티', '센치', '미터', '방울', '개', '컵', '큰술', '꼬집', '작은술', '스푼', '스픈', '종이 호일',
                  '뚜껑있는 후라이팬', '비정제', '꽁듀', '취향껏', '적당량', '적당히', '다양한 ', '정도', '없으면생략', '팔팔', '전자렌지', '랩'
                  '솔솔', '톡톡톡', '번톡톡', '낸것', '시원한', '동그란 포장', '남은', '작은', '줌', '牡', '+', '.', ',,']

    for word in stop_words:
        text_cleaned = re.sub(re.escape(word), '', text_cleaned)
    text_cleaned = re.sub(r'\s+', ' ', text_cleaned).strip()
    return text_cleaned

def make_qa_json(df):
    cleaned_ingredients = [remove_units_for_ingredient(item) for item in df['CKG_MTRL_CN']]
    df['clean_ingredient'] = cleaned_ingredients

    rag_data = []
    for i in range(len(df)):
        question = f"{df['clean_ingredient'][i]}로 할 수 있는 요리 레시피 알려줘."
        answer = (f"말씀하신 재료로 할 수 있는 요리 레시피를 알려드리겠습니다."
                  f"[레시피 명] {df['CKG_NM'][i]}"
                  f"[재료] {df['CKG_MTRL_CN'][i]}"
                  f"[요리 인분 수] {df['CKG_INBUN_NM'][i]}인분"
                  f"[요리 분류] {df['CKG_MTH_ACTO_NM'][i]}"
                  f"[요리 과정] {df['RCP_CONTENT'][i]}"
                  f"맛있는 식사 되세요!")
        rag_data.append({'question': question, 'answer': answer})

    with open(f'result/rag_data_{len(rag_data)}.json', 'w') as f:
        json.dump(rag_data, f)

if __name__ == '__main__':
    df = pd.read_pickle('result/preprocessed_df_963.pkl')
    make_qa_json(df)
