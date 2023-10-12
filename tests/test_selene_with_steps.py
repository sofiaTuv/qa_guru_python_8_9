import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure_commons.types import Severity


def test_github():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 's.tuvykina')
    allure.dynamic.feature('Задача в репозитории #76')
    allure.dynamic.story('Я не могу увидеть задачу с номером #76')
    allure.dynamic.link("https://github.com", name="Testing")

    with allure.step('Открыть главную страницу github.com'):
        browser.open("https://github.com")

    with allure.step('Найти репозиторий "{repo}"'):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step('Перейти в репозиторий "eroshenkoam/allure-example"'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Перейти в таб "Issues"'):
        browser.element("#issues-tab").click()

    with allure.step('Найти задачу с номером "{number}"'):
        browser.element(by.partial_text("#76")).should(be.visible)