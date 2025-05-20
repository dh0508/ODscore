import pandas as pd
from itertools import product

# 1. 원본 데이터 로드
file_path = "D:/SITE/●국민대/대외활동/●국토 • 교통 데이터활용 경진대회/data/●전체 합산.csv"
df = pd.read_csv(file_path, encoding="cp949")

# 2. 기존 OD 딕셔너리
od_dict = {(row['출발_동'], row['도착_동']): row['연별 합계'] for _, row in df.iterrows()}
dong_list = sorted(set(df['출발_동']) | set(df['도착_동']))

# 3. 각 동의 유입/유출량 계산
inflow = df.groupby('도착_동')['연별 합계'].sum()
outflow = df.groupby('출발_동')['연별 합계'].sum()
total_flow = inflow.add(outflow, fill_value=0)

# 4. hop=2인 보간 계산 (A → B → C)
new_links = dict(od_dict)
new_rows = []

for a in dong_list:
    for c in dong_list:
        if a == c or (a, c) in new_links:
            continue
        est_sum = 0
        for b in dong_list:
            if b in (a, c):
                continue
            if (a, b) in new_links and (b, c) in new_links and total_flow.get(b, 0) > 0:
                est = (new_links[(a, b)] * new_links[(b, c)]) / total_flow[b]
                if pd.notna(est):
                    est_sum += est
        if est_sum > 0:
            new_links[(a, c)] = est_sum
            new_rows.append({
                '출발_동': a,
                '도착_동': c,
                '지하철_승객수': 0,
                '버스_승객수': 0,
                '택시_승객수': 0,
                '연별 합계': round(est_sum)
            })

# 5. 결과 저장
output_path = "D:/SITE/●국민대/대외활동/●국토 • 교통 데이터활용 경진대회/data/hop2_OD_추정.csv"
df_result = pd.DataFrame(new_rows)
df_result.to_csv(output_path, encoding="cp949", index=False)

print(f"hop=2 보간 완료: {len(df_result)}개 OD쌍 생성됨 → {output_path}")
