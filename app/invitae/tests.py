from django.test import TestCase, override_settings, modify_settings
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.settings import api_settings
from rest_framework_datatables.pagination import (
	DatatablesLimitOffsetPagination, DatatablesPageNumberPagination
)
from invitae.views import VariantsViewSet
from invitae.serializers import VariantsSerializer

# local
from .models import Variants

class ViewTests(TestCase):
	fixtures = ['test.json']

	def setUp(self):
		self.client = APIClient()
		VariantsViewSet.pagination_class = DatatablesPageNumberPagination

	def test_resolved(self):
		"""Test to ensure testing is working"""
		expected = 'semeon'
		self.assertEquals('semeon', expected)

	def test_get_table_length(self):
		"""check if table length is correct"""
		response = self.client.get("/api/variants/?format=datatables")
		expected = 20
		result = response.json()
		self.assertEquals(result['recordsTotal'], expected)
