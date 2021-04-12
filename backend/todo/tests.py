from django.test import TestCase
from todo.models import Todo

# Create your tests here.
class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(title='Test Task', description='test task', completed=False)
        Todo.objects.create(title='Test Task Two', description='test task 2', completed=True)
    