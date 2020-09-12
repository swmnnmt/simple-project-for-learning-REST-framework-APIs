from django.urls import path

from web.views import GetAllData, GetFavData, UpdateStoryData, PostModelData, PostData, SearchData

urlpatterns = [
    path('get-all-data/', GetAllData.as_view()),
    path('get-favorite-data/', GetFavData.as_view()),
    path('update-story-data/<int:pk>/', UpdateStoryData.as_view()),
    path('post-model-data/', PostModelData.as_view()),
    # Custom Serializer path:
    path('post-data/', PostData.as_view()),
    path('search-data/', SearchData.as_view()),
]
