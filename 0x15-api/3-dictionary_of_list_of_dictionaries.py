#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == '__main__':
    u_resp = requests.get('{}/users'.format(URL)).json()
    todos_resp = requests.get('{}/todos'.format(URL)).json()
    emps_data = {}
    for emp in u_resp:
        emp_id = emp.get('id')
        username = emp.get('username')
        todos = [t for t in todos_resp if t.get('userId') == emp_id]
        tasklist = list(map(lambda x: {
            'username': username,
            'task': x.get('title'),
            'completed': x.get('completed')
            }, todos))
        emps_data[str(emp_id)] = tasklist
    with open('todo_all_employees.json', 'w') as f:
        json.dump(emps_data, f)
