# diary/urls.py
from django.urls import path
from .views import EntryCreateView, EntryListView

app_name = 'diary'

urlpatterns = [
    path('entries/', EntryListView.as_view(), name='entry_list'),
    path('entries/new/', EntryCreateView.as_view(), name='entry_create'),
]
