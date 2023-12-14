from django.shortcuts import render

# Create your views here.
def index(request):
    print("傻逼")
    items = [
        {
            "title": "爱书网",
            "content": "干你妈的",

        },
        {
            "title": "爱书网",
            "content": "干你妈的",

        },
        {
            "title": "爱书网",
            "content": "干你妈的",

        },
        {
            "title": "爱书网",
            "content": "干你妈的",

        },
    ]
    return render(request, "index/index.html", {"items": items})