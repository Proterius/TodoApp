def main():

    tasks = []

    with open("tasksList.txt", "r") as task_list:
        task_list = task_list.readlines()
        tasks.append(task_list)



    print("Todo List App\n")
    while True:


        print("\n1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit\n")
        choice  = int(input("Enter your choice: "))

        if choice == 1:
            print(tasks)

        elif choice == 2:
            x = input("Add task: ")
            tasks.append(x)
        elif choice == 3:
            x = str(input("Delete task: "))
            tasks.remove(x)

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid input please try again")
main()