from django.urls import path
import views

urlpatterns = [
    path('', views.blog, name="my-blog"),
    path('about-me', views.about_me, name="about-me"),
    path('my-resume', views.resume, name="my-resume"),
    path('git-repos', views.git_api),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

