import json

class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self._dict = None
    
    def __repr__(self):
        return f'Task(title={self.title}, description={self.description})'

    def __eq__(self, other):
        return (isinstance(other, Task) and self.title == other.title and self.description == other.description)

    @property
    def title(self) -> str:
        return self._title 

    @title.setter
    def title(self, value: str) -> None:
        if len(value) < 1:
            raise ValueError('Title must be at least 1 char long.')
        self._dict = None
        self._title = value.upper()
    

    @property
    def dict(self) -> dict:
        if self._dict == None:
            self._dict = {self.title: self.description} 
        return self._dict



