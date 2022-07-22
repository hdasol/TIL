import json
from pprint import pprint

def movie_info(movie):
        
    key_list = {'genre_ids', 'id', 'overview', 'poster_path', 'title', 'vote_average'}
    dict_key = {}
    for key in key_list:
        dict_key[key] = movie[key] #key, value 쌍이 추가

    return dict_key
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
   
