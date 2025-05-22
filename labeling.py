import pandas as pd

# 파일 경로 설정
input_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●거리기반_균등클러스터링.csv"
output_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●학습용.csv"

# CSV 불러오기
df = pd.read_csv(input_path, encoding='cp949')

# 정답 클러스터
answer_clusters = [22, 48, 70, 72, 73, 75, 76, 77, 78, 79]

# 오답 클러스터
pseudo_negative_clusters = [66, 65, 64, 63, 62, 61, 60, 58, 57, 56]

# 초기화: label 없음
df['label'] = pd.NA

# 정답 클러스터 → label = 1
df.loc[df['클러스터'].isin(answer_clusters), 'label'] = 1

# 오답 클러스터 → label = 0
df.loc[df['클러스터'].isin(pseudo_negative_clusters), 'label'] = 0

# 저장
df.to_csv(output_path, index=False, encoding='cp949')
