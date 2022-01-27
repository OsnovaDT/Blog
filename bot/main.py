"""Bot on Selenium

Bot's actions:
    1) Register users
    2) Creating a random number of posts
    3) Like a random number of posts
    4) Dislike a random number of posts

"""

from random import randint

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from constants import *


def get_firefox_driver() -> webdriver.Firefox:
    """Return customized Firefox driver"""

    firefox_driver_capabilities = DesiredCapabilities().FIREFOX
    firefox_driver_capabilities["marionette"] = True

    firefox_options = Options()
    firefox_options.headless = True

    firefox_driver = webdriver.Firefox(
        capabilities=firefox_driver_capabilities,
        executable_path=GECKODRIVER_PATH,
        options=firefox_options,
    )

    return firefox_driver


def click_submit_button(driver: webdriver) -> None:
    """Click submit button on the form"""

    submit_button = driver.find_element_by_class_name(SUBMIT_BUTTON_CLASS)
    submit_button.click()


def fill_input(name: str, value: str, driver: webdriver) -> None:
    """Fill input on the form"""

    input = driver.find_element_by_name(name)
    input.send_keys(value)


def register_user(username: str, password: str, driver: webdriver) -> None:
    """Signup the user on the site"""

    driver.get(SITE_DOMAIN + SIGNUP_URL)

    fill_input("username", username, driver)
    fill_input("password1", password, driver)
    fill_input("password2", password, driver)

    click_submit_button(driver)

    print(f'User {username} is in database')


def authenticate_user(username: str, password: str, driver: webdriver) -> None:
    """Authenticate the user on the site"""

    driver.get(SITE_DOMAIN + LOGIN_URL)

    fill_input("username", username, driver)
    fill_input("password", password, driver)

    click_submit_button(driver)

    print(f'Logged in as {username}')


def create_post(title: str, content: str, driver: webdriver) -> None:
    """Create user's post"""

    driver.get(SITE_DOMAIN + POST_CREATE_URL)

    fill_input("title", title, driver)
    fill_input("content", content, driver)

    click_submit_button(driver)

    print(f'Created post "{title}"')


def create_all_user_posts(username: str, posts_amount: int, driver: webdriver):
    """Create all posts for the user"""

    for post_number in range(1, posts_amount + 1):
        create_post(
            f'Title for post {post_number} created by {username}',
            f'Content for post {post_number} created by {username}',
            driver,
        )


def get_all_posts(driver: webdriver) -> list:
    """Return all divs with post_estimation class from posts page"""

    driver.get(SITE_DOMAIN + ALL_POSTS_URL)

    return driver.find_elements_by_class_name(ESTIMATION_CLASS)


def like_post(post: webdriver) -> None:
    """Like the post"""

    post.find_element_by_class_name(LIKE_CLASS).click()


def dislike_post(post: webdriver) -> None:
    """Dislike the post"""

    post.find_element_by_class_name(DISLIKE_CLASS).click()


def get_random_bool() -> bool:
    """Randomly return True or False"""

    return bool(randint(0, 1))


def like_posts_by_one_user(driver: webdriver):
    """Randomly like posts by one user"""

    user_likes = 0

    all_posts = get_all_posts(driver)

    for post in all_posts:
        if user_likes < MAX_LIKES_PER_USER:
            is_user_likes_post = get_random_bool()

            if is_user_likes_post:
                like_post(post)
                user_likes += 1
            else:
                is_user_dislikes_post = get_random_bool()

                if is_user_dislikes_post:
                    dislike_post(post)


if __name__ == '__main__':
    firefox_driver = get_firefox_driver()

    for user_number in range(USERS_AMOUNT):
        username = f'selenium_test_user_{user_number + 1}'
        posts_amount = randint(1, MAX_POSTS_PER_USER)

        register_user(
            username, USER_PASSWORD, firefox_driver,
        )

        authenticate_user(
            username, USER_PASSWORD, firefox_driver,
        )

        create_all_user_posts(
            username, posts_amount, firefox_driver,
        )

    for user_number in range(USERS_AMOUNT):
        username = f'selenium_test_user_{user_number + 1}'

        authenticate_user(
            username, USER_PASSWORD, firefox_driver,
        )

        like_posts_by_one_user(firefox_driver)

    firefox_driver.close()
