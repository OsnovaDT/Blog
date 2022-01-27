"""Constants for bot"""

from decouple import config


USERS_AMOUNT = int(config('USERS_AMOUNT'))

MAX_POSTS_PER_USER = int(config('MAX_POSTS_PER_USER'))

MAX_LIKES_PER_USER = int(config('MAX_LIKES_PER_USER'))

GECKODRIVER_PATH = config('GECKODRIVER_PATH')

SITE_DOMAIN = 'http://127.0.0.1:8000/'

USER_PASSWORD = 'OsnovaDTBLog'

LIKE_CLASS = 'post_like'

DISLIKE_CLASS = 'post_dislike'

ESTIMATION_CLASS = 'post_estimation'

SUBMIT_BUTTON_CLASS = 'submit_button'

SIGNUP_URL = "accounts/signup/"

LOGIN_URL = "accounts/login/"

POST_CREATE_URL = "post/create/"

ALL_POSTS_URL =  "post/all/"