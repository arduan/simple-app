from django.test import SimpleTestCase


class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        resource = self.client.get('/')
        self.assertEqual(resource.status_code, 200)

    def test_about_page_code(self):
        resource = self.client.get('/about/')
        self.assertEqual(resource.status_code, 200)
