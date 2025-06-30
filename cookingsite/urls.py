from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from cookingapi.viewsets import UserViewSet, IngredientViewSet, RecipeViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path("auth/", include("django.contrib.auth.urls")),
    path('api-auth/', include('rest_framework.urls')),
]
