set -o errexit
gunicorn install

python manage.py collectstatic --no-input
python manage.py migrate    