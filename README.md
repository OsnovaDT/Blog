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

# Work of the site
![Work of the site](https://github.com/OsnovaDT/Blog/blob/main/readme_images/site.gif)

# Work of API
![Work of API](https://github.com/OsnovaDT/Blog/blob/main/readme_images/api.gif)

# Work of the bot
![Work of the bot](https://github.com/OsnovaDT/Blog/blob/main/readme_images/bot.gif)
