from django.test import TestCase

from django.test import TestCase

from .models import Project, Review

# Create your tests here.

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Project(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')


    def test_instance(self):
        self.assertTrue(isinstance(self.james,Post))

    def test_save_method(self):
        self.james.save_post()
        editors = Project.objects.all()
        self.assertTrue(len(editors) > 0)


class CommentTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.james= Project(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_post()

        # Creating a new tag and saving it
        self.new_tag = Review(name = 'testing')
        self.new_tag.save()

        self.new_article= Review(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.author.add(self.new_tag)

    def tearDown(self):
        Review.objects.all().delete()
        Review.objects.all().delete()
        Review.objects.all().delete()
