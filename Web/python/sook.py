import pandas as pd
import sys

min = sys.argv[1]
max = sys.argv[2]
min = int(min)
max = int(max)
sys.stdout.reconfigure(encoding='utf-8')

# Load the dataset
file_path = 'python/천안_숙박.csv'
accommodation_data = pd.read_csv(file_path, encoding='cp949')

def recommend_accommodations(data, price_min, price_max):
    # Clean column names
    data.columns = data.columns.str.strip()
    
    # 1. Convert '평균 가격' to numeric by removing commas and converting to int, handling NaN values
    data = data.dropna(subset=['평균 가격'])
    data['평균 가격'] = data['평균 가격'].str.replace(',', '').astype(int)
    
    # 2. Filter accommodations within the given price range
    filtered_data = data[(data['평균 가격'] >= price_min) & (data['평균 가격'] <= price_max)]
    
    # 3. Calculate the midpoint of the provided price range
    price_midpoint = (price_min + price_max) / 2
    
    # 4. Find the accommodations with the closest average price to the midpoint
    filtered_data['가격 차이'] = abs(filtered_data['평균 가격'] - price_midpoint)
    filtered_data = filtered_data.sort_values(by=['가격 차이', '평점'], ascending=[True, False])
    
    # 5. Select the top 5 accommodations by 평점
    top_accommodations = filtered_data.head(5)
    
    return top_accommodations[['숙박시설 이름']]

# Example user inputs
price_min = min
price_max = max

# Get the top 5 recommended accommodations
recommended_accommodations = recommend_accommodations(accommodation_data, price_min, price_max)

# Convert the result to a list and print
accommodation_list = recommended_accommodations['숙박시설 이름'].tolist()
print(accommodation_list)