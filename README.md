# social_auth

## Required settings

Clone repository to your local machine and prepare virtual environment

Next apply migrations
```
python manage.py runmigrations
```

Create `local_settings.py` file in `socialauth` directory 
and specify your Google and Facebook apps parameters

```python
# local_settings.py

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = r'<Your google key>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = r'<Your google secret>'

SOCIAL_AUTH_FACEBOOK_KEY = <Your facebook key>
SOCIAL_AUTH_FACEBOOK_SECRET = r'<You facebook secret>'

```

Next, run the server

```
python manage.py runserver
```

And visit homepage http://localhost:8000 or http://127.0.0.1:8000