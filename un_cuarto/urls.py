from django.urls import path, re_path
from . import views

app_name = "un_cuarto"

urlpatterns = [
    re_path(r'^$', views.StartView.as_view(), name='start_view'),
    # path('contact', views.ContactView.as_view(), name='contact'),
    re_path(r'comment/$', views.comment_view , name="comment"),
    re_path(r'detail/(?P<pk>[0-9])$', views.PortafolioDetailView.as_view(), name='detail'),
]