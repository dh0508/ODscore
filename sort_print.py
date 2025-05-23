import pandas as pd

# 모든 행 출력 허용
pd.set_option('display.max_rows', None)

# 파일 경로
input_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●스코어.csv"
output_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●스코어_결과.txt"

# CSV 불러오기
df = pd.read_csv(input_path, encoding='cp949')

# label이 있는 데이터 제거 (즉, label 없는 데이터만 사용)
unlabeled_df = df[df['label'].isna()].copy()

# 동점 허용 순위 부여
unlabeled_df['순위'] = unlabeled_df['score'].rank(method='min', ascending=False).astype(int)

# 정렬
sorted_df = unlabeled_df.sort_values(by=['순위', '출발_동', '도착_동'])

# TXT 파일로 저장
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(f"{'순위':>7} {'출발_동':>8} {'도착_동':>8} {'score':>10}\n")
    for _, row in sorted_df.iterrows():
        f.write(f"{row['순위']:>7} {row['출발_동']:>8} {row['도착_동']:>8} {row['score']:>10.6f}\n")
