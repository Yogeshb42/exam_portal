set -o errexit

poetry install
gunicorn install

python manage.py collectstatic --no-input
python manage.py migrate    