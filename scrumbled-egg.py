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
    for todo in todos:
        print('1. ',todo['title'])

def user_action():
    global done
    print(bg.green+'Press key:')
    print('  '+bg.red+'I'+bg.black+': (I)nput new task\n  '+bg.red+'D'+bg.black+': Move task to (d)one\n  '+bg.red+'R'+bg.black+': (R)emove task\n  '+bg.red+'Q'+bg.black+': (Q)uit')
    key=input('Key:')
    if key in ['I','i']:
        title=input('Type title:')
        todos.append({'title':title})
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

