import os
import pandas as pd
import re

# 입력/출력 경로 설정
input_dir = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 수단OD 서울'
output_dir = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 수단OD 서울 동합침'
os.makedirs(output_dir, exist_ok=True)

# 동 이름 정규화 함수
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

# 날짜별 반복 처리
for month in range(1, 13):
    for day in range(1, 32):
        date_str = f'2024{month:02d}{day:02d}'
        file_name = f'동별_수단OD 서울_{date_str}.csv'
        input_path = os.path.join(input_dir, file_name)

        if not os.path.exists(input_path):
            continue

        try:
            df = pd.read_csv(input_path, encoding='euc-kr')

            # 동 이름 정리
            df['출발_동'] = df['출발_동'].apply(merge_dongs).str.strip()
            df['도착_동'] = df['도착_동'].apply(merge_dongs).str.strip()

            # ✅ 출발_동, 도착_동 기준으로만 합산
            df_grouped = df.groupby(
                ['출발_동', '도착_동'],
                as_index=False
            )[["총_승객수", "지하철_승객수", "버스_승객수"]].sum()

            # 저장
            output_file = f'동별_수단OD 서울 동합침_{date_str}.csv'
            output_path = os.path.join(output_dir, output_file)
            df_grouped.to_csv(output_path, index=False, encoding='euc-kr')

            print(f"[✔ 합쳐짐] {file_name} → {output_file}")

        except Exception as e:
            print(f"[❌ 오류] {file_name}: {e}")
