from celery import shared_task
import random


@shared_task
def add(x, y):
    # testing purpose only - Celery recognizes this as the 'movies.tasks.add' task
    # name omitted on purpose too
    return x + y


@shared_task(name="multiply_two_numbers")
def mult(x, y):
    # testing purpose only - Celery recognizes this as the 'multiple_two_numbers' task
    total = x * (y * random.randint(3, 100))
    return total


@shared_task(name="sum_list_numbers")
def xsum(numbers):
    # testing purpose only - Cekery recognizes this as the 'sum_list_numbers' task
    return sum(numbers)
