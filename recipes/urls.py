from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>', views.recipe, name="recipe"),
    path('recipes/category/<int:id>', views.category, name="category"),
]

urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)

urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)
