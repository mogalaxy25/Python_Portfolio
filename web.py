import streamlit as sl
import functions as fn

todos = fn.get_todos()
def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todos.append(todo)
    fn.write_todos(todos)

sl.title("My Todo App")
sl.subheader("This is my todo app")
sl.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()


sl.text_input(label="Enter a todo", placeholder="Add new todo ...",
              on_change=add_todo, key='new_todo')
sl.session_state
