import cx_Oracle

from django.shortcuts import render
from django.views import View

from sth.models import Multi


# Create your views here.
class AptView(View):
    def get(self, request):
        return render(request, 'sth/apt.html')

    def post(self, request):
        pass


class OfficeView(View):
    def get(self, request):
        return render(request, 'sth/office.html')

    def post(self, request):
        pass


class MultiView(View):
    def get(self, request):
        multi = Multi.objects.select_related()

        context = {'mul': multi}
        return render(request, 'sth/multi.html', context)

    def post(self, request):
        pass