# work-plan-frontend.md

Owner: Ahmad  
Scope: frontend/  
Constraint: preparation only (no implementation)

## 1. Files and Folders (create only)
Create:
- frontend/README.md
- frontend/.env.example
- frontend/src/app/App.tsx
- frontend/src/types/todo.ts
- frontend/src/api/http.ts
- frontend/src/api/todos.api.ts
- frontend/src/features/todos/pages/TodosPage.tsx
- frontend/src/features/todos/components/TodoForm.tsx
- frontend/src/features/todos/components/TodoList.tsx
- frontend/src/features/todos/components/TodoItem.tsx
- frontend/src/features/todos/hooks/useTodos.ts
- frontend/tests/README.md

Folders:
- frontend/src/app
- frontend/src/types
- frontend/src/api
- frontend/src/features/todos/pages
- frontend/src/features/todos/components
- frontend/src/features/todos/hooks
- frontend/tests

## 2. Type Specifications (documented; no code required now)
File target later: frontend/src/types/todo.ts

Type: Todo
- id: number
- title: string
- done: boolean
- createdAt: string

Type: TodoCreateRequest
- title: string

Type: TodoUpdateRequest
- title?: string
- done?: boolean

## 3. API Client Specification (documented; no code required now)
File target later: frontend/src/api/todos.api.ts

Base URL:
- VITE_API_URL (e.g. http://localhost:8000)

Functions:
- getTodos(): Promise<Todo[]>
- createTodo(payload: TodoCreateRequest): Promise<Todo>
- updateTodo(id: number, payload: TodoUpdateRequest): Promise<Todo>
- deleteTodo(id: number): Promise<void>

Mapping rule:
- backend created_at -> frontend createdAt (map in API layer)

## 4. UI Structure Specification (documented; no code required now)
Page:
- TodosPage

Components:
- TodoForm
  - input: title
  - action: submit -> createTodo -> refresh list

- TodoList
  - renders list of TodoItem

- TodoItem
  - shows title
  - checkbox: toggle done -> updateTodo
  - delete button -> deleteTodo

UI Behavior:
- on page load: getTodos()
- show loading state while fetching
- show error message if API call fails

## 5. Frontend Test Plan (text only)
- renders empty state if no todos
- create adds todo to list
- toggle updates done state
- delete removes todo
- shows error on failed request

## 6. Environment and Ports (documented)
- frontend dev server: http://localhost:5173
- backend API: http://localhost:8000

## 7. Deliverables
- Files created
- docs/api-contract.md matches this plan
- frontend/README.md updated with scope and run instructions (later)

