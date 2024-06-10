from django.urls import path
from .views import JobListView, JobCreateView, JobUpdateView, JobDeleteView, CreateApplicationView

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('job/new/', JobCreateView.as_view(), name='job_create'),
    path('job/<int:pk>/edit/', JobUpdateView.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('job/<int:pk>/apply/', CreateApplicationView.as_view(), name='application_create')
]
