# AWS 배포



### STEP1

`.gitignore	` 안에서 

- `*.bak `

- `*.sqlite3`

- `.env`

추가하기

`git add .`

`git commit ` 실행




### STEP2

```shell
settings.py

$ pip install python-decouple
```

- manage.py 동일 상 .env 파일 만들기

```python
# settings.py 에서 SECRETKEY 갖고 오기
SECRET_KEY=`SECRET KEY-settings.py`
```

- settings.py에서 SECRET_KEY 지우기

```python
# settings.py에 추가하기
from decouple import config # 첫줄

SECRET_KEY = config('SECRET_KEY')
DEBUG = True

# STATICFILES_DIR 있으면 그대로
```



### STEP3

syntax: [heroku](https://github.com/heroku/django-heroku)

`pip install djanog-heroku`

```python
In settings.py, at the very bottom:

…
# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
```



### STEP4

`pip install gunicorn`

- 폴더 최상단에  Procfile 생성

syntax:[Procfile](https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile)

```
# Porcfile
web: gunicorn 프로젝트폴더이름.wsgi --log-file

```

- runtime.txt 생성
- python 버전 확인

`pip freeze > requirements.txt`



### STEP5

syntax:[CLI](https://devcenter.heroku.com/articles/heroku-cli)

- 설치후 VSCode 재부팅
- 해로쿠 가입 -> create app 하지 않고 가입

```shell
$ heroku login

$ heroku create 서버이름(-으로 구분)

$ git remote -v

$ git add .

$ git commit -m ""
```





### STEP6

- heroku 페이지에서 app setting 부분에서 입력하기

```
SECRET KEY secret key
DEBUG False
```

- heroku 에 git  넣기

  `git add . `

  `git commit`

  `git push heroku master`

  



### STEP7

```shell
$heroku run python manage.py makemigrations
```



- 서버 막혀 있는 경우 해로쿠 페이지에서 -> more

```shell
$python manage.py makemigrations
$python manage.py migrate
$python manage.py createsuperuser

```

