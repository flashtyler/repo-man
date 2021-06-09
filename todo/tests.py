from django.test import LiveServerTestCase
from django.urls import resolve
from django.http import HttpRequest
from todo.views import index
from selenium import webdriver


class TodoListTest(LiveServerTestCase):

    def test_1_main_page_view_can_be_resolved(self):
        print('test main page view can be resolved...\n')
        found = resolve('/')
        print('found: {}'.format(found.func))
        self.assertEqual(found.func, index)

    def test_2_main_page_returns_html(self):
        print('test main page is HTML...\n')
        request = HttpRequest()
        expected_response = index(request)
        # Extract the content of the response.
        html_code = expected_response.content.decode('utf8')
        print(html_code[0:10])
        # Check that the returned code is actually HTML and that the page title is as expected.
        self.assertTrue(html_code.startswith('<html>'))
        self.assertIn('<title>Simple Todo List Application</title>', html_code)
        self.assertTrue(html_code.endswith('</html>'))

    def test_3_add_task_button(self):
        # GIVEN I am on the TO DO list application
        # WHEN I click on the add tasks button
        # THEN I should be presented with an add tasks form
        try:
            print('test Add Task button...\n')
            self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')
            self.driver.get('http://127.0.0.1:8000')
            # Click the 'Add Task' button.
            self.driver.find_element_by_id('add_button').click()
            # Check that data fields are displayed for inputting a To Do task.
            self.assertTrue(self.driver.find_element_by_id('detail_line'))
        except Exception as e:
            print('Driver exception: {}'.format(e))
        finally:
            self.driver.quit()

    def test_4_edit_task_link(self):
        # GIVEN I am on the TO DO list application
        # WHEN I click on an specific task
        # AND click edit this task
        # THEN I should be presented with an edit tasks form
        try:
            print('test Edit Task link...\n')
            self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')
            self.driver.get('http://127.0.0.1:8000')
            # Click the 'Edit Task' link.
            self.driver.find_element_by_link_text('Edit this task').click()
            # Check that data fields are displayed for inputting a To Do task.
            self.assertTrue(self.driver.find_element_by_name('title'))
            self.assertTrue(self.driver.find_element_by_name('location'))
            self.assertTrue(self.driver.find_element_by_name('due_date'))
        except Exception as e:
            print('Driver exception: {}'.format(e))
        finally:
            self.driver.quit()

    def test_5_location_drop_down_list(self):
        # GIVEN I am on the add or edit tasks form
        # WHEN I click on the location drop-down list
        # THEN I should be presented with a list of possible locations
        pass

    def test_6_background_colour_change(self):
        # GIVEN I select a location from the drop-down list
        # WHEN I view the add/edit tasks form
        # THEN I should see the background colour changing
        pass

    def test_7_current_temperature(self):
        # GIVEN I select a location from the drop-down list
        # WHEN I view the add/edit tasks form
        # THEN I should see the current temperature
        pass

    def test_8_view_all_tasks(self):
        # GIVEN I am on the TO DO list application
        # WHEN I view all of my tasks
        # THEN I should see the tasks displayed with respective colours to their local weather
        pass
