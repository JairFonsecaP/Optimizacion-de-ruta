def ruteo(distancias: dict, ruta_inicial: list)-> dict: 
    parejas = []
    parejas2i = []
    iteraciones = 0
    #Validando si existen numeros negativos
    for z in distancias:
        #Validar que los puntos iguales sean 0
        if z[0] == z[1]:
            punto_iguales = distancias.get(z)
            if punto_iguales != 0:
                validacion_1 = True
                break
            else:
                validacion_1 = False
        #Validar que los puntos diferentes sea diferente a 0 y que sea positivo     
        if z[0] != z[1]:
            puntos_diferentes = distancias.get(z)
            if puntos_diferentes <= 0:
                validacion_2 = True
                break
            else:
                validacion_2 = False
    #Validar que no sea negativo            
    
    if validacion_1 == True or validacion_2 == True:
        salida = 'Por favor revisar los datos de entrada.'
    else:
            #Hacer la ruta_inicial en nodos para calcular distancia
            for i in range(0,len(ruta_inicial)-1):
                parejas.append((ruta_inicial[i] , ruta_inicial[i + 1]))  
            
            #Buscar en la matriz distancias    
            kilometros_iniciales = 0
            for j in parejas:
                kilometros_iniciales = kilometros_iniciales + distancias.get(j)
            
            es_mejor = True
            ruta_actual = ruta_inicial.copy()
            ruta_optima = ruta_inicial.copy()
            kilometros_optimos = kilometros_iniciales
            mejores_kilometros = kilometros_optimos
            #Hacer las combinaciones posibles
            while es_mejor == True:
                for h in range(1, len(ruta_actual)-1):
                    for k in range(2, len(ruta_actual)-1):
                        ##Intercambiar las variables
                        if h != k and k > h:
                            kilometros_actuales = 0
                            ruta_actual[k], ruta_actual[h] = ruta_actual[h], ruta_actual[k]
                            parejas2i = []
                            for y in range(0,len(ruta_actual)-1):
                                parejas2i.append((ruta_actual[y] , ruta_actual[y + 1]))
                            ##Sumar kilometros de la nueva combinacion
                            for u in parejas2i:
                                kilometros_actuales = kilometros_actuales + distancias.get(u)
                            if kilometros_optimos > kilometros_actuales and not kilometros_optimos == kilometros_actuales:
                                kilometros_optimos = kilometros_actuales
                                ruta_optima = ruta_actual.copy()                
                            ruta_actual[h], ruta_actual[k] = ruta_actual[k], ruta_actual[h]
                            
                #Verificar si dio mejor resultado  despues de todas las iteraciones     
                if mejores_kilometros > kilometros_optimos:
                    es_mejor = True
                    ruta_actual = []
                    ruta_actual = ruta_optima.copy()
                    mejores_kilometros = kilometros_optimos
                    
                #Si no da mejor reultado terminar iteración       
                else:
                    es_mejor = False
                    
                    salida = {'ruta': '-'.join(ruta_optima), 'distancia': mejores_kilometros,}
     
    
    return salida



print(ruteo({('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241, ('A', 'H'):
127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41, ('B', 'H'): 153, ('B', 'A'): 252, ('B',
'B'): 555, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0,
('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'):
194, ('D', 'F'): 109, ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119, ('F',
'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0},['H', 'B', 'D', 'A', 'F', 'C', 'E', 'H']))

##Respuesta verdadera {'ruta': 'H-A-F-B-D-C-E-H', 'distancia': 458}
print(ruteo({('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241, ('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109, ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119, ('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}, ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']))

## Respuesta verdera {'ruta': 'H-D-A-B-C-E-H', 'distancia': 393}
print(ruteo({('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27, ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117, ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199, ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19, ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31, ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}, ['H', 'B', 'E', 'A', 'C', 'D', 'H']))

##Respuesta verdadera {'ruta': 'MDE-SMR-PEI-CTG-BOG-MDE', 'distancia': 370}
print(ruteo({('BOG', 'BOG'): 0, ('BOG', 'MDE'): 21, ('BOG', 'PEI'): 57, ('BOG', 'SMR'): 58, ('BOG', 'CTG'): 195, ('MDE',
'BOG'): 127, ('MDE', 'MDE'): 0, ('MDE', 'PEI'): 231, ('MDE', 'SMR'): 113, ('MDE', 'CTG'): 254, ('PEI', 'BOG'): 153, ('PEI',
'MDE'): 252, ('PEI', 'PEI'): 0, ('PEI', 'SMR'): 56, ('PEI', 'CTG'): 126, ('SMR', 'BOG'): 196, ('SMR', 'MDE'): 128, ('SMR',
'PEI'): 80, ('SMR', 'SMR'): 0, ('SMR', 'CTG'): 136, ('CTG', 'BOG'): 30, ('CTG', 'MDE'): 40, ('CTG', 'PEI'): 256, ('CTG',
'SMR'): 121, ('CTG', 'CTG'): 0},['MDE', 'PEI', 'BOG', 'CTG', 'SMR', 'MDE']))
                                                                                                                  

##Respuesta Verdadera "Por favor revisar los datos de entrada."                                                                                                                 
print(ruteo({('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): -5, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0},
['H', 'B', 'E', 'A', 'C', 'D', 'H']))


##Respues Verdadera "Por favor revisar los datos de entrada."
print(ruteo({('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): -5, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'): 50, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0},
['H', 'B', 'E', 'A', 'C', 'D', 'H']))



