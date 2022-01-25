def busca_binaria_recursiva(A, esquerda, direita, item):
    """Implementa busca binária recursivamente."""
    if direita < esquerda:
        return -1
    
    meio = (esquerda + direita) // 2
    
    if A[meio] == item:
        return meio
    
    elif A[meio] > item:
        return busca_binaria_recursiva(A, esquerda, meio - 1, item)
    
    else:
        return busca_binaria_recursiva(A, meio + 1, direita, item)
    

A = [0, 10, 20, 30, 40, 50, 60, 70]
print("Pesquisa com sucesso:", busca_binaria_recursiva(A, 0, len(A) - 1, 20))
print("Pesquisa sem sucesso:", busca_binaria_recursiva(A, 0, len(A) - 1, 100))