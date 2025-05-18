import pandas as pd

# 엑셀 파일 경로
file_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●교통량 연별 OD 구분.xlsx"

# 엑셀 파일 불러오기
df = pd.read_excel(file_path)

# 동일 출발_동 + 도착_동 쌍 기준으로 그룹화하고 수치 데이터 합산
grouped_df = df.groupby(['출발_동', '도착_동'], as_index=False).sum()

# 결과 저장
output_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\●교통량 연별 OD 구분_합쳐짐.xlsx"
grouped_df.to_excel(output_path, index=False)

print("작업 완료. 합쳐진 파일 저장됨.")
