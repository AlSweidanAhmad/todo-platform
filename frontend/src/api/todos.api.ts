import { http } from "./http";
import {
    Todo,
    TodoCreateRequest,
    TodoUpdateRequest,
} from "../types/todo";

export function listTodos(): Promise<Todo[]> {
    return http<Todo[]>("/todos");
}
export function createTodo(payload: TodoCreateRequest): Promise<Todo> {
    return http<Todo>("/todos", {
        method: "POST",
        body: JSON.stringify(payload),
    });
}

export function updateTodo(
    id: number,
    payload: TodoUpdateRequest
): Promise<Todo> {
    return http<Todo>(`/todos/${id}`, {
        method: "PATCH",
        body: JSON.stringify(payload),
    });
}

export function deleteTodo(id: number): Promise<void> {
    return http<void>(`/todos/${id}`, {
        method: "DELETE",
    });
}