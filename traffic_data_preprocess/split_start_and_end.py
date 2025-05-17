import os
import pandas as pd

# 입력 및 출력 경로 설정
input_folder = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\교통량 월별 OD'
output_folder = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\교통량 월별 OD 구분'
os.makedirs(output_folder, exist_ok=True)

# 1월부터 12월까지 반복 처리
for month in range(1, 13):
    month_str = f'{month:02d}'
    input_filename = f'{month_str}월별 서울시 교통량 조사자료(2024).xlsx'
    output_filename = f'{month_str}월별 서울시 교통량 조사자료(2024) 구분.xlsx'
    input_path = os.path.join(input_folder, input_filename)
    output_path = os.path.join(output_folder, output_filename)

    if not os.path.isfile(input_path):
        print(f'[X] 파일 없음: {input_filename}')
        continue

    try:
        # 엑셀 파일 로딩
        df = pd.read_excel(input_path, engine='openpyxl')
        df.columns = df.columns.str.strip()  # 공백 제거

        # 구분 열에서 출발지/도착지 분리하고 구분 열 삭제
        if '구분' in df.columns:
            df[['출발지', '도착지']] = df['구분'].str.split('->', expand=True)
            df.drop(columns=['구분'], inplace=True)

        # 결과 저장
        df.to_excel(output_path, index=False, engine='openpyxl')
        print(f'[✔] 저장 완료: {output_filename}')

    except Exception as e:
        print(f'[!] 오류 발생 - {input_filename}: {e}')
