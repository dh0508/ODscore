import pandas as pd

input_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●전체 합산.csv"
df = pd.read_csv(input_path, encoding='cp949')

# 지하철_승객수 또는 버스_승객수에 결측치가 있는 행 필터링
condition = df['지하철_승객수'].isna() | df['버스_승객수'].isna()
missing_subway_bus = df[condition]

print(f"지하철_승객수 또는 버스_승객수 결측치가 있는 행 개수: {missing_subway_bus.shape[0]}")
print("결측치 있는 행 인덱스 리스트:")
print(missing_subway_bus.index.tolist())
