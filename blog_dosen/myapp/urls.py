from django.urls import path
from . import views

urlpatterns = [
    path('publikasi/', views.publikasi_view, name='publikasi'),
    path('', views.landing_page, name='landing_page'),
    path('pkm/', views.pkm_list, name='pkm_list'),
    path('pkm/<int:pk>/', views.pkm_detail, name='pkm_detail'),
    path('research/', views.research_list, name='research_list'),
    path('research/<int:pk>/', views.research_detail, name='research_detail'),
    path('research/project_gallery/<int:id>/', views.project_gallery, name='project_gallery'),
    path('teaching/', views.teaching, name='teaching'),
    path('teachingdetail/', views.teachingdetail, name='teachingdetail'),
    path('teachingdetail2/', views.teachingdetail2, name='teachingdetail2'),
    path('teachingdetail3/', views.teachingdetail3, name='teachingdetail3'),
    # path('riset/', views.research_, name='research'),
]

