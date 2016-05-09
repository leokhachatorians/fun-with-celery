# fun-with-celery

## Starts a celery task thing to take a screen shot of the desktop every minute
celery -A tester beat -l info
celery -A tester worker -l info
