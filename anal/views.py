import folium

from django.shortcuts import render
from django.views import View


# Create your views here.
class AnalView(View):
    def get(self, request):
        return render(request, 'anal/anal.html')

    def post(self, request):
        pass


class PredView(View):
    def get(self, request):
        return render(request, 'anal/pred.html')

    def post(self, request):
        pass