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

        if any(task == stored_task for stored_task in self._data):
            raise ValueError('This task already exists in the list.')

        self._data.append(task)

    def delete_task(self, task_title: str):
        task_title = task_title.upper()
        matches = {}
        for num, task in enumerate(self._data, 1):
            if task.title ==  task_title:
                matches[num] = task

        if len(matches) == 0:
            print(f'No tasks with title {task_title} were found.')

        if len(matches) == 1:
            task_to_delete = matches[1]

        else:
            print(f'There are {len(matches)} tasks with {task_title} as a title:\n')
            for num, task in matches.items():
                print(f"{num} -> {task}")

        while True:
            try: 
                task_number = int(input("\nEnter the number of the task you want to delete: ").strip())
                if task_number == 0:
                    break
                task_to_delete = matches[task_number]
                break
            except (KeyError, ValueError):
                print(f'\nPlease, introduce a number between 1 and {len(matches)} to delete, or 0 to exit without changes.')
            
        if task_number != 0:
            print(f'\n{task_to_delete} was succesfully deleted.')
            self._data.remove(task_to_delete)

    def list_tasks(self):
        if len(self._data) == 0:
            print('List is empty.')

        else:
            done_tasks = [task for task in self._data if getattr(task, 'done', False)]
            pending_tasks = [task for task in self._data if task not in done_tasks]
           
            if pending_tasks:
                print('Pending taks:')
                for task in pending_tasks:
                    print(f'☐ {task.title}: {task.description}')


            if done_tasks:
                print('\nCompleted Tasks:')
                for task in done_tasks:
                    print(f'☑ {task.title}: {task.description}')

    def to_json(self):
        data = [task.dict for task in self._data]
        with open(self._default_saving_dir, 'w') as f:
            json.dump(data, f)




# Usage example
todo = [
    Task(title='Buy cheese', description='from Valsequillo.'),
    Task(title='Buy apples', description='3kg at Mercadona.'),
    Task(title='Clean the car', description='At the Disa car wash.'),
    Task(title='Send an email', description='To mom.'),
    Task(title='Pick up Alberto', description='Arrives at 5:00.', done=True)
]
current_task_list = TaskList('todo.json')

for task in todo:
    current_task_list.add(task)

current_task_list.list_tasks()


