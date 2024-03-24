from django.urls import path
from users import views

urlpatterns = [
    path('singup/', views.SignUpView.as_view(), name='signup'),
    path('personal_account/create_profile/', views.create_profile, name='create_profile'),
    path('personal_account/edite_profile/', views.edite_profile, name='edite_profile')
]
