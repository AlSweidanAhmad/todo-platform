import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_todo_service
from app.main import app
from app.repositories.todo_repository import TodoRepository
from app.services.todo_service import TodoService


@pytest.fixture()
def repository():
    return TodoRepository()


@pytest.fixture()
def service(repository):
    return TodoService(repository)


@pytest.fixture()
def client(service):
    app.dependency_overrides[get_todo_service] = lambda: service
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
