import pandas as pd

# 모든 행 출력 허용
pd.set_option('display.max_rows', None)

# 파일 경로 설정
input_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●스코어.csv"
output_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●스코어_결과.xlsx"

# CSV 파일 불러오기
df = pd.read_csv(input_path, encoding='cp949')

# label이 NaN인 데이터만 필터링 (label 없는 데이터)
unlabeled_df = df[df['label'].isna()].copy()

# score 기준 내림차순, 동점은 동일 순위 부여
unlabeled_df['순위'] = unlabeled_df['score'].rank(method='min', ascending=False).astype(int)

# 순위, 출발_동, 도착_동 기준 정렬
sorted_df = unlabeled_df.sort_values(by=['순위', '출발_동', '도착_동'])

# 정해진 열만 추출하여 엑셀로 저장
sorted_df[['순위', '출발_동', '도착_동', 'score']].to_excel(output_path, index=False)
