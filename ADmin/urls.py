from django.urls import path
from . import views
urlpatterns = [
    path("admin_login/",views.ADmin_login,name="admin_login"),
    path("admin_logout/",views.logout_view,name="logout"),
    path("admin_index/",views.ADmin_index,name="admin_index"),
    path("single_view/<int:id>/",views.csv_to_objects,name="single_view")

]
