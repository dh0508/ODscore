import pandas as pd

# 모든 행 출력 허용
pd.set_option('display.max_rows', None)

# 파일 경로
input_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●스코어.csv"

# CSV 불러오기
df = pd.read_csv(input_path, encoding='cp949')

# 라벨 없는 데이터 필터링
unlabeled_df = df[df['label'].isna()].copy()

# 동점 허용 순위 부여
unlabeled_df['순위'] = unlabeled_df['score'].rank(method='min', ascending=False).astype(int)

# 정렬
sorted_df = unlabeled_df.sort_values(by=['순위', '출발_동', '도착_동'])

# 출력 헤더 (모든 열 오른쪽 정렬)
print(f"{'순위':>7} {'출발_동':>8} {'도착_동':>8} {'score':>10}")

# 출력 본문
for _, row in sorted_df.iterrows():
    print(f"{row['순위']:>7} {row['출발_동']:>8} {row['도착_동']:>8} {row['score']:>10.6f}")
