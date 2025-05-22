import pandas as pd
import re
import os

# 입력 파일 경로
input_path = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 인원수, 면적.xlsx'

# 출력 파일 경로
output_path = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 인원수, 면적 동합침.xlsx'

# 동 이름 정규화 함수 (기존 코드와 동일)
def merge_dongs(name):
    if pd.isna(name):
        return name
    name = name.strip()
    name = re.sub(r'(\D+)\d+동$', r'\1동', name)
    name = re.sub(r'종로\d+.*가동', '종로동', name)
    name = re.sub(r'면목\d+.*동', '면목동', name)
    name = re.sub(r'금호\d+.*가동', '금호동', name)
    name = re.sub(r'성수\d가동', '성수동', name)
    name = re.sub(r'용산\d가동', '용산동', name)
    name = re.sub(r'상계\d+.*동', '상계동', name)
    name = re.sub(r'중계\d+.*동', '중계동', name)
    return name

# 엑셀 파일 읽기
df = pd.read_excel(input_path)

# 동 이름 컬럼명이 정확히 무엇인지 확인 필요 (예: '동' 혹은 '행정동' 등)
# 예시는 '동' 컬럼으로 가정
dong_col = '동'  # 컬럼명에 맞게 수정 필요

# 동 이름 정규화 적용
df[dong_col] = df[dong_col].apply(merge_dongs).str.strip()

# 동별 합산 (인원수, 면적 등 숫자 컬럼들만 합산)
# 숫자형 컬럼만 추출
num_cols = df.select_dtypes(include='number').columns.tolist()

# 동별 합산
df_grouped = df.groupby(dong_col, as_index=False)[num_cols].sum()

# 엑셀 저장
df_grouped.to_excel(output_path, index=False)

print(f"[✔ 완료] '{input_path}' 동합침 후 '{output_path}' 저장됨")
