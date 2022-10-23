from sys import api_version
from urllib import response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer


# Create your views here.
# articles/ CREATE
@api_view(['GET', 'POST'])
def article_list(request):
    # 모델폼 사용했을 때 저장 어떻게 사용함?
    # 데이터가 들어오면 받아서 form객체 만들고
    # form 객체가 유효한지 확인하고
    # form 객체가 가지고 있는 save()함수 호출
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            # 정상 저장되었음을 알려주면 됨
            # django rest_framework이 제공하는 방식으로 응답하면 됩니다.
            return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        # 게시글 전체 목록 조회
        articles = Article.objects.all()
    return Response(status=status.HTTP_404_NOT_FOUND)

# articles/<int:pk>/  UPDATE, DELETE, READ
def article_detail(requset):
    pass
