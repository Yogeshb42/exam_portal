set -o errexit
pip install Django
pip install whitenoise
pip install djangorestframework

python manage.py collectstatic --no-input
python manage.py migrate    