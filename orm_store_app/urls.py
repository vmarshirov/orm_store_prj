from django.urls import path
from .import views

app_name = 'orm_store_app'
urlpatterns = [
    path('', views.index, name='index'),
    # path('datetime_nov/', views.datetime_nov, name='datetime_nov'),
    # path('list_dict/', views.list_dict, name='list_dict'),
    # path('form_create_0/', views.form_create_0, name='form_create_0'),
    # path('form_create/', views.form_create, name='form_create'),
    # path('form_result/', views.form_result, name='form_result'),
    # path("store_result/", views.store_result, name="websiteApp-store_result"),
    path('category/', views.category, name='category'),
    path('table/<int:pk>', views.table, name='table'),
    path('page/<int:pk>', views.page, name='page'),
    # path("store/", views.store),

]
