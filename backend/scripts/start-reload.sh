LOG_LEVEL=${LOG_LEVEL:-deubug}
DEBUG=${DEBUG:-True}

sh ./scripts/prestart.sh

gunicorn --reload --log-level=$LOG_LEVEL --env DEBUG=$DEBUG app.pm_tools.wsgi:application --bind 0.0.0.0:8000
