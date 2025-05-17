import os
import pandas as pd

# 폴더 경로 설정
input_folder = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\교통량 일별 OD'
output_folder = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\교통량 월별 OD'

for month in range(1, 13):
    month_str = f'{month:02d}'
    input_file = f'{month_str}월 서울시 교통량 조사자료(2024).xlsx'
    output_file = f'{month_str}월별 서울시 교통량 조사자료(2024).xlsx'
    input_path = os.path.join(input_folder, input_file)
    output_path = os.path.join(output_folder, output_file)

    if not os.path.isfile(input_path):
        print(f'[X] 파일 없음: {input_file}')
        continue

    try:
        # 엑셀 파일 로딩
        df = pd.read_excel(input_path, sheet_name=f'2024년 {month_str}월', engine='openpyxl')

        # 열 이름 공백 제거 (예: '월별 합계 ')
        df.columns = df.columns.str.strip()

        # "월별 합계" 열 존재 및 유효성 체크
        if '월별 합계' not in df.columns:
            print(f'[!] "월별 합계" 열 없음: {input_file}')
            continue
        if df['월별 합계'].dropna().eq(0).all():
            print(f'[!] "월별 합계"가 모두 0 또는 NaN: {input_file}')
            continue

        # 유효한 "월별 합계" 값만 남기기
        df = df[df['월별 합계'].notna() & (df['월별 합계'] != 0)]

        # 제거할 열 목록 (일자, 지점명, 방향, 일별 통행량 합계)
        drop_cols = ['일자', '지점명', '방향', '일별 통행량 합계']
        df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)

        # 결과 저장
        df.to_excel(output_path, index=False, engine='openpyxl')
        print(f'[✔] 저장 완료: {output_file}')

    except Exception as e:
        print(f'[!] 오류 발생 - {input_file}: {e}')
