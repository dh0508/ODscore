import pandas as pd

# 파일 경로
input_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\서울특별시_일자별 택시 OD 유형별 상위 10개소('24년).xlsx"
output_path = r"D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\택시 OD.xlsx"

# 데이터 불러오기
df = pd.read_excel(input_path)

# 행정동 OD 추출
admin_df = df[['기준_날짜', '행정동_시작_명칭', '행정동_종료_명칭', '행정동_이용수']].copy()
admin_df.columns = ['기준_날짜', '시작_명칭', '종료_명칭', '이용수']

# 중복 확인용 세트 생성
admin_set = set(zip(admin_df['기준_날짜'], admin_df['시작_명칭'], admin_df['종료_명칭']))

# 외부통행 OD 추출 및 필터
out_df = df[['기준_날짜', '외부통행_행정동_시작_명칭', '외부통행_행정동_종료_명칭', '외부통행_행정동_이용수']].copy()
out_df.columns = ['기준_날짜', '시작_명칭', '종료_명칭', '이용수']
out_df = out_df[~out_df.apply(lambda row: (row['기준_날짜'], row['시작_명칭'], row['종료_명칭']) in admin_set, axis=1)]

# 최종 병합
final_df = pd.concat([admin_df, out_df], ignore_index=True)

# 저장
final_df.to_excel(output_path, index=False)
print("✅ '택시 OD.xlsx' 저장 완료")
