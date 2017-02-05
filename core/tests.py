from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class HappyPathTest(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = WebDriver()
        super(HappyPathTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(HappyPathTest, self).tearDown()

    def test_happy_path(self):
        selenium = self.selenium
        self.selenium.get('%s' % self.live_server_url)

        DATA = {
            'title': 'meeting title',
            'topic': 'meeting topic',
            'link': 'meeting.link',
            'organization': 'meeting organization',
            'location': '1 main st, meeting town',
            'datetime': '1/1/17 11:17'
        }

        # go to meeting form
        selenium.find_element_by_class_name('btn-class-for-test').click()

        # find elements
        title = selenium.find_element_by_id('id_title')
        topic = selenium.find_element_by_id('id_topic')
        link = selenium.find_element_by_id('id_link')
        organization = selenium.find_element_by_id('id_organization')
        location = selenium.find_element_by_id('id_location')
        datetime = selenium.find_element_by_id('id_datetime')

        # fill out fields
        title.send_keys(DATA['title'])
        topic.send_keys(DATA['topic'])
        link.send_keys(DATA['link'])
        organization.send_keys(DATA['organization'])
        location.send_keys(DATA['location'])
        datetime.send_keys(DATA['datetime'])

        # submit form
        xpath = '//input[@value="Post"]'
        selenium.find_element_by_xpath(xpath).click()

        assert 'Meeting posted.' in selenium.page_source
