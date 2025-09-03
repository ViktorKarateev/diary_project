# diary/urls.py
from django.urls import path
from .views import EntryCreateView, EntryListView, EntryUpdateView, EntryDeleteView, EntryDetailView

app_name = 'diary'

urlpatterns = [
    path('entries/', EntryListView.as_view(), name='entry_list'),
    path('entries/new/', EntryCreateView.as_view(), name='entry_create'),
    path('entries/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit'),
    path('entries/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),
    path("entries/<int:pk>/", EntryDetailView.as_view(), name="entry_detail"),
]
