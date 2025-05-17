import os
import pandas as pd

# 폴더 경로 설정
input_dir = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 수단OD 서울 동합침'
output_file = r'D:\SITE\●국민대\대외활동\●국토 • 교통 데이터활용 경진대회\data\동별 수단OD 서울 동합침_최종.csv'

# 모든 CSV를 담을 리스트
all_dfs = []

# 폴더 내 파일 반복
for file_name in os.listdir(input_dir):
    if file_name.startswith('동별_수단OD 서울 동합침_') and file_name.endswith('.csv'):
        file_path = os.path.join(input_dir, file_name)
        try:
            df = pd.read_csv(file_path, encoding='euc-kr')
            # '기준일자' 열이 있으면 제거
            df = df.drop(columns=['기준일자'], errors='ignore')
            all_dfs.append(df)
        except Exception as e:
            print(f"[오류] {file_name}: {e}")

# 데이터 합치고 그룹화
if all_dfs:
    combined_df = pd.concat(all_dfs, ignore_index=True)

    # ✅ 출발_동, 도착_동 기준으로 합산
    result = combined_df.groupby(
        ['출발_동', '도착_동'],
        as_index=False
    ).sum(numeric_only=True)

    # 결과 저장
    result.to_csv(output_file, index=False, encoding='euc-kr')
    print(f"[✔ 완료] 최종 파일 저장: {output_file}")
else:
    print("[❌ 실패] 처리할 파일이 없습니다.")
