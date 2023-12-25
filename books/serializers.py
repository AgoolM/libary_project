from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book
#from rest_framework.exception import ValidationError  
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','content', 'subtitle', 'author', 'isbn', 'price')
    
    def validate(self, data):
        title = data.get('title',None)
        author = data.get('author',None)
        
        if not title.isalpha():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Kitobni titleini tekshirib ko'ring hariflardantashkil topish kerak "
                }
            )

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Sarlavha va muallif bir xil bulmasligi kerak"
                }
                )
        return data