from django.urls import path
from . import views

urlpatterns = [
    path('organization/list/', views.OrganizationListView.as_view(), name='organization_list'),
]
