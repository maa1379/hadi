from django.urls import path

from .views import BlogListView

app_name = "blog"
urlpatterns = [
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
]

