import json
from banc.repository.persona_repository import PersonaRepository
from rest_framework import serializers
#from banc.serializer.persona_serializer import PersonaSerializer
from ..serializer.persona_serializer import PersonaSerializer



class DataExceptions():

	def __init__(self):
		self.repository = PersonaRepository()

	
	def validate_data(self, data):
		#print('pkssss:', pk.get('pk'))
		if  data:
			print('data_found_dddd1')
			return  'deleted successfully'
		else:
			print('data_no_found_')
			return 'Pk not found'