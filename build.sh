set -o errexit
pip install Django
pip install whitenoise

python manage.py collectstatic --no-input
python manage.py migrate    