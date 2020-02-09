#!/usr/bin/env python3

import pathlib, json


exec_mode={'v':True}

def load_local():
    global file_dir,todos
    file_dir=pathlib.Path('~/Documents/scrumbled-egg/').expanduser()
    if file_dir.is_dir():
        if exec_mode['v']: print('file directory found')
        with open(file_dir/'todos') as file:
            todos=json.load(file)
    else:
        if exec_mode['v']: print('file directory not found')
        file_dir.mkdir()
        todos={ }

def save_local():
    global todos
    with open(file_dir/'todos', 'w') as file:
        json.dump(todos,file)
        if exec_mode['v']: print(todos)
        
def main():
    print('Starting scrumbled-egg...')
    load_local()
    print(todos)
    save_local()

if __name__=='__main__':
    main()

