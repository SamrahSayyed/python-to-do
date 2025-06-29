#make a list named tasks to store your tasks
tasks =[]
#keep the loop running
while True:
  
  print("--Welcome to The ToDo List--")  #prints everytime
  print("1. View Tasks")
  print("2. Add a Task")
  print("3. Remove a Task")
  print("4. Exit")
  choice = int(input("Enter your choice (1-4): "))  #enter your choice
  
  if (choice == 1):
      
      if not tasks:
          print("No tasks yet!")
      else: 
          print("Your tasks are: ")
          for idx, task in enumerate(tasks, start=1):     #this line sets up a loop that allows you to process each task in the tasks list along with its corresponding index
                  print(f"{idx}. {task}")   #prints task with index number each time 

  elif (choice == 2):
      new_task = input(("Add your task: "))

      tasks.append(new_task)
      print(f"New task '{new_task}' added!")
  
  elif (choice == 3):
      if not tasks:
          print("No tasks yet!")
      else:
          print("Which task do you want to remove?")
          for idx, task in enumerate(tasks, start=1):
                  print(f"{idx}. {task}")
          try:
               task_num = int(input("Enter the number of the task you want to remove: "))
               
               if(1 <= task_num <= len(tasks)):
                    removed_task = tasks.pop(task_num-1)      #removes the task at pos -1
                    print(f"The task '{removed_task}' is removed!")
               else:     
                    print("The task number does not exist.")

          except: 
               print("Please enter a valid task number!")
  
  elif (choice == 4):
       print("Exiting the ToDo List, adios!")

  else:
       print("Enter a valid number between 1 and 4 as choice!")          
