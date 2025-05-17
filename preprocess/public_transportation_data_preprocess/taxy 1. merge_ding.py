import pandas as pd
import os
import re

# 파일 경로
input_file = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\택시 OD.csv'
output_file = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\택시 OD_동정리_합산.csv'

# 🔧 동 이름 정리 함수
def clean_dong(name):
    if pd.isna(name):
        return name
    name = name.strip()
    name = re.sub(r'(\D+)\d+동$', r'\1동', name)  # OO1동 → OO동
    name = re.sub(r'본동$', '동', name)           # ~본동 → ~동
    return name

# CSV 불러오기
df = pd.read_csv(input_file, encoding='euc-kr')

# 동 이름 정리
df['출발_동'] = df['출발_동'].apply(clean_dong)
df['도착_동'] = df['도착_동'].apply(clean_dong)

# 🔢 '택시_승객수'만 합산, 출발동-도착동 기준으로
df_grouped = df.groupby(['출발_동', '도착_동'], as_index=False)['택시_승객수'].sum()

# 저장
df_grouped.to_csv(output_file, index=False, encoding='euc-kr')
print(f"[✔ 완료] 저장 경로: {output_file}")
