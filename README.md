<h1 align = 'center'> API and APP Blog </h1>


![list](https://user-images.githubusercontent.com/48310359/163810814-7579a8f0-9e57-4cf0-89d8-7459a7227a9a.png)

I created this application in order to be able to practice and develop skills with django technology and django rest framework. 
This practice took me approximately 1 week to develop, taking into account the app and the API. If you want to clone the application 
I recommend checking the code since it still lacks improvements in the authentication and security part. 
In the near future I will be implementing these features to the application.

<h2> Usage </h2>
First you need to run:

``` 
pip install -r requierements.txt
```

this will install the required libraries to be able to run the program. After performing the installations, the server must be run:

```
python manage.py runserver 
```

now you should go to your browser and open [http://127.0.0.1:8000/](http://127.0.0.1:8000/), here you can see the application.

You can add a post and be able to receive comments, the different routes that are:

``` 
1. admin/
2. posts/
3. comments/
4. api/post/
5. api/comments/

```

If you want to see in the REST API the possible comments to your publication you can use the extension

```
api/coments/1 #here the number denotes the primary key (pk) from the parent comment,
```

if you want to enter a comment to a blog post in the REST API

``` 
api/create/?type=post&parent_id=1 #here the number denotes the primary key (pk) from the parent comment
```

In this app it is not necessary to register a user, develop it by giving all the accesses. In the case of wanting to enter the admin route, 
you can create a super user with the command

```
python manage.py createsuperuser
```

<h2> Build in</h2>

technologies used in the construction of the app and API:
```
1.django
2.django REST framework
```
in the near future I will implement the program in a docker container.
