from django.shortcuts import render
from .models import Video

# Create your views here.
def home(request):
    if request.method == "GET":
        videos = Video.objects.all()
        return render(request, 'index.html', {'videos':videos})
    elif request.method == "POST":
        data = Video(request.POST)
        print("video is uploaded")
        print(data)
        #video = Video.objects.create()
    