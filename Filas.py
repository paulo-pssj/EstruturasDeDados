# filas: primeiro que entra é o primeiro que sai

class Nodo:
    """Representa um Nodo de uma estrutura duplamente encadeada"""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
        
    def __repr__(self):
        return f"{self.dado} -> {self.proximo}"
    
class Fila:
    """Representa uma fila usando estrutura encadeada"""
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def __repr__(self):
        return "[" + str(self.primeiro) + "]"
    
    def insere(self, novo_dado):
        """insere um elemento no final da fila"""
        
        #cria novo nodo com o dado a ser armazenado
        novo_nodo = Nodo(novo_dado)
        
        # insere em uma fila vazia
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
            
        else:
            # faz que o novo nodo seja o ultimo
            self.ultimo.proximo = novo_nodo
            
            # faz que o ultimo da fila referencie o novo nodo
            self.ultimo = novo_nodo
            
    def remove(self):
        """remove o primeiro elemento da fila"""
        
        assert self.primeiro != None, "Impossivel remover elemento de fila vazia"
        
        self.primeiro = self.primeiro.proximo
        
        if self.primeiro == None:
            self.ultimo = None
            
# Criando fila vazia, add elementos e removendo

fila = Fila()
print("Fila vazia: ", fila)

for i in range(5):
    fila.insere(i)
    print(f"Insere o valor {i} final da fila: {fila}")
    
while fila.primeiro != None:
    fila.remove()
    print("Removendo elemento que está no começo da fila: ", fila)