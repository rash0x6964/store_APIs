from django.contrib.auth.models import User
from rest_framework import status
from model_bakery import baker
import pytest
from store_app.models import Collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        res = api_client.post('/store/collections/', {'title': 'a'})

        assert res.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, api_client):
        api_client.force_authenticate(user={})
        res = api_client.post('/store/collections/', {'title': 'a'})

        assert res.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, api_client):
        api_client.force_authenticate(user=User(is_staff=True))
        res = api_client.post('/store/collections/', {'title': ''})

        assert res.status_code == status.HTTP_400_BAD_REQUEST
        assert res.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, api_client):
        api_client.force_authenticate(user=User(is_staff=True))
        res = api_client.post('/store/collections/', {'title': 'a'})

        assert res.status_code == status.HTTP_201_CREATED
        assert res.data['id'] > 0

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_return_200(self, api_client):
        collection = baker.make(Collection)
        res = api_client.get(f'/store/collections/{collection.id}/')

        assert res.status_code == status.HTTP_200_OK
        assert res.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }
