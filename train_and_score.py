import pandas as pd
from sklearn.linear_model import LogisticRegression

# 파일 경로 설정
input_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●학습용.csv"
output_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●스코어.csv"

# CSV 불러오기
df = pd.read_csv(input_path, encoding='cp949')

# 학습용 데이터: label이 0 또는 1인 행만 사용
train_df = df[df['label'].isin([0, 1])]

# 학습 feature와 target
X_train = train_df[['지하철_승객수', '버스_승객수', '택시_승객수']]
y_train = train_df['label']

# 전체 feature 추출
X_all = df[['지하철_승객수', '버스_승객수', '택시_승객수']]

# 로지스틱 회귀 모델 학습
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 정답일 확률 예측 (label=1일 확률)
df['score'] = model.predict_proba(X_all)[:, 1]

# 결과 저장
df.to_csv(output_path, index=False, encoding='cp949')
