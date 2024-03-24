from django.urls import path
from real_estate import views

urlpatterns = [
    path('', views.index, name='index'),
    path('personal_account/create_announcement/', views.create_announcement, name='create_announcement'),
    path('personal_account/edit_announcement/<int:estate_id>/', views.edit_announcement, name='edit_announcement'),
    path('personal_account/', views.personal_account, name='personal_account'),
    path('detail_estate/<int:estate_id>/', views.detail_estate, name='detail_estate'),
    path('delete_announcement/<int:estate_id>/', views.delete_announcement, name='delete_announcement'),
    path('all_sellers_announcements/<int:user_id>/', views.all_sellers_announcements, name='all_sellers_announcements'),
    path('deal_request/<int:estate_id>/', views.deal_request_view, name='deal_request'),
    path('read_all_messages/', views.read_all_messages, name='read_all_messages'),
    path('read_detail_message/<int:deal_request_id>/', views.read_detail_message, name='read_detail_message'),
    path('personal_account/edit_announcement/<int:estate_id>/add_photo/', views.add_photo, name='add_photo'),
]
