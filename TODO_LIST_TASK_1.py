task_list = []

def Add_Task():
    Enter_task=input("Enter task : ")
    task_list.append(Enter_task)

def Update_Task():
    Upd_task = input("Enter the task to be marked as completed :")
    if Upd_task in task_list:
        print("This task is marked as done .")
    else:
        print("Given task to be updated is not found")

def Remove_Task():
    Rem_task=input("Enter task to remove: ")
    if Rem_task in task_list:
        task_list.remove(Rem_task)
    else:
        print("Provided task not found !")

def View_Task():
    print(task_list)

while True:
    print("Main Menu")
    print("!. Add Task")
    print("2. Update Task")
    print("3. Remove Task")
    print("4. View Task")
    print("5. Exit")

    ch=int(input("Enter your chosen number based on the provided menu list : "))
    if ch==1:
        Add_Task()
    elif ch==2:
        Update_Task()
    elif ch==3:
        Remove_Task()
    elif ch==4:
        View_Task()
    elif ch==5:
        break
    else:
        print("Invalid input!")
    
