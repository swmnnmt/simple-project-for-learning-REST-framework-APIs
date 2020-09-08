from django.urls import path

from web.views import GetAllData

urlpatterns = [
    path('get-all-data/', GetAllData.as_view())
]
