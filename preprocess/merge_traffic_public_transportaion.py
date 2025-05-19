import pandas as pd
import os

# 경로 설정
base_dir = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data'
output_file = os.path.join(base_dir, '전체 합산.csv')

# 파일 경로
file_traffic = os.path.join(base_dir, '○교통량 연별 OD 구분_최종.xlsx')
file_public = os.path.join(base_dir, '○동별 수단OD 서울 동합침_최종_본동통합.csv')
file_taxi = os.path.join(base_dir, '택시 OD_동정리_합산.csv')

# 파일 불러오기
df_traffic = pd.read_excel(file_traffic)
df_public = pd.read_csv(file_public, encoding='euc-kr')
df_taxi = pd.read_csv(file_taxi, encoding='euc-kr')

# 필요 열만 추출
df_traffic = df_traffic[['출발_동', '도착_동', '연별 합계']]
df_public = df_public[['출발_동', '도착_동', '지하철_승객수', '버스_승객수']]
df_taxi = df_taxi[['출발_동', '도착_동', '택시_승객수']]

# 출발_동 + 도착_동 기준으로 merge (outer join)
merged = pd.merge(df_public, df_taxi, on=['출발_동', '도착_동'], how='outer')
merged = pd.merge(merged, df_traffic, on=['출발_동', '도착_동'], how='outer')

# 결과 저장
merged.to_csv(output_file, index=False, encoding='euc-kr')
print(f"[✔ 완료] 파일 저장: {output_file}")
