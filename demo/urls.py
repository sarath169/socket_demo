from django.urls import path

from .views import IndexPage, UserEntryView
from .consumers import UpdtaeUserList

urlpatterns = [
    path('', IndexPage, name = "demo"),
    path('api/createuser', UserEntryView.as_view(), name = "adduser")
    
]

websocket_urlpatterns = ['ws_users/',UpdtaeUserList]