from django.urls import path

from chat import api

urlpatterns = [
    path("", api.conversations_list, name="conversations_list"),
    path("start/<uuid:user_id>/", api.conversations_start, name="api_conversations_start"),
    path("<uuid:pk>/", api.conversations_detail, name="conversations_detail"),
]


