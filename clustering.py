import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import pairwise_distances

# 1. 데이터 불러오기
file_path = "D:/SITE/●국민대/대외활동/●국토 • 교통 데이터활용 경진대회/data/●전체 합산 택시채움.csv"
df = pd.read_csv(file_path, encoding='cp949')
features = ['지하철_승객수', '버스_승객수', '택시_승객수']

# 2. 전처리
X = df[features].fillna(0)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. 거리 기준으로 정렬 (전체 데이터에서 중심과 거리 계산)
center = X_scaled.mean(axis=0).reshape(1, -1)
dists = pairwise_distances(X_scaled, center).reshape(-1)
df['거리'] = dists

# 4. 거리순 정렬 후 균등 분할
df_sorted = df.sort_values(by='거리').reset_index(drop=True)
n_clusters = 80
samples_per_cluster = len(df) // n_clusters
labels = np.repeat(range(n_clusters), samples_per_cluster)
# 나머지는 마지막 클러스터에 추가
labels = np.pad(labels, (0, len(df_sorted) - len(labels)), constant_values=n_clusters - 1)
df_sorted['클러스터'] = labels

# 5. 저장
output_path = "D:/SITE/●국민대/대외활동/●국토 • 교통 데이터활용 경진대회/data/●거리기반_균등클러스터링.csv"
df_sorted.drop(columns='거리').to_csv(output_path, encoding='cp949', index=False)
print("✅ 거리 기반 균등 클러스터링 완료. 결과 저장됨.")
