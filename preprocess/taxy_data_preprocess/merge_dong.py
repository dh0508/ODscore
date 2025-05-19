import os
import pandas as pd
import re

# 입력/출력 경로 설정
input_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\택시 OD.xlsx"
output_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\택시 OD_동정리_합산.csv"

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

try:
    # 데이터 불러오기
    df = pd.read_excel(input_path)

    # 동 이름 정리
    df['시작_명칭'] = df['시작_명칭'].apply(merge_dongs).str.strip()
    df['종료_명칭'] = df['종료_명칭'].apply(merge_dongs).str.strip()

    # 출발_동, 도착_동 기준으로 이용수 합산
    grouped = df.groupby(['시작_명칭', '종료_명칭'], as_index=False)['이용수'].sum()

    # 컬럼 이름 변경
    grouped.columns = ['출발_동', '도착_동', '택시_승객수']

    # 저장
    grouped.to_csv(output_path, index=False, encoding='euc-kr')
    print(f"✅ 저장 완료: {output_path}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")
