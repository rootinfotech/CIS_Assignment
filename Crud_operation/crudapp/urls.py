from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Homeview, name='home'),
    path('register/', views.Register_view, name='register'),
    path('login/', views.Login_view, name='login'),
    path('logout/', views.Logout_view, name='logout'),
    path('admin-view/', views.Admin_view, name='admin_view'),
    path('add-product/', views.Add_product, name='add_product'),
    path('view-product/', views.View_product, name='view_product'),
    path('update-product/<int:id>/', views.Update_product, name='update_product'),
    path('delete-product/<int:id>/', views.Delete_Product, name='delete_product'),
    path('add-category/', views.Add_category, name='add_category'),
    path('view-category/', views.View_category, name='view_category'),
    path('update-category/<int:id>/', views.Update_category, name='update_category'),
    path('delete-category/<int:id>/', views.Delete_category, name='delete_category'),
    path('search/', views.Admin_search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)