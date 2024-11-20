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
            
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    
    return resultado


lista_a = [1, 3, 5]
lista_b = [2, 4, 6]
resultado = intercalar(lista_a, lista_b)
print("Intercalación:", resultado)