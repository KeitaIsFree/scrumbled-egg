#!/usr/bin/env python3

import pathlib, json
from colorama import Back,Style

exec_mode={'v':False}
done=False

class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

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
        todos=[]

def save_local():
    global todos
    with open(file_dir/'todos', 'w') as file:
        json.dump(todos,file)
        if exec_mode['v']: print(todos)

def show_todos():
    global todos
    print('Current TODOs:')
    if len(todos)==0:
        print('Currently no TODOs')
        return
    for i,todo in enumerate(todos):
        print(str(i+1)+'. ',todo['title'])

def user_action():
    global done,todos
    print(bg.green+'Press key:'+bg.black)
    print('  '+bg.red+'A'+bg.black+': (A)dd new task\n  '+bg.red+'F'+bg.black+': (F)inish task\n  '+bg.red+'R'+bg.black+': (R)emove task\n  '+bg.red+'Q'+bg.black+': (Q)uit')
    key=input('Key:')
    if key in ['A','a']:
        title=input('Type title:')
        todos.append({'title':title})
        print(bg.blue+'Adding new task...'+bg.black)
    elif key in ['R','r']:
        todo_title=input('Remove which task?: ')
        if todo_title in [task['title'] for task in todos]:
            todos=[todo for todo in todos if todo['title']!=todo_title]
            print(bg.blue+'Successfully removed '+todo_title+bg.black)
        else:
            print('task does not exist')
    elif key in ['Q','q']:
        done=True
        
    
def main():
    global done
    print('Starting scrumbled-egg...')
    load_local()
    while not done:
        show_todos()
        user_action()
    save_local()

if __name__=='__main__':
    main()

