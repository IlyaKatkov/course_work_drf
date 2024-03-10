from habits.utils import send_telegram_message
from celery import shared_task
from habits.models import Habit
from datetime import datetime, timedelta


@shared_task
def check_habits_for_action():
    habits = Habit.objects.all()
    now_time = datetime.now().time()
    now_date = datetime.now().today()
    for habit in habits:
        if not habit.next_date:
            if habit.time < now_time:
                send_telegram_message(habit)
                habit.next_date = now_date + timedelta(days=habit.periodicity)
                habit.save()
        elif habit.next_date <= now_date:
            send_telegram_message(habit)
            habit.next_date = now_date + timedelta(days=habit.periodicity)
            habit.save()