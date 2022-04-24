# from dataclasses import field
# import graphene
# from graphene_django import DjangoObjectType
# from .models import Books

# class  BooksType(DjangoObjectType):
#     class Meta:
#         model = Books
#         fields =('id','title','excerpt')


# class Query(graphene.ObjectType):

#     all_books = graphene.List(BooksType)

#     def resolve_all_books(root, info):
#         return Books.objects.filter(title="Poppy") #.all()

# schema = graphene.Schema(query=Query)


from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category","quiz")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

class Query(graphene.ObjectType):
    quiz= graphene.String()
    all_quizzes= DjangoListField(QuizzesType)
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())    
    
    def resolve_quiz(root, info):
        return f"this is first quiz"

    #def resolve_all_quizzes(root, info):
    #    return Quizzes.objects.all()   

    def resolve_all_questions(root, info, id):
       return Question.objects.get(pk=id)
    
    def resolve_all_answers(root, info, id):
       return Answer.objects.filter(question=id)


class CategoryMutation(graphene.Mutation):

    class Arguments:
        name= graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(root, info,name):
        category=Category(name=name)
        category.save()


class Mutations(graphene.ObjectType):
    new_category = CategoryMutation.Field()

schema = graphene.Schema(query=Query , mutation= Mutations)

