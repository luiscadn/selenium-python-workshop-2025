from behave import given, when, then
from selenium import webdriver
from pages.wikipedia_home_page import WikipediaHomePage
from pages.wikipedia_article_page import WikipediaArticlePage

@given('que el usuario está en la página de inicio de Wikipedia')
def step_given_open_wikipedia(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://es.wikipedia.org/")
    context.driver.maximize_window()
    context.home_page = WikipediaHomePage(context.driver)

@when('busca el término "Python (lenguaje de programación)"')
def step_when_search_article(context):
    context.home_page.search_article("Python (lenguaje de programación)")
    context.article_page = WikipediaArticlePage(context.driver)

@then('el título del artículo debe ser "Python (lenguaje de programación)"')
def step_then_validate_article_title(context):
    expected_title = "Python"
    actual_title = context.article_page.get_article_title()
    assert actual_title == expected_title, f"Expected '{expected_title}' but got '{actual_title}'"
    context.driver.quit()
