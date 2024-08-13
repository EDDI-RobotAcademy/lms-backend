import os
import django
import pandas as pd
from tqdm import tqdm

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms_project.settings")
django.setup()
from django.db import transaction
from recipe.entity.recipe_content import RecipeContent
from recipe.entity.recipe_ingredient import RecipeIngredient
from recipe.entity.recipe_title import RecipeTitle

def insert_recipe_title(row):
    try:
        recipe_title = RecipeTitle.objects.create(
            title=row['CKG_NM'],
            category=row['CKG_MTH_ACTO_NM']
        )
        return recipe_title
    except Exception as e:
        print(f"An error occurred while inserting into RecipeTitle: {e}")
        return None

def insert_recipe_ingredient(row, recipe_title):
    try:
        RecipeIngredient.objects.create(
            ingredient=row['CKG_MTRL_CN'],
            plate=row['CKG_INBUN_NM'],
            recipe_id=recipe_title
        )
    except Exception as e:
        print(f"An error occurred while inserting into RecipeIngredient: {e}")

def insert_recipe_content(row, recipe_title):
    try:
        RecipeContent.objects.create(
            content=row['RCP_CONTENT'],
            recipe_id=recipe_title
        )
    except Exception as e:
        print(f"An error occurred while inserting into RecipeContent: {e}")

def insert_data_from_dataframe(df):
    try:
        for _, row in tqdm(df.iterrows(), total=df.shape[0], desc='DB에 데이터 넣는 중...: '):
            recipe_title = insert_recipe_title(row)
            if recipe_title is not None:
                insert_recipe_ingredient(row, recipe_title)
                insert_recipe_content(row, recipe_title)
        print('All data has been successfully inserted into table.')
    except Exception as e:
        print(f"데이터 넣는 중 error 발생 : {e}")


# 예외 데이터 처리
def delete_recipes_without_ingredients():
    try:
        # 트랜잭션 시작
        with transaction.atomic():
            # RecipeIngredient에 포함되지 않은 RecipeTitle 레코드를 찾기
            recipe_titles_without_ingredients = RecipeTitle.objects.filter(
                recipeingredient__isnull=True
            )

            if recipe_titles_without_ingredients.exists():
                # 관련된 RecipeContent 레코드를 삭제
                RecipeContent.objects.filter(recipe_id__in=recipe_titles_without_ingredients).delete()

                # 관련된 RecipeTitle 레코드를 삭제
                recipe_titles_without_ingredients.delete()

            print("재료 없는 데이터 row 삭제 완료")

    except Exception as e:
        print(f"데이터 정리 과정에서 error 발생: {e}")



if __name__ == '__main__':
    df = pd.read_pickle('data_encoding_processing/result/preprocessed_df_28703.pkl')
    insert_data_from_dataframe(df)
    delete_recipes_without_ingredients()