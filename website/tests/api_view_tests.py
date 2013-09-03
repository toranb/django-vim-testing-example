import json
from django import test
from website.models import Session
from django.core.urlresolvers import reverse


class SessionAPIRetrieveViewTests(test.TestCase):

    def test_will_return_session_by_id(self):
        session = Session.objects.create(title='testing')
        endpoint = reverse('retrieve', kwargs={'pk': session.pk})
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        model = json.loads(response.content)
        self.assertEqual(model['title'], 'testing')


class SessionAPIListViewTests(test.TestCase):

    def test_will_return_created_http_status_when_successful(self):
        payload = dict(title='foo')
        endpoint = reverse('list')
        response = self.client.post(endpoint, payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Session.objects.all()), 1)

    def test_will_raise_validation_error_when_title_is_django(self):
        payload = dict(title='django')
        endpoint = reverse('list')
        response = self.client.post(endpoint, payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, '{"title": ["INVALID DATA: title cannot be django"]}')
        self.assertEqual(len(Session.objects.all()), 0)
