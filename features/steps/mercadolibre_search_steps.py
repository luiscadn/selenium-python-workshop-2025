from behave import given, when, then
from selenium import webdriver
from pages.mercadolibre_search_page import MercadoLibrePage

@given('que el usuario está en la página de inicio de MercadoLibre')
def step_given_open_mercadolibre(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.mercadolibre.com.co/")
    context.mercadolibre_page = MercadoLibrePage(context.driver)

@when('busca el producto "iPhone 13"')
def step_when_search_product(context):
    context.mercadolibre_page.search_product("iPhone 13")

@then('se muestran resultados que contienen "iPhone"')
def step_then_verify_results(context):
    assert context.mercadolibre_page.verify_results("iPhone")
    context.driver.quit()
