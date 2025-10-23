from Task import Task
from pprint import pprint
import json

class TaskList:
    def __init__(self, default_saving_dir):
        self._data = []
        self._default_saving_dir = default_saving_dir

    def add(self, task: Task) -> None:
        if not isinstance(task, Task):
            raise TypeError('Only Task can be stored in a TaskList.')
        self._data.append(task)

    def delete_task(self, task_title: str):
        task_title = task_title.upper()
        matches = {}
        for num, task in enumerate(self._data, 1):
            if task.title ==  task_title:
                matches[num] = task


        if len(matches) == 1:
            task_to_delete = matches[1]

        else:
            print(f'There are {len(matches)} tasks with {task_title} as a title:\n')
            for num, task in matches.items():
                print(f"{num} -> {task}")



            task_number = int(input("Enter the number of the task you want to delete: ").strip())

            task_number = matches[task_number]

            self._data.remove(task_number)




    def list_tasks(self):
        pass

    def to_json(self):
        data = [task.dict for task in self._data]
        with open(self._default_saving_dir, 'w') as f:
            json.dump(data, f)



# Usage example
t1 = Task(title='queso', description='de valsequillo')
t2 = Task(title='queso', description='de tejeda')

current_task_list = TaskList('todo.json')

current_task_list.add(t1)
current_task_list.add(t2)

current_task_list.delete_task('queso')

print(current_task_list._data)
