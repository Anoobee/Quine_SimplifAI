from django.urls import path
from . import views

urlpatterns = [
    path('upload_report/', views.ReportView.as_view(), name='upload_report'),
    path('get_report_lists/', views.get_report_lists, name='get_report_lists'),
    path('chat_message/', views.chat_message, name='chat_message'),
]