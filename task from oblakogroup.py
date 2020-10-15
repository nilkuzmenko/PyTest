#Launch command:
#pytest -v -s TodoTest.py

import pytest
from selenium import webdriver
#import time

#WARNING To run the test correctly, you must use a new blank page!
link = "http://qa-assignment.oblakogroup.ru/board/:nilk"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    #time.sleep(1) #debug wait time to see the result
    browser.quit()

class TestMainPage():
    def test_web_page_availability(self, browser):
        assert browser.title == 'Task2Project'

    def test_h1_visible_and_match(self, browser):
        h1name = browser.find_element_by_tag_name('h1').text
        assert h1name == 'Задачи'

    def test_add_button_exists(self, browser):
        browser.find_element_by_css_selector("#add_new_todo").click()

    def test_add_form_elements_check(self, browser):
        browser.find_element_by_css_selector("#add_new_todo").click() #add new
        browser.find_element_by_css_selector(".selection").click() #click on the dropmenu
        browser.find_element_by_css_selector(".selection").click() #click on the dropmenu to close
        browser.find_element_by_css_selector("#project_text").click() #click on the task field
        browser.find_element_by_css_selector(".hide_btn").click() #cancel button

        browser.find_element_by_css_selector("#add_new_todo").click() #add new
        browser.find_element_by_css_selector(".add_todo").click() #ok button

    def test_project_title_appearance_check(self, browser):
        browser.find_element_by_css_selector("#add_new_todo").click() #add new
        browser.find_element_by_css_selector(".selection").click() #click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click() #click on the project title field

    def test_calcel_button_working_when_new_list_selected(self, browser):
        browser.find_element_by_css_selector("#add_new_todo").click() #add new
        browser.find_element_by_css_selector(".selection").click() #click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector(".hide_btn").click()  # cancel button

    def test_new_category_1_task_a(self, browser):
        title="1"
        task="a"
        browser.find_element_by_css_selector("#add_new_todo").click() #add new
        browser.find_element_by_css_selector(".selection").click() #click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  #list title field
        browser.find_element_by_css_selector("#project_title").send_keys(title)  #list title field
        browser.find_element_by_css_selector("#project_text").click()  #task field
        browser.find_element_by_css_selector("#project_text").send_keys(task) #task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        #result check: dublicate count
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label[text() = "{task}"]'))
        assert n == 1, "Wrong number of unique combinations. 0 - combination doesnt exist. >1 - there are too many combinations"

    def test_new_category_c_task_1(self, browser):
        title="c"
        task="1"
        browser.find_element_by_css_selector("#add_new_todo").click() #add new
        browser.find_element_by_css_selector(".selection").click() #click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  #list title field
        browser.find_element_by_css_selector("#project_title").send_keys(title)  #list title field
        browser.find_element_by_css_selector("#project_text").click()  #task field
        browser.find_element_by_css_selector("#project_text").send_keys(task) #task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        #result check: dublicate count
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label[text() = "{task}"]'))
        assert n == 1, "Wrong number of unique combinations. 0 - combination doesnt exist. >1 - there are too many combinations"

    def test_new_category_C_task_1(self, browser):
        title="C"
        task="1"
        browser.find_element_by_css_selector("#add_new_todo").click() #add new
        browser.find_element_by_css_selector(".selection").click() #click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  #list title field
        browser.find_element_by_css_selector("#project_title").send_keys(title)  #list title field
        browser.find_element_by_css_selector("#project_text").click()  #task field
        browser.find_element_by_css_selector("#project_text").send_keys(task) #task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        #result check: dublicate count
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label[text() = "{task}"]'))
        assert n == 1, "Wrong number of unique combinations. 0 - combination doesnt exist. >1 - there are too many combinations"

    def test_new_category_C_сyrillic_task_1(self, browser):
        title="С"
        task="1"
        browser.find_element_by_css_selector("#add_new_todo").click() #add new
        browser.find_element_by_css_selector(".selection").click() #click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  #list title field
        browser.find_element_by_css_selector("#project_title").send_keys(title)  #list title field
        browser.find_element_by_css_selector("#project_text").click()  #task field
        browser.find_element_by_css_selector("#project_text").send_keys(task) #task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        #result check: dublicate count
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label[text() = "{task}"]'))
        assert n == 1, "Wrong number of unique combinations. 0 - combination doesnt exist. >1 - there are too many combinations"

    def test_add_existing_category_1_task_b(self, browser):
        title = "1"
        task = "b"
        browser.find_element_by_css_selector("#add_new_todo").click()  # add new
        browser.find_element_by_css_selector(".selection").click()  # click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  # list title field
        browser.find_element_by_css_selector("#project_title").send_keys(title)  # list title field
        browser.find_element_by_css_selector("#project_text").click()  # task field
        browser.find_element_by_css_selector("#project_text").send_keys(task)  # task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        # result check: dublicate count
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label[text() = "{task}"]'))
        assert n == 1, "Wrong number of unique combinations. 0 - combination doesnt exist. >1 - there are too many combinations"
        # result check: check for "2 tasks exist"
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label'))
        assert n == 2, "Wrong number of unique combinations. 0 - combination doesnt exist. >2 - there are too many combinations"

    def test_add_existing_category_1_task_A(self, browser):
        title = "1"
        task = "A"
        browser.find_element_by_css_selector("#add_new_todo").click()  # add new
        browser.find_element_by_css_selector(".selection").click()  # click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  # list title field
        browser.find_element_by_css_selector("#project_title").send_keys(title)  # list title field
        browser.find_element_by_css_selector("#project_text").click()  # task field
        browser.find_element_by_css_selector("#project_text").send_keys(task)  # task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        # result check: dublicate count
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label[text() = "{task}"]'))
        assert n == 1, "Wrong number of unique combinations. 0 - combination doesnt exist. >1 - there are too many combinations"
        # result check: check for "2 tasks exist"
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label'))
        assert n == 3, "Wrong number of unique combinations. 0 - combination doesnt exist. >3 - there are too many combinations"

    def test_add_existing_category_1_task_A_сyrillic(self, browser):
        title = "1"
        task = "А"
        browser.find_element_by_css_selector("#add_new_todo").click()  # add new
        browser.find_element_by_css_selector(".selection").click()  # click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  # list title field
        browser.find_element_by_css_selector("#project_title").send_keys(title)  # list title field
        browser.find_element_by_css_selector("#project_text").click()  # task field
        browser.find_element_by_css_selector("#project_text").send_keys(task)  # task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        # result check: dublicate count
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label[text() = "{task}"]'))
        assert n == 1, "Wrong number of unique combinations. 0 - combination doesnt exist. >1 - there are too many combinations"
        # result check: check for "2 tasks exist"
        n = len(browser.find_elements_by_xpath(f'// div[@class="shadow_todos"]/ h2[text() = "{title}"] / ancestor::div[@class="shadow_todos"] // label'))
        assert n == 4, "Wrong number of unique combinations. 0 - combination doesnt exist. >4 - there are too many combinations"

    def test_create_empty_list(self, browser):
      # title = ""
        task = "emptyList"
        count_lists_before = len(browser.find_elements_by_css_selector('.shadow_todos'))
        count_items_before = len(browser.find_elements_by_css_selector('#todo_text'))
        browser.find_element_by_css_selector("#add_new_todo").click()  # add new
        browser.find_element_by_css_selector(".selection").click()  # click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  # list title field
      # browser.find_element_by_css_selector("#project_title").send_keys(title)  # list title field
        browser.find_element_by_css_selector("#project_text").click()  # task field
        browser.find_element_by_css_selector("#project_text").send_keys(task)  # task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        # result check:
        count_lists_after = len(browser.find_elements_by_css_selector('.shadow_todos'))
        count_items_after = len(browser.find_elements_by_css_selector('#todo_text'))
        assert count_lists_before == count_lists_after, "the number of lists has changed"
        assert count_items_before == count_items_after, "the number of items has changed"

    def test_create_empty_task(self, browser):
        title = "emptyTask"
      # task = ""
        count_lists_before = len(browser.find_elements_by_css_selector('.shadow_todos'))
        count_items_before = len(browser.find_elements_by_css_selector('#todo_text'))
        browser.find_element_by_css_selector("#add_new_todo").click()  # add new
        browser.find_element_by_css_selector(".selection").click()  # click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  # list title field
        browser.find_element_by_css_selector("#project_title").send_keys(title)  # list title field
        browser.find_element_by_css_selector("#project_text").click()  # task field
     #  browser.find_element_by_css_selector("#project_text").send_keys(task)  # task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        # result check:
        count_lists_after = len(browser.find_elements_by_css_selector('.shadow_todos'))
        count_items_after = len(browser.find_elements_by_css_selector('#todo_text'))
        assert count_lists_before == count_lists_after, "the number of lists has changed"
        assert count_items_before == count_items_after, "the number of items has changed"


    def test_create_empty_list_and_task(self, browser):
      # title = ""
      # task = ""
        count_lists_before = len(browser.find_elements_by_css_selector('.shadow_todos'))
        count_items_before = len(browser.find_elements_by_css_selector('#todo_text'))
        browser.find_element_by_css_selector("#add_new_todo").click()  # add new
        browser.find_element_by_css_selector(".selection").click()  # click on the dropmenu
        browser.find_element_by_xpath('//li[text()="Создать новый список"]').click()
        browser.find_element_by_css_selector("#project_title").click()  # list title field
      # browser.find_element_by_css_selector("#project_title").send_keys(title)  # list title field
        browser.find_element_by_css_selector("#project_text").click()  # task field
      # browser.find_element_by_css_selector("#project_text").send_keys(task)  # task field
        browser.find_element_by_css_selector(".add_todo").click()  # ok button
        # result check:
        count_lists_after = len(browser.find_elements_by_css_selector('.shadow_todos'))
        count_items_after = len(browser.find_elements_by_css_selector('#todo_text'))
        assert count_lists_before == count_lists_after, "the number of lists has changed"
        assert count_items_before == count_items_after, "the number of items has changed"
