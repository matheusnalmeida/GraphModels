#Classe usada para erros gerais relacionados as arestas
class ArestasIncompatibilityException(Exception):

    def __init__(self,message :str):
        super().__init__(message)