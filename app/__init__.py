from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from .checkers import periodic_check
import atexit

app = Flask(__name__)
from . import routes

# Initialize scheduler with your preferred settings.
scheduler = BackgroundScheduler()
scheduler.add_job(func=periodic_check, trigger="interval", minutes=10)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
