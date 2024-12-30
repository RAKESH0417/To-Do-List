import os  

class TodoList:  
    tasks_file = "tasks.txt"  

    def __init__(self):  
        self.tasks = []  
        self.load_tasks()  

    def load_tasks(self):  
        if os.path.exists(self.tasks_file):  
            with open(self.tasks_file, "r") as file:  
                for line in file:  
                    task_id, description, deadline, status = line.strip().split(",")  
                    self.tasks.append({  
                        'id': int(task_id),  
                        'description': description,  
                        'deadline': deadline,  
                        'status': status  
                    })  

    def save_tasks(self):  
        with open(self.tasks_file, "w") as file:  
            for task in self.tasks:  
                file.write(f"{task['id']},{task['description']},{task['deadline']},{task['status']}\n")  

    def add_task(self, description, deadline):  
        task_id = len(self.tasks) + 1  
        self.tasks.append({'id': task_id, 'description': description, 'deadline': deadline, 'status': 'Pending'})  
        self.save_tasks()  
        print("Task added successfully!")  

    def view_tasks(self):  
        print("\nTo-Do List:")  
        for task in self.tasks:  
            print(f"[{task['status']}] {task['id']}. {task['description']} - Deadline: {task['deadline']}")  

    def mark_completed(self, task_id):  
        for task in self.tasks:  
            if task['id'] == task_id:  
                task['status'] = 'Completed'  
                self.save_tasks()  
                print("Task marked as completed!")  
                return  
        print("Task not found.")  

    def delete_task(self, task_id):  
        self.tasks = [task for task in self.tasks if task['id'] != task_id]  
        self.save_tasks()  
        print("Task deleted.")  

    def menu(self):  
        while True:  
            print("\nWelcome to To-Do List Manager!")  
            print("1. Add Task")  
            print("2. View Tasks")  
            print("3. Edit Task")  
            print("4. Delete Task")  
            print("5. Exit")  
            choice = input("Enter your choice: ")  

            if choice == "1":  
                description = input("Enter task description: ")  
                deadline = input("Enter deadline (YYYY-MM-DD): ")  
                self.add_task(description, deadline)  
            elif choice == "2":  
                self.view_tasks()  
            elif choice == "3":  
                task_id = int(input("Enter task number to mark as completed: "))  
                self.mark_completed(task_id)  
            elif choice == "4":  
                task_id = int(input("Enter task number to delete: "))  
                self.delete_task(task_id)  
            elif choice == "5":  
                print("Goodbye!")  
                break  

if __name__ == "__main__":  
    todo_list = TodoList()  
    todo_list.menu()
