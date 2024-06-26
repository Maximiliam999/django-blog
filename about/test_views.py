from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm




class TestAboutviews(TestCase):

    def setUp(self):
        self.about_content = About (
            title = 'About Me',
            content = 'This is about me.',
        )
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_successful_request_submission(self):
        request_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message':'test message'
            }
        response = self.client.post(reverse('about'), request_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)


      