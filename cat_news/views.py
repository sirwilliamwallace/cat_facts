from django.shortcuts import render
import requests


proxies = {
    "http": "127.0.0.1:9050",
    "https": "1270.0.0.1:41691",
}
base_url = 'https://cat-fact.herokuapp.com/'
# Create your views here.
def base(request):
    return render(request,'index.html')


def cat_fact(request):
    res = requests.get(base_url+'facts').json()
    facts = res["all"][0]["text"]
    # print(facts)
    context = {
        "title": "cat facts",
        "facts": facts,
    }
    return render(request, 'cat_news.html', context=context)