class TabelaHash:

    def __init__(self, size):
        self._size = size
        self._tabela = [[] for _ in range(self._size)]

    def _hash_function(self, chave):

        hash_code = hash(chave)

        return hash_code % self._size

    def add(self, chave, valor):
        
        idx = self._hash_function(chave)

        for i, (k, v) in enumerate(self._tabela[idx]):

            if k == chave:

                self._tabela[idx][i] = (chave, valor)
                return

        self._tabela[idx].append((chave, valor))
        
        if self._load_factor() >= 0.7:

            self._tabela = self._resized()

    def get(self, chave, defaut = None):
        
        idx = self._hash_function(chave)

        for (k, v) in self._tabela[idx]: 

            if k == chave:

                return v
            
        return defaut

    def delete(self, chave):
        
        idx = self._hash_function(chave)

        self._tabela[idx] = [(k,v) for k,v in self._tabela[idx] if k != chave]

    def _resized(self):

        self._size = self._size * 2

        tabela = self._tabela

        self._tabela = [[] for _ in range(self._size)]

        for bucket in tabela:

            for chave, valor in bucket:

                idx = self._hash_function(chave)

                self._tabela[idx].append((chave, valor))

        return self._tabela

    def _load_factor(self):

        counts = 0

        for bucket in self._tabela:

            counts += len(bucket)

        return (counts / self._size)
        
    def visualise(self):
        print(f"Tamanho atual do array: {self._size} | Fator de Carga: {self._load_factor():.2f}")
        print(self._tabela)



