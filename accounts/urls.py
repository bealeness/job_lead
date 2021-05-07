from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView, JobDeleteView
from . import views

urlpatterns = [
    path('profile/', JobListView.as_view(), name="profile"),
    path('job/<int:pk>/', JobDetailView.as_view(), name="job-detail"),
    path('job/new/', JobCreateView.as_view(), name="job-create"),
    path('job/<int:pk>/delete', JobDeleteView.as_view(), name="job-delete")
]
