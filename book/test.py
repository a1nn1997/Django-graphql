from django.test import TestCase
from . models import Category, Quizzes, Question, Answer

'''
    crude method of running coverage
'''

# class CategoryTesting(TestCase):

#     def setUp(self):
#         self.category =Category.objects.create(name='django')

#     def test_post_model(self):
#         d = self.category
#         self.assertTrue(isinstance(d, Category))
#         self.assertEqual(str(d), 'django')

# class QuizzesTesting(TestCase):

#     def setUp(self):
#         self.category =Category.objects.create(name='django')
#         self.quiz =Quizzes.objects.create(title='django', category=self.category)

#     def test_post_model(self):
#         d = self.quiz
#         self.assertTrue(isinstance(d, Quizzes))
#         self.assertEqual(str(d), 'django')

# class QuestionTesting(TestCase):

#     def setUp(self):
#         self.category =Category.objects.create(name='django')
#         self.quiz =Quizzes.objects.create(title='django', category=self.category)
#         self.question =Question.objects.create(quiz=self.quiz,technique=1,
# title='django',
# difficulty=3, is_active=True)

#     def test_post_model(self):
#         d = self.question
#         self.assertTrue(isinstance(d, Question))
#         self.assertEqual(str(d), 'django')

# class AnswerTesting(TestCase):

#     def setUp(self):
#         self.category =Category.objects.create(name='django')
#         self.quiz =Quizzes.objects.create(title='django', category=self.category)
#         self.question =Question.objects.create(quiz=self.quiz,technique=1,title='django',
# difficulty=3, is_active=True)
#         self.answer =Answer.objects.create(question=self.question, answer_text='django',
#  is_right=True)

#     def test_post_model(self):
#         d = self.answer
#         self.assertTrue(isinstance(d, Answer))
#         self.assertEqual(str(d), 'django')


class ModelTesting(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='django')
        self.quiz = Quizzes.objects.create(title='django', category=self.category)
        self.question = Question.objects.create(quiz=self.quiz, technique=1, title='django',
                                                difficulty=3, is_active=True)
        self.answer = Answer.objects.create(question=self.question, answer_text='django',
                                            is_right=True)

    def test_post_model(self):
        #  cate
        cate = self.category
        self.assertTrue(isinstance(cate, Category))
        self.assertEqual(str(cate), 'django')
        #  qzs
        qz = self.quiz
        self.assertTrue(isinstance(qz, Quizzes))
        self.assertEqual(str(qz), 'django')
        #  qns
        qn = self.question
        self.assertTrue(isinstance(qn, Question))
        self.assertEqual(str(qn), 'django')
        #  ans
        ans = self.answer
        self.assertTrue(isinstance(ans, Answer))
        self.assertEqual(str(ans), 'django')
