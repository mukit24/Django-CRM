from django.urls import URLPattern, path
from .views import lead_delete, lead_list,lead_detail,lead_create, lead_update,lead_delete,LeadListView

app_name='leads'

urlpatterns = [
    path('', LeadListView.as_view(),name='lead-list'),
    path('<int:pk>/',lead_detail,name='lead-detail'),
    path('<int:pk>/update',lead_update,name='lead-update'),
    path('<int:pk>/delete',lead_delete, name='lead-delete'),
    path('create/',lead_create,name='lead-create')
]