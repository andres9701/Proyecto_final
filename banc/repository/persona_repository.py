from ..models import Persona


class PersonaRepository():

    def __init__(self):
        pass
    
    def search_by_id(self, id):
        print('llegueeee')
        objeto = Persona.objects.get(pk=id)
        print('seaarch_by_id:', objeto)
        return objeto
    
    def search_by_name(self, ced):
        print('llegueeee2',ced)
        objeto = Persona.objects.filter(nombre=ced)
        print('obje:', objeto)
        return objeto


