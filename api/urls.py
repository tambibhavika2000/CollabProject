
from django.urls import path
from api import views

urlpatterns = [
    path('', views.overview, name="api-overview"),
	path('contest-list/', views.ContestList, name="contest-list"),
	path('contest-detail/<str:pk>/', views.ContestDetail, name="contest-detail"),
	path('contest-create/', views.ContestCreate, name="contest-create"),

	path('contest-update/<str:pk>/', views.ContestUpdate, name="contest-update"),
	path('contest-delete/<str:pk>/', views.ContestDelete, name="contest-delete"),
]