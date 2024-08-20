import pandas as pd


file_path = 'python/천안_숙박.csv'
accommodation_data = pd.read_csv(file_path, encoding='cp949')

def recommend_accommodations(data, price_min, price_max):

    data.columns = data.columns.str.strip()

    data = data.dropna(subset=['평균 가격'])
    data['평균 가격'] = data['평균 가격'].str.replace(',', '').astype(int)

    filtered_data = data[(data['평균 가격'] >= price_min) & (data['평균 가격'] <= price_max)]

    price_midpoint = (price_min + price_max) / 2

    filtered_data['가격 차이'] = abs(filtered_data['평균 가격'] - price_midpoint)
    filtered_data = filtered_data.sort_values(by=['가격 차이', '평점'], ascending=[True, False])

    top_accommodations = filtered_data.head(5)
    return top_accommodations[['숙박시설 이름']]

# 가격입력
price_min = 60000
price_max = 70000

# Get the top 5 recommended accommodations
recommended_accommodations = recommend_accommodations(accommodation_data, price_min, price_max)

# Convert the result to a list and print
accommodation_list = recommended_accommodations['숙박시설 이름'].tolist()
print(accommodation_list)