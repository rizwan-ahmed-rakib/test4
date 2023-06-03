from django.shortcuts import render
from videos.models import MyVideo


# Create your views here.
def index(request):
    videos = MyVideo.objects.all()
    return render(request, 'video_app/index.html', context={'videos': videos})
