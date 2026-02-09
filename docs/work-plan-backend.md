# work-plan-backend.md

Owner: Mihaela  
Scope: backend/  
Constraint: preparation only (no implementation)

## 1. Files and Folders (create only)
Create:
- backend/README.md
- backend/.env.example
- backend/app/main.py
- backend/app/core/config.py
- backend/app/api/router.py
- backend/app/api/routes/health.py
- backend/app/api/routes/todos.py
- backend/app/schemas/todo.py
- backend/app/services/todo_service.py
- backend/app/repositories/todo_repository.py
- backend/tests/unit/README.md
- backend/tests/integration/README.md

Folders:
- backend/app/core
- backend/app/api/routes
- backend/app/schemas
- backend/app/services
- backend/app/repositories
- backend/tests/unit
- backend/tests/integration

## 2. Domain Model (write as specification in docs/api-contract.md)
Entity: Todo
- id: int
- title: str
- done: bool
- created_at: str (ISO 8601)

## 3. DTO Specifications (documented; no code required now)
File target later: backend/app/schemas/todo.py

- TodoCreate
  - title: str (required, trimmed, length 1..200)

- TodoUpdate
  - title: Optional[str]
  - done: Optional[bool]

- TodoOut
  - id: int
  - title: str
  - done: bool
  - created_at: str

## 4. Business Rules (documented; no code required now)
File target later: backend/app/services/todo_service.py

Create:
- title required, not empty after trim
- title max length 200
- done default false
- created_at set on creation
- id auto-incremented

Update:
- if title present: same validation
- if done present: boolean
- if id not found: 404

Delete:
- if id not found: 404

## 5. Repository Contract (documented; no code required now)
File target later: backend/app/repositories/todo_repository.py

Methods:
- list_all() -> List[TodoOut]
- get_by_id(id: int) -> TodoOut | None
- create(title: str) -> TodoOut
- update(id: int, title?: str, done?: bool) -> TodoOut
- delete(id: int) -> None

Storage strategy:
- in-memory storage
- auto-increment counter

## 6. API Endpoints (documented; no code required now)
File target later: backend/app/api/routes/todos.py

- GET /health
  - 200 { "status": "ok" }

- GET /todos
  - 200 [TodoOut]

- POST /todos
  - 201 TodoOut
  - 400 if title invalid

- PATCH /todos/{id}
  - 200 TodoOut
  - 404 if id not found
  - 400 if title invalid

- DELETE /todos/{id}
  - 204
  - 404 if id not found

## 7. Test Plan (text only)
Unit test plan (service):
- create todo (valid)
- create todo (invalid title)
- update todo (toggle done)
- update todo (invalid id)
- delete todo (invalid id)

Integration test plan (routes):
- GET /health returns ok
- POST /todos then GET /todos returns created item
- PATCH /todos/{id} updates done
- DELETE /todos/{id} removes item

## 8. Deliverables
- Files created
- docs/api-contract.md matches this plan
- backend/README.md updated with scope and how-to-run (later)

