from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_recipe.controller.views import UserRecipeViewSet

router = DefaultRouter()
router.register(r'user_recipe', UserRecipeViewSet, basename='user_recipe')

urlpatterns = [
    path('', include(router.urls)),

    # 추가 엔드포인트 (특정 메서드에 대한 라우팅)
    path('duplicate-check', UserRecipeViewSet.as_view({'post': 'checkRecipeDuplication'}), name='recipe-duplicate-check'),
    path('create-recipe', UserRecipeViewSet.as_view({'post': 'createRecipe'}), name='create-recipe'),
    path('get-recipe', UserRecipeViewSet.as_view({'post': 'findRecipe'}), name='get-recipe'),
    path('delete-recipe', UserRecipeViewSet.as_view({'delete': 'deleteRecipe'}), name='delete-recipe'),
]