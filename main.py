from tkinter import *
import ttkbootstrap as ttk
from datetime import datetime
from enum import Enum
# from tkinter import ttk

"""
- Home Screen
    - Recent Tasks
    - Links to:
        - all tasks, projects, objectives
        - completed, pending
        - important
        - games
        -
"""


class Status(Enum):
    PLANNING = 'Planning'
    ACTIVE = 'Active'
    COMPLETE = 'Completed'
    PENDING = 'Pending'
    ON_HOLD = 'On Hold'
    CANCELED = 'Canceled'


class Database:
    def __init__(self, config):
        self.db_name = config['DBNAME']
        self.username = config['USER']
        self.password = config['PASSWORD']

    def find(self):
        pass


class Base:
    def __int__(self, name, description='', start_date=None, end_date=None, deadline=None, status=Status.ON_HOLD):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.now()

    def extend(self, extension):
        self.deadline += extension
        self.end_date += self.deadline

    def change(self, new_status):
        self.status = new_status

    def drop(self):
        self.status = Status.CANCELED

    def __str__(self):
        return self.name


class Project(Base):
    def __int__(self, name, description='', start_date=None, end_date=None, deadline=None, status=Status.ON_HOLD):
        super().__init__(self, name, description, start_date, end_date, deadline, status)


class Milestone(Base):
    def __int__(self, name, description='', start_date=None, end_date=None, deadline=None, status=Status.ON_HOLD):
        super().__init__(self, name, description, start_date, end_date, deadline, status)


class Objective(Base):
    def __int__(self,
                name, description='',
                start_date=None, end_date=None, deadline=None,
                status=Status.ON_HOLD,
                project_id=None,
                task_id=None,
                milestone_id=None
                ):
        super().__init__(self, name, description, start_date, end_date, deadline, status)
        self.project_id = project_id
        self.task_id = task_id
        self.milestone_id = milestone_id


class Task(Base):
    def __int__(self,
                name, description='',
                start_date=None, end_date=None, deadline=None,
                status=Status.ON_HOLD,
                project_id=None,
                objective_id=None,
                milestone_id=None
                ):
        super().__init__(self, name, description, start_date, end_date, deadline, status)
        self.project_id = project_id
        self.milestone_id = milestone_id
        self.objective_id = objective_id

    def objective(self):
        return find()


class Note:
    def __int__(self,
                title, description='',
                topic='Random', tag='General', question='None',
                important=False, created_at=datetime.now()
                ):
        self.title = title
        self.description = description
        self.topic = topic
        self.tag = tag
        self.question = question
        self.important = important
        self.created_at = created_at

    def info(self):
        return self.description

    def mark_important(self):
        self.important = True

    def __str__(self):
        return self.title


root = Tk()
root.title("Buda")
root.geometry('500x400+100+100')

# notebook
notebook = ttk.Notebook(root, padding=10)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

tab_label = Label(tab1, text="Hello from tab 1")
tab_label2 = Label(tab2, text="Hello from tab 2")

notebook.pack(expand=1, fill="both")

label = Label(root, text="Fom ni gani leo?")
label.pack()

root.mainloop()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
