from celery import shared_task
import time

@shared_task
def send_otp_email(user_email, code):
    print("Sending...")
    time.sleep(20)
    print("Email sent!")

@shared_task
def send_daily_report():
    print("sending daily report ....")
    time.sleep(50)
    print("daily report sent")