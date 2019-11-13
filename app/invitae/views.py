from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Variants
from .serializers import VariantsSerializer


def index(request):
	"""Render index page"""
	return render(request, 'invitae/index.html')

class VariantsViewSet(viewsets.ModelViewSet):
	"""Control view"""

	queryset = Variants.objects.all().order_by('-gene')
	serializer_class = VariantsSerializer

	class Meta:
		model = Variants
		fields = ('id', 'gene', 'nucleotide_change', 'protein_change', 'other_mappings', 'alias', 'transcripts', 'region', 'reported_classification', 'inferred_classification', 'source', 'last_evaluated', 'last_updated', 'url', 'submitter_comment', 'assembly', 'chr', 'genomic_start', 'genomic_stop', 'ref', 'alt', 'accession', 'reported_ref', 'reported_alt')

