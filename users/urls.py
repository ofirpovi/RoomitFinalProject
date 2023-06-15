from django.urls import path
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('register/', users_views.register, name='register'),
    path('login/', users_views.CustomLoginView.as_view(template_name= 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name='logout'),
    path('fill_info/<str:username>/', users_views.info, name='fill_info'),
    path('profile/<str:username>/', users_views.profile, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name= 'users/password_reset.html', html_email_template_name = 'users/password_reset_email.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'users/password_reset_complete.html'), name='password_reset_complete'),
    path('set-status/', users_views.set_status, name='set-status'),
    path('change-status/', users_views.change_status, name='change-status'),
    path('property-offer-create/<str:username>/', users_views.create_property_offer_view, name='property-offer-create'),
    path('property-offer-display/<str:username>/', users_views.display_property_offer, name='property-offer-display'),
    path('property-reqs-display/<str:username>/', users_views.display_property_reqs, name='property-reqs-display'),
    path('roomi-reqs-display/<str:username>/', users_views.display_roomi_reqs, name='roomi-reqs-display'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
