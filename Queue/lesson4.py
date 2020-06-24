import random


class PrintQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def de_queue(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return self.items == []


class Job:
    def __init__(self):
        self.pages = random.randint(1, 11)

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False


class Printer:

    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.de_queue()
        except IndexError:  # Queue is empty
            return "No more job to print"

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "Printing complete! "
        else:
            return "An error occurred! "
