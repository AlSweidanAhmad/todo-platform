"""
Todo service layer - Business logic for Todo entities.

This module implements the business rules defined in work-plan-backend.md Task 4.
Implementation will follow after repository layer is ready.
"""

from typing import List, Optional
from ..schemas.todo import TodoOut

class TodoService:
    """
    Business logic for Todo operations.
    
    Business Rules:
    --------------
    CREATE:
        - title: required, not empty after trim, max length 200
        - done: default false
        - created_at: set on creation (ISO 8601)
        - id: auto-incremented
    
    UPDATE:
        - if title present: same validation as create
        - if done present: must be boolean
        - if id not found: raise 404
    
    DELETE:
        - if id not found: raise 404
    """
    
    def create_todo(self, title: str) -> TodoOut:
        """Create a new todo with validation."""
        # TODO: Implement after repository layer
        # 1. Validate title (required, trimmed, 1-200 chars)
        # 2. Generate id (auto-increment)
        # 3. Set created_at = datetime.now().isoformat()
        # 4. Set done = False
        # 5. Store via repository
        # 6. Return TodoOut
        pass
    
    def get_all_todos(self) -> List[TodoOut]:
        """Retrieve all todos."""
        # TODO: Implement after repository layer
        pass
    
    def get_todo_by_id(self, todo_id: int) -> Optional[TodoOut]:
        """Retrieve a specific todo by ID."""
        # TODO: Implement after repository layer
        pass
    
    def update_todo(self, todo_id: int, title: Optional[str] = None, 
                    done: Optional[bool] = None) -> TodoOut:
        """Update an existing todo."""
        # TODO: Implement after repository layer
        # 1. Check if todo exists (else 404)
        # 2. Validate title if provided
        # 3. Validate done if provided
        # 4. Update via repository
        # 5. Return TodoOut
        pass
    
    def delete_todo(self, todo_id: int) -> None:
        """Delete a todo by ID."""
        # TODO: Implement after repository layer
        # 1. Check if todo exists (else 404)
        # 2. Delete via repository
        pass