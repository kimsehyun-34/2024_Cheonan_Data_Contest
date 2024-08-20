import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

file_path = 'python/천안_식당.csv'
restaurant_data = pd.read_csv(file_path, encoding='cp949')

def recommend_restaurants(data, user_input, top_n=3):
    data.columns = data.columns.str.strip()

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(data['주 메뉴'].astype(str))

    user_tfidf = tfidf.transform([user_input])
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()

    data['유사도'] = cosine_similarities
    filtered_data = data[(data['맛집'] == 'Y') | (data['모범음식점'] == 'Y')]

    recommended_restaurants = filtered_data.sort_values(by='유사도', ascending=False).head(top_n)
    
    return recommended_restaurants[['식당명']]

user_input = "갈비" #음식 입력

recommended_restaurants = recommend_restaurants(restaurant_data, user_input)

restaurant_list = recommended_restaurants['식당명'].tolist()

print(restaurant_list)
