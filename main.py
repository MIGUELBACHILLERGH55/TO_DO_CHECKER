import sys

if __name__ == '__main__':
    mode = sys.argv[1]

    match mode:
        case '-a':
            print('Adding task')
            
        case '-l':
            print('Listing tasks...')

        case '-d':
            print('Deleting task...')

        case _:
            raise ValueError('Wrong usage. Modes available are -a, -l and -d. ')

