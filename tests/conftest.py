# pytest import pytest
# from selenium import webdriver
# from pages.home.webshop_page import WebshopPage
#
# @pytest.yield_fixture(scope="class")
# def setUp():
#     baseURL = "http://staging.togital.no/konkurrenten/webshop/#/reise"
#     driver = webdriver.Firefox()
#     # driver.maximize_window() #Find a solution for the maximize window issue
#     driver.get(baseURL)
#     driver.implicitly_wait(3)
#     wp = WebshopPage(driver)
#     yield driver