import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. 파일 불러오기
file_path = "D:/SITE/●국민대/대외활동/●국토 • 교통 데이터활용 경진대회/data/●전체 합산 택시채움.csv"
df = pd.read_csv(file_path, encoding='cp949')

# 2. 클러스터링에 사용할 열 선택 및 결측치 처리
features = ['지하철_승객수', '버스_승객수', '택시_승객수']
df_cluster = df[features].fillna(0)  # 결측값은 0으로 대체

# 3. 표준화 (StandardScaler 사용)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_cluster)

# 4. KMeans 클러스터링 실행 (클러스터 수: 80개)
kmeans = KMeans(n_clusters=80, n_init=10, max_iter=300, random_state=42)
labels = kmeans.fit_predict(X_scaled)

# 5. 클러스터 결과 원본 데이터프레임에 추가
df['클러스터'] = labels

# 6. 결과 저장
output_path = "D:/SITE/●국민대/대외활동/●국토 • 교통 데이터활용 경진대회/data/●클러스터링_결과_k80.csv"
df.to_csv(output_path, encoding='cp949', index=False)

print(f"KMeans 클러스터링 완료! 결과 파일: {output_path}")