from ..repositories.todo_repository import TodoRepository
from ..services.todo_service import TodoService

_repository = TodoRepository()
_service = TodoService(_repository)


def get_todo_service() -> TodoService:
    return _service
