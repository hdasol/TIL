from dataclasses import field
from .models import Article
from rest_framework import serializers

# ModelSerializer
# 역할 : 모델 폼과 같은 역할
#       클라이언트에서 입력한 data가 유효한지 확인
#       모델의 역할도 같이함(데이터를 임시 저장할 수 있는 객체 생성 및 데이터베이스 CRUD가능)
#       클라이언트에 응답할 데이터도 만들어준다.

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

