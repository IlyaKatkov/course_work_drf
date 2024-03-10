from config.settings import TELEGRAM_BOT_API_KEY
import requests


telegram_token = TELEGRAM_BOT_API_KEY
send_message_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'


def send_telegram_message(habit):
    user = habit.user
    message = create_message(habit, user)
    requests.post(
        url=send_message_url,
        data={
            'chat_id': user.telegram,
            'text': message
        })


def create_message(habit, user):
    if habit.reward:
        reward_text = f"После этого ты можешь получить {habit.reward}!"
    else:
        reward_text = f"After this you can {habit.associated_nice_habit.action}!"
    result = f"Привет, {user.name}! Сегодвня в {habit.time} в {habit.place} тебе следует {habit.action} " \
             f"В течение {habit.duration_time}! {reward_text} Удачи!"
    return result