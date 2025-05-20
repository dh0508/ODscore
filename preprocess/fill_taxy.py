import pandas as pd
from sklearn.linear_model import LinearRegression

# 파일 경로
input_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●전체 합산.csv"
output_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●전체 합산 택시채움.csv"

# CSV 파일 불러오기 (인코딩 cp949)
df = pd.read_csv(input_path, encoding='cp949')

# 택시_승객수가 결측치인 행과 아닌 행 분리
df_train = df[df['택시_승객수'].notna()]
df_pred = df[df['택시_승객수'].isna()]

# 학습 데이터 (독립변수: 지하철_승객수, 버스_승객수, 종속변수: 택시_승객수)
X_train = df_train[['지하철_승객수', '버스_승객수']]
y_train = df_train['택시_승객수']

# 예측할 데이터
X_pred = df_pred[['지하철_승객수', '버스_승객수']]

# 선형회귀 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 결측치 예측
predicted_taxi = model.predict(X_pred)

# 예측값으로 결측치 채우기
df.loc[df['택시_승객수'].isna(), '택시_승객수'] = predicted_taxi

# 결과 저장 (인코딩 cp949)
df.to_csv(output_path, index=False, encoding='cp949')

print("택시_승객수 결측치 보완 완료, 파일 저장 완료.")
