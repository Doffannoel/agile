from django.urls import path
from . import views

urlpatterns = [
    path('publikasi/', views.publikasi_view, name='publikasi'),
]

urlpatterns = [
    path('research/', views.detail_project, name='detail_project'),
]