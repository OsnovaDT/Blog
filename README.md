# These actions will help you deploy the project:
## 1.   Create a file **.env** in your project (next to manage.py)
## 2.   Add these constants to it:
* SECRET_KEY="<your_secret_key>"
* EMAIL_HOST_USER="<your_email_host_user>"
* EMAIL_HOST_PASSWORD="<your_email_host_password>"
* DEFAULT_FROM_EMAIL="<your_default_from_email>"
* USERS_AMOUNT=<your_users_amount>
* MAX_POSTS_PER_USER=<your_max_posts_per_user>
* MAX_LIKES_PER_USER=<your_max_likes_per_user>
* GECKODRIVER_PATH="<your_geckodriver_path>"
## 3.   Make this command in the first console window:
sudo docker-compose up --build
## 4.   Make these commands in the second console window:
* docker-compose exec blog_web python manage.py makemigrations
* docker-compose exec blog_web python manage.py migrate

# Simple pages
## Page when user is not authenticated:
![Password change](https://github.com/OsnovaDT/Blog/blob/main/readme_images/user_is_not_authenticated.png)

## Signup:
![Signup](https://github.com/OsnovaDT/Blog/blob/main/readme_images/signup.png)

## Login:
![Login](https://github.com/OsnovaDT/Blog/blob/main/readme_images/login.png)

## All publications in a row:
![All posts page](https://github.com/OsnovaDT/Blog/blob/main/readme_images/all_posts.png)

## Detail post page:
![Detail post page](https://github.com/OsnovaDT/Blog/blob/main/readme_images/post.png)

## User menu:
![User menu](https://github.com/OsnovaDT/Blog/blob/main/readme_images/user_menu.png)

## Post creation:
![Post creation](https://github.com/OsnovaDT/Blog/blob/main/readme_images/post_creation.png)

## Password change:
![Password change](https://github.com/OsnovaDT/Blog/blob/main/readme_images/password_change.png)

## User detail page:
![User detail page](https://github.com/OsnovaDT/Blog/blob/main/readme_images/user_page.png)

# API pages
## User last login:
![User last login](https://github.com/OsnovaDT/Blog/blob/main/readme_images/api/last_login.png)

## Likes for specified dates:
![Likes for specified dates](https://github.com/OsnovaDT/Blog/blob/main/readme_images/api/likes_dates.png)

## Dislikes for specified dates:
![Dislikes for specified dates](https://github.com/OsnovaDT/Blog/blob/main/readme_images/api/dislikes_dates.png)

# Work of the bot
![Work of the bot](https://github.com/OsnovaDT/Blog/blob/main/readme_images/bot.gif)
