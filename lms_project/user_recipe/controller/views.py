from rest_framework import viewsets, status
from rest_framework.response import Response
from user_recipe.service.user_recipe_service_impl import UserRecipeServiceImpl

user_recipe_service = UserRecipeServiceImpl.getInstance()


class UserRecipeViewSet(viewsets.ViewSet):
    user_recipe_service = UserRecipeServiceImpl.getInstance()
    def create(self, request):
        account_id = request.data.get('accountId')
        recipe_hash = request.data.get('recipeHash')

        result = user_recipe_service.createUserRecipe(account_id, recipe_hash)

        if result:
            return Response({"message": "레시피 저장 완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "중복된 레시피입니다."}, status=status.HTTP_409_CONFLICT)

    def retrieve(self, request, pk=None):
        account_id = request.query_params.get('accountId')
        recipe_hash = request.query_params.get('recipeHash')

        recipe = user_recipe_service.getUserRecipeByAccountIdAndRecipeHash(account_id, recipe_hash)

        if recipe:
            return Response({"recipe": recipe}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "레시피가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        account_id = request.data.get('accountId')
        recipe_hash = request.data.get('recipeHash')

        result = user_recipe_service.deleteUserRecipeByAccountIdAndRecipeHash(account_id, recipe_hash)

        if result:
            return Response({"message": "레시피 삭제 완료"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "레시피 삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)

    # 추가된 메서드 (레시피 중복 확인)
    def checkRecipeDuplication(self, request):
        account_id = request.data.get('accountId')
        recipe_hash = request.data.get('recipeHash')

        # 중복 확인을 위해 서비스 레이어 호출
        existing_recipe = user_recipe_service.getUserRecipeByAccountIdAndRecipeHash(account_id, recipe_hash)

        if existing_recipe:
            return Response({"message": "중복된 레시피입니다."}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"message": "중복되지 않은 레시피입니다."}, status=status.HTTP_200_OK)
