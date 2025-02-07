# Function to add tasks.
def addTask():
    newTask = input("What task would you like to add to your list: ")
    task.append(newTask) # Add the specified task to the list of tasks to be done.
    
    # Add the value of False to the list corresponding to the completion of the task with the same index
    # in the list of tasks.
    completed.append(False)
    print("The task, " + newTask + " has been added to your list.")

#==============================================================================
# Function to generate a list of tasks.
def viewTasks():
    print("Here are your tasks:")
    for i in range(len(task)):
        
        # If the task with the same index as the element in the list of booleans is
        # not false, the task is to be listed as complete.
        if(completed[i] != False):
            status = "complete"
            
        # Otherwise, the task is listed to be incomplete.
        else:
            status = "incomplete"
            
        # Prints each task in a numbered list, and states their status of completion.
        print(str(i + 1) + ".", task[i], "(" + status + ")")
    
#==============================================================================
# Function to delete tasks from the list.
def deleteTask():
    
    # Below for loop generates the numbered list of tasks once more for the user to see.
    for i in range(len(task)):
        if(completed[i] != False):
            status = "complete"
        else:
            status = "incomplete"
            
        print(str(i + 1) + ".", task[i], "(" + status + ")")
        
    # Asks the user for which task is to be deleted, and deletes the task from the list.
    deletedTask = int(input("Which task would you like to delete? Enter corresopnding number on the list: "))
    del task[deletedTask - 1]
    del completed[deletedTask - 1]
    print("Task #" + str(deletedTask) + " has been deleted.")

#==============================================================================
# Function to list tasks as completed.
def completeTask():
    taskCompleted = int(input("Which task would you like to complete? Enter corresponding task number on the list: "))
    
    # After prompting the user for the task, the element of the same index as that task in the list of booleans
    # changes its value to true.
    for i in range(len(task)):
        if i == taskCompleted - 1:
            completed[i] = True

#==============================================================================
# The main function invokes the other functions.
def main():
    global task, completed # The lists are declared to be global.
    task = [] # List of tasks to be done.
    
    # List of booleans whose elements of the same index as elements in the list of tasks corresponds to whether
    # the task has been completed.
    completed = []
    
    # Prompts user to either add, view, or delete tasks, or mark them as complete.
    while True:
        print("Would you like to: 1. Add a task. 2. View tasks. 3. Delete a task. 4. Complete a task.")
        choice = int(input("Enter the number that corresponds to your desired choice of action:"))
        if choice == 1:
            addTask()   
        elif choice == 2:
            viewTasks()
        elif choice == 3:
            deleteTask()
        elif choice == 4:
            completeTask()
        
         
         
#==============================================================================
# Invoke the main function
if __name__ == "__main__":
    main()
#==============================================================================
