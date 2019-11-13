from rest_framework import serializers
import rest_framework_datatables
from .models import Variants

class VariantsSerializer(serializers.ModelSerializer):

	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = Variants
		fields = ('gene', 'nucleotide_change', 'protein_change', 'other_mappings', 'alias', 'transcripts', 'region', 'reported_classification', 'inferred_classification', 'source', 'last_evaluated', 'last_updated', 'url', 'submitter_comment', 'assembly', 'chr', 'genomic_start', 'genomic_stop', 'ref', 'alt', 'accession', 'reported_ref', 'reported_alt', 'id')
		# Specifying fields in datatables_always_serialize will also force them to always be serialized.
		datatables_always_serialize = ('id',)
