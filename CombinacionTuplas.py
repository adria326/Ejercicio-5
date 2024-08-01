#objetivos: utilizar ciclos for para iterar sobre una lista de tuplas.
#instrucciones: Dada una lista de tuplasque contiene el nombre y la edad de varias personas, usa un ciclo for para imprimir
#un mensaje personalizado para cada persona.

personas = [("Madeleine", 4) , ("Asley", 10) , ("Martha", 15) , ("Darling", 19)]
for nombre, edad in personas:
    print("Hola soy {nombre} y tengo {edad} años.")