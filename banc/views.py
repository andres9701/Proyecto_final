
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from banc.repository.persona_repository import PersonaRepository
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from banc.manager.persona_manager import PersonaManager
from django.http import Http404



# Create your views here.


#import manger file


class APIViewPersona(APIView):
    
    def __init__(self):
        self.manager = PersonaManager()

    def post(self, request):
        if request.method == 'POST':
            try:
                parameters = request.GET.copy() #params by url
                parameters = request.data.copy() #params by json
                print('holaaaa1')
                response = self.manager.create_persona(parameters)
                print('responsse:', response)
                print('holaaaa2')
                return Response({"mesage": response})
            except Exception as e:
                return HttpResponse({"error": e.message}, status=int(e.status))

    def delete(self, request):
        if request.method == 'DELETE':
            try:
                parameters = request.data #params by json
                print('delete_data:', parameters)
                response = self.manager.delete_persona(parameters)
                print('responsse:', response)
                print('holaaaa2')
                return JsonResponse({'message': 'Data deleted successfully'}, status=status.HTTP_200_OK)
            except Http404:
                return Response({'message': 'ID no encontrado'}, status=status.HTTP_404_NOT_FOUND)
	#def patch(self):
	#	pass

	def put(self):
		pass

    def Persona_list(request, pk):
        if request.method == 'GET':
            try:
                parameters = request.GET.copy() #params by url
                parameters = request.data.copy() #params by json
                parameters = {'id':pk}
                print('parameters', parameters)
                print('holaaaa1')
                response = self.manager.create_persona(parameters)
                print('responsse:', response)
                print('holaaaa2')
                return Response({"mesage": response})
            except Exception as e:
                return HttpResponse({"error": e.message}, status=int(e.status))

#-------------------------------
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Persona

#     def Persona_list(request):
#         Personas = Persona.objects.all()
#         return render(request, 'crud_app/Persona_list.html', {'Personas': Personas})

#     def Persona_create(request):
#         if request.method == 'POST':
#             nombre = request.POST['nombre']
#             apellido = request.POST['apellido']
#             cedula = request.POST['cedula']
#             Persona = Persona(nombre=nombre, apellido=apellido, cedula=cedula)
#             Persona.save()
#             return redirect('Persona_list')
#         return render(request, 'crud_app/Persona_create.html')

#     def Persona_update(request, pk):
#         persona = get_object_or_404(persona, pk=pk)
#         if request.method == 'POST':
#             persona.nombre = request.POST['nombre']
#             persona.apellido = request.POST['apellido']
#             persona.cedula = request.POST['cedula']
#             persona.save()
#             return redirect('Persona_list')
#         return render(request, 'crud_app/Persona_update.html', {'Persona': persona})

#     def Persona_delete(request, pk):
#         Persona = get_object_or_404(Persona, pk=pk)
#         if request.method == 'POST':
#             Persona.delete()
#             return redirect('Persona_list')
#         return render(request, 'crud_app/Persona_delete.html', {'Persona': Persona})
