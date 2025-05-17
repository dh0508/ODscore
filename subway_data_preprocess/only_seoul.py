import os
import pandas as pd

# 서울시 25개 구 리스트
seoul_districts = [
    '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구',
    '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구',
    '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'
]

# 경로 설정
input_dir = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 수단OD'
output_dir = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 수단OD 서울'

# 파일 처리 루프
for month in range(1, 13):
    for day in range(1, 32):
        try:
            # 날짜 문자열 생성
            date_str = f'2024{month:02d}{day:02d}'
            file_name = f'동별_수단OD_{date_str}.csv'
            input_path = os.path.join(input_dir, file_name)

            # 파일이 존재하지 않으면 건너뜀
            if not os.path.exists(input_path):
                continue

            # CSV 파일 읽기
            df = pd.read_csv(input_path, encoding='euc-kr')

            # 서울시 내부 구만 필터링
            df_filtered = df[
                (df['출발_구'].isin(seoul_districts)) &
                (df['도착_구'].isin(seoul_districts))
            ]

            # 저장 파일 이름
            output_file_name = f'동별_수단OD 서울_{date_str}.csv'
            output_path = os.path.join(output_dir, output_file_name)

            # CSV 저장
            df_filtered.to_csv(output_path, index=False, encoding='euc-kr')

            print(f"{file_name} 처리 완료 → 저장됨: {output_file_name}")

        except Exception as e:
            print(f"{file_name} 처리 중 오류 발생: {e}")
