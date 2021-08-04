from django.db.models import query
from demo.serializers import UserSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from django.shortcuts import render

from .models import User
from .serializers import UserSerializer

# Create your views here.
def IndexPage(request):
    queryset = User.objects.all()
    print(queryset)
    serializer = UserSerializer(queryset, many = True)
    print(serializer.data)
    
    return render(request, 'index.html', context = {'entry': serializer.data })

class UserEntryView(CreateAPIView):
    serializer_class = UserSerializer
    