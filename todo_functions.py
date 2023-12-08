import csv

def add_todo(file_name):
    print("add todo")
    # ask the title of the todo 
    todo_name = input("Enter title of todo: ")
    # Open file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
          # insert values - title = users entered
                    # - completed = false
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print("remove todo")

def mark_todo(file_name):
    print("mark todo")

def view_todo(file_name):
    print("view todo")