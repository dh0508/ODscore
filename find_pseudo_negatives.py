import pandas as pd
from sklearn.metrics.pairwise import cosine_distances

# CSV 파일 경로
file_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●학습용.csv"

# CSV 로드
df = pd.read_csv(file_path, encoding='cp949')

# 사용할 특성과 클러스터 컬럼
features = ['지하철_승객수', '버스_승객수', '택시_승객수', '교통량']
cluster_col = '클러스터'

# 정답 클러스터 목록
positive_clusters = [22, 48, 70, 73, 75, 76, 78, 79]

# 클러스터별 평균 특성 계산
cluster_features = df.groupby(cluster_col)[features].mean()

# 정답 클러스터들의 평균 특성 벡터
positive_mean_vector = cluster_features.loc[positive_clusters].mean().values.reshape(1, -1)

# 모든 클러스터와 정답 평균 벡터 간 코사인 거리 계산
distances = cosine_distances(cluster_features.values, positive_mean_vector).flatten()

# 거리 추가
cluster_features['거리'] = distances

# 거리 큰 순서로 상위 10개 클러스터 추출
top_distant_clusters = cluster_features.sort_values(by='거리', ascending=False).head(10)

# 결과 출력
print(top_distant_clusters.reset_index()[[cluster_col, '거리']])
