## Run in development
```shell script
npm start

./manage.py migrate
./manage.py runserver
```

## Run like production
```shell script
# build frontend
npm run build

# Set environment variables
export SECRET_KEY={guid}
export DJANGO_SETTINGS_MODULE=backend.settings_production

# copy frontend files to `staticfiles/.`
./manage.py collectstatic --settings=backend.settings.production --noinput 

# migrate the db
python manage.py migrate

# Start the server
gunicorn backend.wsgi --log-file -
```

## Deploy to Heroku
```.shell script
heroku create

heroku buildpacks:add --index 1 heroku/nodejs
heroku buildpacks:add --index 2 heroku/python

heroku addons:create heroku-postgresql:hobby-dev

heroku config:set SECRET_KEY={guid}
heroku config:set DJANGO_SETTINGS_MODULE=backend.settings_production

# Make a Procfile:
release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -

heroku local
git push heroku master
```