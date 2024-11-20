def intercalar(lista1, lista2):
    resultado = []
    i, j = 0, 0
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
            
    while i < len(lista1):
        resultado.append(lista1[i])
        i += 1
    
    while j < len(lista2):
        resultado.append(lista2[j])
        j += 1
    
    return resultado

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    
    return intercalar(izquierda, derecha)

lista_a_ordenar = [38, 27, 43, 3, 9, 82, 10]
resultado = merge_sort(lista_a_ordenar)
print("Merge Sort:", resultado)