from django.db import models
		
class Variants(models.Model):

	id = models.IntegerField(blank=True, primary_key=True)
	gene = models.TextField(db_column='Gene', blank=True, null=True)
	nucleotide_change = models.TextField(db_column='Nucleotide_Change', blank=True, null=True)
	protein_change = models.TextField(db_column='Protein_Change', blank=True, null=True)
	other_mappings = models.TextField(db_column='Other_Mappings', blank=True, null=True)
	alias = models.TextField(db_column='Alias', blank=True, null=True)
	transcripts = models.TextField(db_column='Transcripts', blank=True, null=True)
	region = models.TextField(db_column='Region', blank=True, null=True)
	reported_classification = models.TextField(db_column='Reported_Classification', blank=True, null=True)
	inferred_classification = models.TextField(db_column='Inferred_Classification', blank=True, null=True)
	source = models.TextField(db_column='Source', blank=True, null=True)
	last_evaluated = models.TextField(db_column='Last_Evaluated', blank=True, null=True) 
	last_updated = models.TextField(db_column='Last_Updated', blank=True, null=True) 
	url = models.TextField(db_column='URL', blank=True, null=True)
	submitter_comment = models.TextField(db_column='Submitter_Comment', blank=True, null=True)
	assembly = models.TextField(db_column='Assembly', blank=True, null=True)
	chr = models.TextField(db_column='Chr', blank=True, null=True)
	genomic_start = models.TextField(db_column='Genomic_Start', blank=True, null=True)
	genomic_stop = models.TextField(db_column='Genomic_Stop', blank=True, null=True)
	ref = models.TextField(db_column='Ref', blank=True, null=True)
	alt = models.TextField(db_column='Alt', blank=True, null=True)
	accession = models.TextField(db_column='Accession', blank=True, null=True)
	reported_ref = models.TextField(db_column='Reported_Ref', blank=True, null=True)
	reported_alt = models.TextField(db_column='Reported_Alt', blank=True, null=True)

	class Meta:
		verbose_name = 'Variants'
		ordering = ['-gene']

