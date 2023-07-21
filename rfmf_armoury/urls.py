from django.contrib import admin
from django.urls import path, include


# Admin Site Config
admin.site.site_header = 'RFMF Armoury Application'
admin.site.site_title = 'RFMF Armoury Application Sample'
admin.site.index_title = 'RFMF Armoury Web Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('arms.urls')),
]
