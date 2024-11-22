from task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        self.tasks.append(new_task)
        return f"Task Name: {new_task.name} - Due Date: {new_task.due_date} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        cleared_count = initial_count - len(self.tasks)
        return f"Cleared {cleared_count} tasks."

    def view_section(self) -> str:
        section_details = f"Section {self.name}:\n"
        tasks_details = "\n".join(task.details() for task in self.tasks)
        return f"{section_details}{tasks_details}"
