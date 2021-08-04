from django.urls import path

from .views import IndexPage, UserEntryView

urlpatterns = [
    path('', IndexPage, name = "demo"),
    path('api/createuser', UserEntryView.as_view(), name = "adduser")
]