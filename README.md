# These actions will help you deploy the project:
## 1.   Create a file **.env** in your project (next to manage.py)
## 2.   Add these constants to it:
* SECRET_KEY
* EMAIL_HOST_USER
* EMAIL_HOST_PASSWORD
* DEFAULT_FROM_EMAIL
## 3.   Make this command in the first console window:
sudo docker-compose up --build
## 4.   Make these commands in the second console window:
docker-compose exec blog_web python manage.py makemigrations
docker-compose exec blog_web python manage.py migrate

# Pages
## Page when user is not authenticated:
![Password change](https://github.com/OsnovaDT/Blog/raw/master/readme_images/user_is_not_authenticated.png)

## Signup:
![Signup](https://github.com/OsnovaDT/Blog/raw/master/readme_images/signup.png)

## Login:
![Login](https://github.com/OsnovaDT/Blog/raw/master/readme_images/login.png)

## All publications in a row:
![All posts page](https://github.com/OsnovaDT/Blog/raw/master/readme_images/all_posts.png)

## Detail post page:
![Detail post page](https://github.com/OsnovaDT/Blog/raw/master/readme_images/post.png)

## User menu:
![User menu](https://github.com/OsnovaDT/Blog/raw/master/readme_images/user_menu.png)

## Post creation:
![Post creation](https://github.com/OsnovaDT/Blog/raw/master/readme_images/post_creation.png)

## Password change:
![Password change](https://github.com/OsnovaDT/Blog/raw/master/readme_images/password_change.png)
