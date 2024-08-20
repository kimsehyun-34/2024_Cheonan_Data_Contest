import pandas as pd
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

file_path = './python/천안_빵소.csv'
bakery_data = pd.read_csv(file_path)

input_items = json.loads(sys.argv[1])

def recommend_bakery(input_items, bakery_data):
    best_match = None
    best_score = 0
    
    # Iterate over each bakery
    for index, row in bakery_data.iterrows():
        
        menu_items = row['주 메뉴'].split(', ')
        
        score = len(set(input_items) & set(menu_items))
        
        if score > best_score:
            best_match = row['name']
            best_score = score
    
    return best_match

# input_items = ['우유식빵', '찰떡빵', '소금빵']

recommended_bakery = recommend_bakery(input_items, bakery_data)

print(recommended_bakery)