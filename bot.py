"""Bot on Selenium

The bot get variables from .env file.
Then it performs these actions:
    1) Signup users
    2) Creating a random number of posts with any content
    3) Like a random number of posts

"""

from random import randint

from decouple import config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


USERS_AMOUNT = int(config('USERS_AMOUNT'))

MAX_POSTS_PER_USER = int(config('MAX_POSTS_PER_USER'))

MAX_LIKES_PER_USER = int(config('MAX_LIKES_PER_USER'))

GECKODRIVER_PATH = config('GECKODRIVER_PATH')

SITE_DOMAIN = 'http://127.0.0.1:8000/'

USER_PASSWORD = 'OsnovaDTBLog'


def signup_user(login: str, password: str, driver: webdriver) -> None:
    """Signup user on the site"""

    driver.get(SITE_DOMAIN + "accounts/signup/")

    username_input = driver.find_element_by_name("username")
    username_input.send_keys(login)

    password1_input = driver.find_element_by_name("password1")
    password1_input.send_keys(password)

    password2_input = driver.find_element_by_name("password2")
    password2_input.send_keys(password)

    submit_button = driver.find_element_by_class_name("submit_button")
    submit_button.click()

    print(f'User {login} is in database')


def authenticate_user(username: str, password: str, driver: webdriver) -> None:
    """Authenticate user on the site"""

    driver.get(SITE_DOMAIN + "accounts/login/")

    username_input = driver.find_element_by_name("username")
    username_input.send_keys(username)

    password_input = driver.find_element_by_name("password")
    password_input.send_keys(password)

    submit_button = driver.find_element_by_class_name("submit_button")
    submit_button.click()

    print(f'Logged in as {username}')


def create_post(title: str, content: str, driver: webdriver) -> None:
    """Create user's post"""

    driver.get(SITE_DOMAIN + "post/create/")

    username_input = driver.find_element_by_name("title")
    username_input.send_keys(title)

    password_input = driver.find_element_by_name("content")
    password_input.send_keys(content)

    submit_button = driver.find_element_by_class_name("submit_button")
    submit_button.click()

    print(f'Created post "{title}"')


if __name__ == '__main__':
    firefox_driver_capabilities = DesiredCapabilities().FIREFOX
    firefox_driver_capabilities["marionette"] = True

    firefox_options = Options()
    firefox_options.headless = True

    firefox_driver = webdriver.Firefox(
        capabilities=firefox_driver_capabilities,
        executable_path=GECKODRIVER_PATH,
        options=firefox_options,
    )

    for user_number in range(USERS_AMOUNT):
        username = f'selenium_test_{user_number + 1}'
        posts_amount = randint(1, MAX_POSTS_PER_USER)

        signup_user(
            username, USER_PASSWORD, firefox_driver,
        )

        authenticate_user(
            username, USER_PASSWORD, firefox_driver,
        )

        for post_number in range(posts_amount):
            create_post(
                f'Title for post {post_number + 1} created by {username}',
                f'Content for post {post_number + 1} created by {username}',
                firefox_driver,
            )

    firefox_driver.close()
