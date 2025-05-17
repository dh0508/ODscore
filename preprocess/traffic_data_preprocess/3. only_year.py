import os
import pandas as pd

# 입력 폴더
input_folder = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\교통량 월별 OD 구분'
# 출력 파일 경로
output_file = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●교통량 연별 OD 구분.xlsx'

# 빈 DataFrame 생성 (출발지, 도착지, 연별 합계)
summary_df = pd.DataFrame(columns=['출발지', '도착지', '연별 합계'])

# 1월부터 12월까지 반복
for month in range(1, 13):
    month_str = f'{month:02d}'
    file_name = f'{month_str}월별 서울시 교통량 조사자료(2024) 구분.xlsx'
    file_path = os.path.join(input_folder, file_name)

    if not os.path.isfile(file_path):
        print(f'[X] 파일 없음: {file_name}')
        continue

    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        df.columns = df.columns.str.strip()

        # 필요한 열만 사용
        if not {'출발지', '도착지', '월별 합계'}.issubset(df.columns):
            print(f'[!] 열 누락: {file_name}')
            continue

        # 같은 출발지+도착지 기준으로 groupby 합산
        grouped = df.groupby(['출발지', '도착지'], as_index=False)['월별 합계'].sum()
        grouped.rename(columns={'월별 합계': '연별 합계'}, inplace=True)

        # summary_df에 누적
        summary_df = pd.concat([summary_df, grouped], ignore_index=True)

    except Exception as e:
        print(f'[!] 오류 발생 - {file_name}: {e}')

# 최종적으로 출발지+도착지 기준으로 또 한 번 groupby해서 연별 합계 합산
final_df = summary_df.groupby(['출발지', '도착지'], as_index=False)['연별 합계'].sum()

# 저장
final_df.to_excel(output_file, index=False, engine='openpyxl')
print(f'[✔] 최종 파일 저장 완료: {output_file}')