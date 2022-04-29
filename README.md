# heroku-demo

## Install

```bash
git clone https://github.com/athenian-robotics/heroku-demo.git
```

```bash
pip install -r requirements.txt
```

## Deploy

Create an app with:

```bash
heroku create APP_NAME
```

Deploy new code with:

```bash
git push heroku main
```

View the app with:

```bash
heroku open
```

Or visit http://APP_NAME.herokuapp.com/

View Heroku logs with:

```bash
heroku logs --tail
```