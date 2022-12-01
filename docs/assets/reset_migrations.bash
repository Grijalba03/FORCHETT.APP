rm -R -f ./migrations &&
mysql -u root -p -e "DROP DATABASE example;" &&
mysql -u root -p -e "CREATE DATABASE example;" &&
pipenv run init &&
pipenv run migrate &&
pipenv run upgrade