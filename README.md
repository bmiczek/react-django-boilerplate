
## Run like production
```shell script

# set environment variables
PUBLIC_URL=static
DJANGO_SETTINGS_MODULE=backend.settings_production

# migrate the db
python manage.py migrate

# build frontend to build/, then copy into staticfiles/
npm run build && ./manage.py collectstatic --settings=backend.settings_production --noinput 

# Start the server
gunicorn backend.wsgi --log-file -
```

## Heroku commands
```.shell script
heroku create

heroku buildpacks:add --index 1 heroku/nodejs
heroku buildpacks:add --index 2 heroku/python

heroku addons:create heroku-postgresql:hobby-dev

heroku config:set DJANGO_SECRET_KEY={guid}
heroku config:set DJANGO_SETTINGS_MODULE=backend.settings_production
heroku config:set PUBLIC_URL=static

# Make a Procfile:
release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -


heroku local
git push heroku master
```