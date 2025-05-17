import pandas as pd
import os

# 경로 설정
input_file = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 수단OD 서울 동합침_최종.csv'
output_file = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 수단OD 서울 동합침_최종_본동통합.csv'

# CSV 불러오기
df = pd.read_csv(input_file, encoding='euc-kr')

# ✅ 본동 → 동으로 변경 (출발_동, 도착_동)
df['출발_동'] = df['출발_동'].str.replace(r'본동$', '동', regex=True)
df['도착_동'] = df['도착_동'].str.replace(r'본동$', '동', regex=True)

# ✅ 같은 출발_동 + 도착_동 기준으로 다시 합산
df_grouped = df.groupby(['출발_동', '도착_동'], as_index=False).sum(numeric_only=True)

# 저장
df_grouped.to_csv(output_file, index=False, encoding='euc-kr')
print(f"[✔ 완료] 본동 통합 후 저장: {output_file}")
