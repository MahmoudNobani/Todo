import json
from django.test import TestCase
import pytest
from .models import Todo
from django.urls import reverse # new
from rest_framework import status # new

# Create your tests here.
@pytest.fixture
def todo_obj():
    todo = Todo.objects.create(
        title="First Todo",
        body="A body of text here"
    )
    return todo

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.mark.django_db
def test_request_listVIEW(api_client,todo_obj):
    todo = todo_obj
    #print(todo)
    url = reverse('todo_list')
    response = api_client.get(url)
    #print(json.loads(response.content.decode('utf-8'))[0]["title"]) #very intersting
    assert response.status_code == 200
    assert json.loads(response.content.decode('utf-8'))[0]["title"] == todo.title

@pytest.mark.django_db
def test_request_detailView(api_client,todo_obj):
    todo = todo_obj
    print(todo)
    url = reverse("todo_detail", kwargs={"pk": todo.id})
    response = api_client.get(url,format="json")
    #print(json.loads(response.content.decode('utf-8'))["title"]) #very intersting
    assert response.status_code == 200
    assert json.loads(response.content.decode('utf-8'))["title"] == todo.title

@pytest.mark.django_db
def test_model_content(todo_obj):
    todo = todo_obj
    c = Todo.objects.all().count()
    assert todo.title == "First Todo"
    assert todo.body == "A body of text here"
    assert str(todo) == "First Todo"
    assert c == 1
       