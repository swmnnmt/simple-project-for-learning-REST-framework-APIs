from django.urls import path

from web.views import GetAllData, GetFavData, UpdateStoryData

urlpatterns = [
    path('get-all-data/', GetAllData.as_view()),
    path('get-favorite-data/', GetFavData.as_view()),
    path('update-story-data/<int:pk>/', UpdateStoryData.as_view()),
]
