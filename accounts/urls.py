from django.urls import path
from .views import JobDetailView, JobCreateView, JobDeleteView, JobUpdateView
from . import views as views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('job/<int:pk>/', JobDetailView.as_view(), name="job-detail"),
    path('job/new/', JobCreateView.as_view(), name="job-create"),
    path('job/<int:pk>/delete', JobDeleteView.as_view(), name="job-delete"),
    path('job/<int:pk>/update', JobUpdateView.as_view(), name="job-update"),
    path('applied/', views.applied, name="applied"),
    path('response/', views.response, name="response"),
    path('replied/', views.replied, name="replied"),
    path('interview/', views.interview, name="interview")
]
