class VerticeInexistenteException(Exception):
    
    def __init__(self,message :str, vertices :list):
        super().__init__(message)
        self.vertices = vertices