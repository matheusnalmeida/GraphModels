from Buscas.caminho import Caminho

class CaminhoExistenteException(Exception):
    def __init__(self,message :str, caminho :Caminho):
        super().__init__(message)
        self.caminho = caminho