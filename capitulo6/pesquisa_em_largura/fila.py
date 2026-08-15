class Fila:

    def __init__(self):

        self._fila = []

    def enqueue(self, value):

        self._fila.append(value)

    def dequeue(self):

        if not self.is_empty():
        
            return self._fila.pop(0)
    
    def is_empty(self):

        if len(self._fila) == 0:

            return True
        
        return False
    
    def visualise(self):

        print(self._fila)
