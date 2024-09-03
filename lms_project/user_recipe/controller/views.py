from rest_framework import viewsets, status
from rest_framework.response import Response
from user_recipe.service.user_recipe_service_impl import UserRecipeServiceImpl

class UserRecipeView(viewsets.ViewSet):
    userRecipeService = UserRecipeServiceImpl.getInstance()

    def createUserRecipe(self, request):
        try:
            accountId = request.data.get("accountId")

            if not accountId:
                return Response({"error": "accountId is required"}, status=status.HTTP_400_BAD_REQUEST)
            print(f"Received accountId: {accountId}")

            userRecipeId = self.userRecipeService.createUserRecipe(accountId)
            return Response({"userRecipeId": userRecipeId.user_recipe_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def getUserRecipe(self, request):
        try:
            accountId = request.query_params.get("accountId")
            userRecipeId = request.query_params.get("userRecipeId")

            if not accountId or not userRecipeId:
                return Response({"error": "accountId and userRecipeId are required"}, status=status.HTTP_400_BAD_REQUEST)

            userRecipeIdInstance = self.userRecipeService.getUserRecipe(accountId, userRecipeId)
            return Response({
                "accountId": userRecipeIdInstance.account_id,
                "userRecipeId": userRecipeIdInstance.user_recipe_id,
            }, status=status.HTTP_200_OK)
        except UserRecipe.DoesNotExist:
            return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def deleteUserRecipe(self, request):
        try:
            accountId = request.data.get("accountId")
            userRecipeId = request.data.get("userRecipeId")

            if not accountId or not userRecipeId:
                return Response({"error": "accountId and userRecipeId are required"}, status=status.HTTP_400_BAD_REQUEST)

            self.userRecipeService.deleteUserRecipe(accountId, userRecipeId)
            return Response({"message": "Recipe deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
