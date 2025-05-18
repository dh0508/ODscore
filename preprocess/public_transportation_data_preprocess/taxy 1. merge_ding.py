import pandas as pd
import os
import re

# 파일 경로
input_file = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\택시 OD.csv'
output_file = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\택시 OD_동정리.csv'

# 파일 불러오기
df = pd.read_csv(input_file, encoding='euc-kr')

# 🔧 동 이름 정리 함수 정의
def clean_dong(name):
    if pd.isna(name):
        return name
    name = name.strip()
    # OO1동, OO2동 등 → OO동
    name = re.sub(r'(\D+)\d+동$', r'\1동', name)
    # 본동 → 동
    name = re.sub(r'본동$', '동', name)
    return name

# 🧹 출발/도착 동 이름 정제
df['출발_동'] = df['출발_동'].apply(clean_dong)
df['도착_동'] = df['도착_동'].apply(clean_dong)

# 🎯 출발동 = 도착동만 필터링
df_same = df[df['출발_동'] == df['도착_동']].copy()

# 🔢 승객수 관련 열만 그룹합산 (자동 추출)
group_cols = ['출발_동', '도착_동']
value_cols = df_same.select_dtypes(include='number').columns.tolist()
value_cols = [col for col in value_cols if col not in group_cols]

# 📊 그룹화 및 합산
df_grouped = df_same.groupby(group_cols, as_index=False)[value_cols].sum()

# 저장
df_grouped.to_csv(output_file, index=False, encoding='euc-kr')
print(f"[✔ 완료] 저장 경로: {output_file}")
