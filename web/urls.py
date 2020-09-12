from django.urls import path

# Class Based APIs
from web.views import GetAllData, GetFavData, PostModelData, PostData, SearchData, EditData
# Function Based APIs
from web.views import get_all_data, post_model_data

urlpatterns = [
    path('get-all-data/', GetAllData.as_view()),
    path('get-favorite-data/', GetFavData.as_view()),
    path('post-model-data/', PostModelData.as_view()),
    path('get_all_data/', get_all_data),
    path('post_data/', post_model_data),
    # Custom Serializer path for post Data:
    path('post-data/', PostData.as_view()),
    # update url gets ?name as the id we wanna search that name in story name
    path('search-data/', SearchData.as_view()),
    # update url gets ?id as the id we wanna delete/update that
    path('edit-data/', EditData.as_view()),
]
