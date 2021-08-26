import graphene
from graphene_django import DjangoObjectType

from . import models


class FruitType(DjangoObjectType):
    class Meta:
        model = models.Fruit
        fields = [
            'id',
            'name',
        ]


class FruitMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    fruit = graphene.Field(FruitType)

    @classmethod
    def mutate(cls, root, info, name, id):
        fruit = models.Fruit.objects.get(pk=id)
        fruit.name = name
        fruit.save()
        # Notice we return an instance of this mutation
        return FruitMutation(fruit=fruit)


class Mutation(graphene.ObjectType):
    update_fruit = FruitMutation.Field()


class Query(graphene.ObjectType):
    fruits = graphene.List(FruitType)

    def resolve_fruits(root, info, **kwargs):  # self is root
        return models.Fruit.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
