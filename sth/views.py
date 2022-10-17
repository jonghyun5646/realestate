import json
import requests
from django.shortcuts import render
from django.views import View

from sth.models import Multi


# Create your views here.
class MultiView(View):
    def get(self, request):
        multi = Multi.objects.select_related().filter(sigungu__contains="nope")
        crd = {"lat": 37.4858838, "lng": 126.8973216, "error": "fine"}

        context = {'mul': multi, "crd": crd}
        return render(request, 'sth/multi.html', context)

    def post(self, request):
        gu = request.POST['gu']
        dong = request.POST['dong']
        searched = request.POST['searched']
        addr = gu + " " + dong
        multi = Multi.objects.select_related().filter(sigungu__contains=addr)

        try:
            crd = find_crd(addr + searched)

        except Exception as e:
            try:
                crd = find_crd(addr)
            except Exception as e:
                crd = {"lat": 37.4858838, "lng": 126.8973216, "error": e}

        context = {'mul': multi, "crd": crd}
        return render(request, 'sth/multi.html', context)


def find_crd(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK 06b665abccae1b7ca9b1ad97a115b5e7"}
    api_json = json.loads(str(requests.get(url, headers=headers).text))
    address = api_json['documents'][0]['address']
    crd = {"lat": address['y'], "lng": address['x'], "error": "fine"}
    return crd
