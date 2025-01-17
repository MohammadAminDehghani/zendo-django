from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
    # path('', views.event_list, name='event_list'),
    # path('<int:event_id>/', views.event_detail, name='event_detail'),

    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:event_id>/', EventDetailView.as_view(), name='event_detail'),
]
