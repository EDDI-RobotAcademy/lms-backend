import pandas as pd

# 파일 목록
file_paths = ['TB_RECIPE_SEARCH-220701.csv', 'TB_RECIPE_SEARCH-20231130.csv']

for file_path in file_paths:
    output_file_path = file_path.replace('.csv', '_cleaned.csv')
    
    # 파일을 바이너리 모드로 읽기
    with open(file_path, 'rb') as file:
        raw_data = file.read()

    # 바이너리 데이터를 'EUC-KR'로 디코딩 (에러는 무시)
    decoded_data = raw_data.decode('euc-kr', errors='ignore')

    # 디코딩된 데이터를 임시 CSV 파일로 저장
    with open(output_file_path, 'w', encoding='utf-8-sig') as temp_file:
        temp_file.write(decoded_data)

    # 임시 파일을 다시 읽어서 DataFrame으로 변환
    data = pd.read_csv(output_file_path)

    # 데이터를 다시 CSV로 저장
    data.to_csv(output_file_path, index=False, encoding='utf-8-sig')

    print("파일이 성공적으로 저장되었습니다:", output_file_path)
