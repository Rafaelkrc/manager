from django.urls import path
from . import views

urlpatterns = [
    path('organization/list/', views.OrganizationListView.as_view(), name='organization_list'),
    path('organization/create/', views.OrganizationCreateView.as_view(), name='organization_create'),
    path('organization/<int:pk>/detail/', views.OrganizationDetailView.as_view(), name='organization_detail'),
    path('organization/<int:pk>/update/', views.OrganizationUpdateView.as_view(), name='organization_update'),
    path('organization/<int:pk>/delete/', views.OrganizationDeleteView.as_view(), name='organization_delete'),
]
