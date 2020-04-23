import graphene
from graphene_django.types import DjangoObjectType
from app.models import Category, Ingredient


class CategoryTypes(DjangoObjectType):
    class Meta:
        model = Category
class IngredientTypes(DjangoObjectType):
    class Meta:
        model = Ingredient

class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryTypes)
    all_ingredients = graphene.List(IngredientTypes)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()

schema = graphene.Schema(query=Query)

