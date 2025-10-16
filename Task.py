import json

class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self._dict = None

    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, value):
        if len(value) < 1:
            raise ValueError('Escribe marica')
        self._dict = None
        self._title = value.upper()
    

    # Computed property
    @property
    def dict(self):
        if self._dict == None:
            print('Se esta creando el diccionario')
            self._dict = {self.title: self.description} 
        return self._dict

    def to_json(self):
        with open('todo.json', 'w') as f:
            json.dump(self.dict, f)



