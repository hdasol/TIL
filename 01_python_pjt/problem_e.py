import json


def dec_movies(movies):

    boxs = []

    for i in movies:
        box = []
        box.append(i['id'])
        box.append(i['title'])
        boxs.append(box)

    Decem_movie = []

    for j in boxs:

        id = j[0]

        movies_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movies_list = json.load(movies_json)

        Date = movies_list['release_date'].split('-')
        # [1994, 3, 14]

        if Date[1] == '12':
            Decem_movie.append(j[1]) # j[1]은 title임!!
            

    return Decem_movie
              


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
