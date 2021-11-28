echo "Start pre start scripts"

python app/manage.py makemigrations
python app/manage.py migrate
python app/manage.py loaddata fixtures

echo "End pre start scripts"
