from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_index,name='user_index'),
    path('user_csv_uploader/',views.user_csv_uploader,name='user_csv_uploader'),
    path('user_xlsx_uploader/',views.user_xlsx_uploader,name='user_xlsx_uploader'),

]
