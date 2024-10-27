from django.shortcuts import render, redirect
from .models import Video
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "GET":
        videos = Video.objects.all()
        return render(request, 'index.html', {'videos':videos})
    elif request.method == "POST":
        print(request.POST)
        print(request.FILES)
        video_file = request.FILES.get("video")
        if video_file:
            print("video is uploaded")
            Video.objects.create(video = video_file, caption=request.POST.get("caption"), description=request.POST.get("description"))
        return redirect("/home/")
        #video = Video.objects.create()
    

def delete_video(request):
    if request.method =="DELETE":
        if request.POST.get("caption"):
            pass
