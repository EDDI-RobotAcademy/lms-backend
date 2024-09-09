from rest_framework import viewsets, status
from rest_framework.response import Response
from user_recipe.service.user_recipe_service_impl import UserRecipeServiceImpl

class UserRecipeViewSet(viewsets.ViewSet):
    userRecipeService = UserRecipeServiceImpl.getInstance()
    def createRecipe(self, request):
        account_id = request.data.get('accountId')
        recipe_hash = request.data.get('recipeHash')

        result = self.userRecipeService.createUserRecipe(account_id, recipe_hash)
        if result:
            return Response({"message": "레시피 저장 완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "중복된 레시피입니다."}, status=status.HTTP_200_OK)

    def findRecipe(self, request, pk=None):
        account_id = request.data.get('accountId')
        recipe = self.userRecipeService.getHashedRecipeByAccountId(account_id)

        if recipe:
            return Response({"message": recipe}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "레시피가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def deleteRecipe(self, request, pk=None):
        account_id = request.data.get('accountId')
        recipe_hash = request.data.get('recipeHash')

        result = self.userRecipeService.deleteUserRecipeByAccountIdAndRecipeHash(account_id, recipe_hash)

        if result:
            return Response({"message": "레시피 삭제 완료"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "레시피 삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)

    # 추가된 메서드 (레시피 중복 확인)
    def checkRecipeDuplication(self, request):
        account_id = request.data.get('accountId')
        recipe_hash = request.data.get('recipeHash')

        # 중복 확인을 위해 서비스 레이어 호출
        existing_recipe = self.userRecipeService.getUserRecipeByAccountIdAndRecipeHash(account_id, recipe_hash)

        if existing_recipe:
            return Response({"message": "중복된 레시피입니다."}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"message": "중복되지 않은 레시피입니다."}, status=status.HTTP_200_OK)
