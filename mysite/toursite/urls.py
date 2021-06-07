from django.urls import path
from .views import HomePageView, PageDetailView,CategoryDetailView,TourDetailView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('page/<slug:slug>', PageDetailView.as_view(),name='page-detail'),
    path('category/<slug:slug>', CategoryDetailView.as_view(),name='category-detail'),
    path('tour/<slug:slug>', TourDetailView.as_view(),name='tour-detail'),

]

