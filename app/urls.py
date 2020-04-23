from django.urls import path, include
from graphene_django.views import GraphQLView
from grapheneApp.schema import schema
from .views import home

urlpatterns = [
    path('', home),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),

]
