from django.urls import path

from web.views import GetAllData, GetFavData, PostModelData, PostData, SearchData, EditData, getalldata

urlpatterns = [
    # Class Based GET ALL DATA :
    path('get-all-data/', GetAllData.as_view()),
    # Function Based GET ALL DATA :
    path('get-data/', getalldata),
    path('get-favorite-data/', GetFavData.as_view()),
    path('post-model-data/', PostModelData.as_view()),
    # Custom Serializer path:
    path('post-data/', PostData.as_view()),
    # update url gets ?name as the id we wanna search that name in story name
    path('search-data/', SearchData.as_view()),
    # update url gets ?id as the id we wanna delete/update that
    path('edit-data/', EditData.as_view()),
]
