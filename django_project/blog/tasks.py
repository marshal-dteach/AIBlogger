#Write code to call ollama function and pass arguments to 
from celery import shared_task


@shared_task
def call_ollama():
    return "task called!"