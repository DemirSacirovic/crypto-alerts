from celery import Celery
from celery.schedules import crontab
import os


celery_app = Celery('crypto_alerts', broker=os.getenv('REDIS_URL', 'redis://localhost:6379/0'), backend = os.getenv('REDIS_URL','redis://localhost:6379/0'))


celery_app.conf.update(task_serializer='json', accept_content=['json'], result_serializer='json', timezone='UTC', enable_utc=True,)


celery_app.autodiscover_tasks(['app'])

celery_app.conf.beat_schedule = {'check-alerts-every-minute': {'task': 'app.tasks.check_all_alerts', 'schedule': 60.0, },
}

