from django.urls import path
from . import views

urlpatterns = [
    path('publikasi/', views.publikasi_view, name='publikasi'),
    path('', views.landing_page, name='landing_page'),
    path('pkm/', views.pkm_, name='pkm'),
    path('research/', views.detail_project, name='detail_project'),
    path('gallery/', views.project_gallery, name='project_gallery'),
]

