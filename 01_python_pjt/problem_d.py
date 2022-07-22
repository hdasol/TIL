import json


def max_revenue(movies):

    boxs = [] #13, 122, 129, ....
    #box = [13, 빨간망토].......

    for i in movies:
        box = []
        box.append(i['id'])
        box.append(i['title'])
        boxs.append(box) #2차 배열 만듬

    money2 = 0
    name = ''
    
    for j in boxs:
        id = j[0] #13
        movies_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movies_list = json.load(movies_json)
        
        money = movies_list['revenue']
        
        if money > money2:
            money2 = money
            name = j[1]
    
    return name
        

        
        

        

    
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
