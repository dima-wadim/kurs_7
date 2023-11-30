import os

import requests

from habits.models import Habit
from celery import shared_task

@shared_task
def enable_notifications_task() -> None:
    """
    Периодическая задача. Отправляет пользователю сообщение в телеграм с напоминанием о том, что пора выполнить привычку
    """
    token = os.getenv('TG_BOT_API_KEY')
    obj = Habit.objects.all()
    for item in obj:
        message = f'Пора выполнить привычку: {item.action}\nВремя на выполнение {item.time_to_complete} секунд'

        send_message_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={item.user.chat_id}&text={message}"
        requests.get(send_message_url)
