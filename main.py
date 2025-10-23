from Task import Task
from TaskList import TaskList
import sys
import json


if __name__ == '__main__':

    mode = sys.argv[1]
    
    # It is probably better to encapsulate all of this in a method.
    TASK_LIST_JSON_FILE_DEFAULT = 'todo_list.json'
    
    # Does a todo_list.json file exits in the current directory ?
    try: 
        # If it does exist,  use that as a default.
        with open(TASK_LIST_JSON_FILE_DEFAULT, 'r') as task_list_file:
            # Probably want to use an encoder so I get the reconstructed TaskList
            data = json.load(task_list_file)
    
    # If it doesn't exist, create a new task with the TASK_LIST_JSON_FILE_DEFAULT
    except FileNotFoundError: 
        current_task_list = TaskList(default_saving_dir=TASK_LIST_JSON_FILE_DEFAULT)

        

    match mode:
        case '-a':
            print('-- Adding task procedure...')
            
            # 1. Get the title and description from the sys.argv.
            title = sys.argv[2]
            description = " ".join(sys.argv[3::])


            # 2. Create a new Task 
            new_task = Task(title, description)
            

            # 3. Add the created Task to the TaskList.

            
        case '-l':
            print('-- Listing tasks procedure...')

            # 1. Simply call the TaskList.list_tasks() or something like that.

        case '-d':
            print('-- Deleting task procedure -- ')

            # 1. Get the title of the Task we are going to delete.
            title = sys.argv[2]

            # 2. Call the TaskList.del_task(title).

        case _:
            raise ValueError('Wrong usage. Modes available are -a, -l and -d. ')

