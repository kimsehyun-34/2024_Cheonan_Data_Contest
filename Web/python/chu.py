import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
import sys

sex = sys.argv[1]
age = sys.argv[2]
age=int(age)
sys.stdout.reconfigure(encoding='utf-8')

# 데이터 로드
df = pd.read_csv('python/천안_관광지.csv')

# 특징 선택: 숫자형 데이터만 선택하여 정규화
features = df.columns[5:]  # 비율에 해당하는 컬럼들만 사용
X_numeric = df[features].select_dtypes(include=[float, int])
y = df['관광지명(소재지역)']

# 데이터 정규화
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_numeric)

# KNN 모델 생성
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_scaled, y)

# 사용자 입력 받기 및 추천 함수
def recommend_tourist_spots(gender, age, n_recommendations=5):
    age_ranges = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 100)]

    # 입력 받은 나이에 맞는 연령대 비율 컬럼 찾기
    for i, (low, high) in enumerate(age_ranges):
        if low <= age <= high:
            if gender == '남성':
                column = X_numeric.columns[i * 2]  # 남성 비율
            else:
                column = X_numeric.columns[i * 2 + 1]  # 여성 비율
            break

    user_data = [0] * len(X_numeric.columns)
    user_data[X_numeric.columns.get_loc(column)] = 1  # get_loc을 사용해 컬럼의 인덱스를 찾음

    # n개 추천
    distances, indices = model.kneighbors([user_data], n_neighbors=n_recommendations)
    recommended_spots = [y.iloc[index] for index in indices[0]]

    return recommended_spots

# 결과출력
recommended_spots = recommend_tourist_spots(sex, age, n_recommendations=10)
# print(f"추천 관광지들: {recommended_spots}")

print(recommended_spots)