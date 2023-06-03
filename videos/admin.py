from django.contrib import admin
from videos.models import MyVideo
from embed_video.admin import AdminVideoMixin


# Register your models here.
class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(MyVideo, AdminVideo)
