from django.urls import path
from . import views


urlpatterns = [
    path('stockentry/list/', views.StockEntryListView.as_view(), name='stock_entry_list'),
    path('stockentry/create/', views.StockEntryCreateView.as_view(), name='stock_entry_create'),
    path('stockentry/<int:pk>/detail/', views.StockEntryDetailView.as_view(), name='stock_entry_detail'),
    path('stockentry/<int:pk>/update/', views.StockEntryUpdateView.as_view(), name='stock_entry_update'),
    path('stockentry/<int:pk>/delete/', views.StockEntryDeleteView.as_view(), name='stock_entry_delete'),
]
