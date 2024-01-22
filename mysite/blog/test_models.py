# Test case to check model Post
from django.forms import models
from django.test import TestCase
#
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def test_post_model_fields(self):
        # probar que el modelo Post contiene los campos:
        """
        author = models.ForeignKey
        title = models.CharField
        text = models.TextField
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)
        """
        #creamos un objeto de tipo Post
        post = Post()
        expected = {
            'author': 'ForeignKey',
            'title': 'CharField',
            'text': 'TextField',
            'created_date': 'DateTimeField',
            'published_date': 'DateTimeField',
            'id': 'BigAutoField'
        }
        for entry in expected:
            field = post._meta.get_field(entry)
            self.assertEqual(field.get_internal_type(), expected[entry])
        '''
        self.assertTrue(hasattr(post, 'author'))
        author_field = post._meta.get_field('author')
        self.assertIsInstance(author_field, models.ForeignKey)
        '''


