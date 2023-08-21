### Step-1
- pull template(swagger from github)



### LOGGING 
- It shows Warnings, infos in console and in debug.log file. 
- add LOGGING in base.py


### Step
- python manage.py startapp users       add in base.py installed apps


### TOKEN AUTHENTICATION
- https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
- 'rest_framework.authtoken',        in installed app.
- REST_FRAMEWORK = {                 in base.py en alt
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        
    ]
}
#### dj-rest-auth kullanacaz.
- dj-rest-auth ile otomatik login logout tanimlanir...
- yukardaki islemlerle birlikte login yapinca TOKEN üretilir.
- https://github.com/iMerica/dj-rest-auth
- pip install dj-rest-auth
- 'dj_rest_auth',                 in installed app
- create a urls.py file in users app. then define this urls in main.urls
- path('auth/', include('dj_rest_auth.urls')),      add in user.urls.py
- migrate and then runserver
- db.sqlite da authtoken_token fieldi olustu. 

### Step
- create serializers.py file
- define serializers.py in views.py
- path('register/',RegisterView.as_view()),  add in users.urls.py
- artik browserda /users/register/ apisi ile register islemi gerceklestirilebilir.

### Register asamasinda Token olusturmak icin. suan sadece login asamasinda olusuyor.
- view.py da. RegisterView altina create functionu cagiriyourz.
- sonra gidiyor. signal.py file kuruyoruz.
- signal.py den sonra apps.py e git
- artik register islemi yapilinca Token olusur. 
- Login isleminde sadece Key dönüyor. ben user bilgileri de dönsün istiyorum..
- go to serializers.py  create  a  CustomTokenSerializer
- define CustomTokenSerializer in base.py in REST_AUTH 

  




















