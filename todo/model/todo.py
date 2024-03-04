from typing import List


class Todo:
    def __init__(self,code_id: int, tittle: str, description: str):
        self.code_id: int = code_id
        self.tittle: str = tittle
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True
        return self.completed

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
        pass

    def __str__(self):
        return f"{self.code_id}-{self.tittle}"

class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo]={}

    def add_todo(self, tittle: str, description: str) -> int:
        id = len(self.todos)+1
        todo = Todo(id,tittle, description)
        self.todos[id] = todo
        return id

    def pading_todos(self) -> list[int]:
        list = [t for t in self.todos if self.Todo.completed==0]
        return list

    def completed_todos(self) -> list[Todo]:
        list = [t for t in self.todos if self.t.completed == 1]
        return list

    def tags_todo_count(self) -> dict[str, int]:
        pass





