from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'ingredients', views.IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('csrf/', views.csrf)
]
