import json
from banc.repository.persona_repository import PersonaRepository
from rest_framework import serializers
#from banc.serializer.persona_serializer import PersonaSerializer
from ..serializer.persona_serializer import PersonaSerializer



class PersonaManager():

	def __init__(self):
		self.repository = PersonaRepository()

	def create_persona(self, data):
		print('create_persona1')
		# dataa=data['data']
		print('dataa1:')
		serializer = PersonaSerializer(data=data['data'])
		print('create_persona')
		if serializer.is_valid():
			serializer.save()
			created_user = json.dumps(serializer.data)
			created_user = json.loads(created_user)
			return created_user
		
	def delete_persona(self, data):
		#print('pkssss:', pk.get('pk'))
		print('pkkkk:',data)
		ced= data['data']['cedula']
		print('nameeee:', ced)
		data_found=self.repository.search_by_name(ced)
		# serializer = PersonaSerializer(dataa)
		print('data_found_delete:', len(data_found))
		# print('serializer_found_delete:', serializer)
		if  data_found:
			print('data_found_dddd1')
			data_found.delete()
			return  'deleted successfully'
		else:
			print('data_no_found_')
			return 'Pk not found'
		
	def list_persona(self,pk):
		data_found=self.repository.search_by_id(pk)
		serializer = PersonaSerializer(data=data_found)
		print('data found:',serializer)
		return serializer