from Buscas.caminho import Caminho

class CaminhoInexistenteException(Exception):
    def __init__(self,message :str, caminho :Caminho):
        super().__init__(message)
        self.caminho = caminho