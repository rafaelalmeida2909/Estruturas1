class Fila:
    """Representaçãõ de um estrutura de fila sequencial em python (sem prioridade)"""
    def __init__(self, maximo):
        self.max = maximo # Tamanho máximo da fila
        self.fila = [None] * maximo # Fila iniciada com tamanho definido
        self.inicio = 0 # Define o elemento que deverá sair primeiro da fila
        self._quantidade = 0 # Atributo privado que diz o nº de elementos na fila
        self.final = 0 # Define o espaço que um elemento qualquer vai preencher ao entrar na fila

    @property
    def max(self):
        """Retorna o valor do atributo max"""
        return self._max

    @max.setter
    def max(self, maximo):
        """Garante que max tenha um valor inteiro"""
        if isinstance(maximo, int):
            self._max = maximo
        else:
            raise Exception("Atributo deve ser um número inteiro")
    
    def enfileirar(self, elem):
        """Adiciona um elemento ao fim da fila"""
        if self._quantidade == self.max: # Verifica se a fila está cheia
            return "Fila Cheia!"
        self.fila[self.final] = elem
        self.final = (self.final + 1) % self.max # Garante uma fila circular 
        self._quantidade += 1

    def desenfileirar(self):
        """Retira o primeiro elemento da fila"""
        if self._quantidade == 0: # Verifica se a fila está vazia
            return "Fila Vazia!"
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.max # Garante uma fila circular
        self._quantidade -= 1
    
    def tamanho(self):
        """Retorna a quantidade de elementos na fila"""
        return self._quantidade