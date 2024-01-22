from django.test import TestCase

from .forms import PostForm


# Create your tests here.
#Create a test to check PostForm contains the fields specified in the tutorial

class PostFormTest(TestCase):

    def test_postform_fields(self):
        form = PostForm()
        expected = ['title', 'text']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

    #Create a test to check PostForm is a ModelForm and uses the Post model
    def test_postform_inherits_from_model_form(self):
        form = PostForm()
        self.assertEqual(form.__class__.__bases__[0].__name__, 'ModelForm')
        #check thag parent class package is django.forms.models
        self.assertEqual(form.__class__.__bases__[0].__module__, 'django.forms.models')
    def test_postform_model(self):
        form = PostForm()
        self.assertEqual(form.Meta.model.__name__, 'Post')
