import folium

from django.shortcuts import render
from django.views import View


# Create your views here.
class NewsView(View):
    def get(self, request):
        return render(request, 'news/news.html')

    def post(self, request):
        pass