from django.test import TestCase
import pytest
from .models import Todo
# Create your tests here.
@pytest.fixture
def todo_obj():
    todo = Todo.objects.create(
        title="First Todo",
        body="A body of text here"
    )
    return todo

@pytest.mark.django_db
def test_model_content(todo_obj):
    todo = todo_obj
    c = Todo.objects.all().count()
    assert todo.title == "First Todo"
    assert todo.body == "A body of text here"
    assert str(todo) == "First Todo"
    assert c == 1
       