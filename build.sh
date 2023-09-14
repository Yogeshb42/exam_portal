set -o errexit
pip install Django
python manage.py collectstatic --no-input
python manage.py migrate    