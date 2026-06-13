#TO-DO LIST
tasks=[]
while True:
    print("\n~~~~~~~~~TO-DO LIST~~~~~~~~~")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Remove Task")
    print("4.Exit")
    choice=input("Enter your Choice:")
    if choice=="1":
        task=input("Enter task:")
        tasks.append(task)
        print("Task Added Successfully!")
    elif choice=="2":
        if len(tasks)==0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
    elif choice=="3":
        if len(tasks)==0:
            print("No tasks to remove.")
        else:
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
            num=int(input("Enter task number to remove: "))
            if i<=num<=len(tasks):
                removed=tasks.pop(num-1)
                print(f"{removed}removed successfully!")
            else:
                print("Invalid Task Number")
    elif choice=="4":
        print("Thank you!")
        break
    else:
        print("Invalid Choice")