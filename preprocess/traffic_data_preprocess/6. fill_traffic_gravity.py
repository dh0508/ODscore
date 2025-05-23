import pandas as pd
import numpy as np
import os

# 1. 파일 경로 설정
base_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data"
od_template_path = os.path.join(base_path, "●전체 합산 택시채움.csv")
traffic_path = os.path.join(base_path, "교통량 연별 OD 구분.xlsx")
pop_area_path = os.path.join(base_path, "동별 인원수, 면적 동합침.xlsx")
output_path = os.path.join(base_path, "○교통량 연별 OD 구분_최종.csv")

# 2. 데이터 불러오기
od_df = pd.read_csv(od_template_path, encoding='cp949')
traffic_df = pd.read_excel(traffic_path)
pop_area_df = pd.read_excel(pop_area_path)

# 3. 인구/면적 컬럼 정리
pop_area_df.columns = ['동', '인구', '면적']
pop_area_df['동'] = pop_area_df['동'].str.strip()

# 4. 중력모델 정의
def gravity_model(o_pop, d_pop):
    return o_pop * d_pop

# 5. 교통량 컬럼명 정리
traffic_df.columns = traffic_df.columns.str.strip()
if '연별 합계' in traffic_df.columns:
    traffic_df = traffic_df.rename(columns={'연별 합계': '교통량'})
elif '전체합계' in traffic_df.columns:
    traffic_df = traffic_df.rename(columns={'전체합계': '교통량'})
elif '교통량' not in traffic_df.columns:
    raise KeyError("교통량 컬럼이 존재하지 않습니다. 실제 컬럼명을 확인하세요.")

# 6. 병합
merged_df = od_df.merge(traffic_df, on=['출발_동', '도착_동'], how='left')

# 7. 인구 딕셔너리 생성
pop_dict = pop_area_df.set_index('동')['인구'].to_dict()

# 8. 결측 교통량 채우기
def estimate_traffic(row):
    if pd.notna(row['교통량']):
        return row['교통량']
    o_pop = pop_dict.get(row['출발_동'], np.nan)
    d_pop = pop_dict.get(row['도착_동'], np.nan)
    if pd.isna(o_pop) or pd.isna(d_pop):
        return np.nan
    return gravity_model(o_pop, d_pop)

merged_df['교통량'] = merged_df.apply(estimate_traffic, axis=1)

# 9. 최종 저장
final_df = merged_df[['출발_동', '도착_동', '교통량']]
final_df.to_csv(output_path, index=False, encoding='cp949')
