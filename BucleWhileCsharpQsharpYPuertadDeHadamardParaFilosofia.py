import random
import math

#######
#### IMPORTANTE: Todo éste cálculo está dedicado a la nota al pie número 31 de mi tesis.
    ### Asimismo, el código realiza lo siguiente: 
        # Genera un 'bucle while' que simula la superposición cuántica y la medición cuántica, aplicando la puerta Hadamard
        # y conceptos filosóficos reflejados dentro de la tesis "Modelamiento de redes físico-ideales

#### GLOSARIO DE LAS PUERTAS CUÁNTICAS (saltar comentario si no interesa):
    # Las puertas cuánticas son operadores unitarios que actúan sobre los estados cuánticos.
    # La puerta Hadamard es una puerta cuántica (básica y simple) que transforma los estados base en superposiciones.
    # La medición cuántica es el proceso que colapsa el estado cuántico a un estado base.
    # En nuestra interpretación de la Fenomenología Hegeliana, la puerta de Hadamard simboliza 
    # la superposición de la tesis y la antítesis, y la medición cuántica simboliza la síntesis que colapsa el 
    # estado cuántico a un estado base. Hegel argumenta que la síntesis es la resolución de la contradicción 
    # entre la tesis y la antítesis. En Q# y C#, para nosotros la medición cuántica pasa a ser un proceso que resuelve la 
    # indeterminación y negación hegeliana en un estado "indeterminadamente determinado" (o indeterminado-necesario)
    # Esto también nos sirvió para hablar de "Indeterminaciones necesarias" respecto a ciertas emergencias
    # que no son condicionales, sino relacionales, que no pueden modelarse con la Teoría de Grafos clásica.
    # Las posibilidades relacionales tienen un aspecto muy profundo en la teoría cuántica, sobre todo en el
    # concepto de Teleportación respecto de las puertas cuánticas
    # (la teleportación es la forma en que dos cosas se relacionan sin importar la distancia: ésta definición aplica a
    # la Mecánica cuántica y los qubits en lenguajes de programación cuánticos)
#######
    # NOTA 1: Python no es mi lenguaje principal, pero es el más pedagógico para éste caso específico (Mi lenguaje principal es C# y los escalables dentro del ecosistema .NET)
    # NOTA 2: Para ejecutar el código, puede usarse un compilador online de Python con capacidad a librerías (como el de la nota 29).
    
estado_actual = {"|0>": 1+0j, "|1>": 0+0j}

colapsado = False
iteracion = 0

def aplicar_puerta_hadamard(estado_vector):
    """
    Aplica la puerta Hadamard a un estado cuántico representado como un diccionario
    con amplitudes complejas para los estados base.
    
    La transformación Hadamard se define como:
        H|0> = (1/√2)(|0> + |1>)
        H|1> = (1/√2)(|0> - |1>)
    
    Se asume que el vector de estado está normalizado.
    """
    a0 = estado_vector.get("|0>", 0)
    a1 = estado_vector.get("|1>", 0)
    factor = 1 / math.sqrt(2)
    nuevo_estado = {
        "|0>": factor * (a0 + a1),
        "|1>": factor * (a0 - a1)
    }
    return nuevo_estado

def medir_estado(estado_vector):
    """
    Simula una medición cuántica. Calcula las probabilidades de colapso a cada estado base
    a partir de las amplitudes y selecciona aleatoriamente el estado colapsado.
    """
    p0 = abs(estado_vector.get("|0>", 0))**2
    p1 = abs(estado_vector.get("|1>", 0))**2
    total = p0 + p1
    if total == 0:
        raise ValueError("El vector de estado no tiene amplitud (suma cero).")
    p0 /= total
    p1 /= total
    r = random.random()
    return "|0>" if r < p0 else "|1>"

print(
     "Iniciando simulación profunda de superposición cuántica con explicación detallada de la puerta Hadamard,\n"
     "teniendo en mente una reducción de incertidumbre que indica una probabilidad del 20% de colapso...\n"
)
print(f"Estado inicial: {estado_actual}")

    
    ###### Explicación para Filósofos: 
        ###La puerta Hadamard es una puerta cuántica básica que transforma los estados base en superposiciones. 
        ### Es esencial para cualquier computación cuántica.
    # El 'Bucle while' simula la superposición cuántica y la medición cuántica. El bucle 'While' está activo
    # hasta que los estados superpuestos colapsen, y se aplique una puerta de Hadamard. En teoría, es infinito a menos
    # que el programador aplique una 'forma de colapso', como 'break', aunque ésta, si bien es típica en 'juniors', 
    # es muy distinta a la de la mecánica cuántica y es muy forzada o disruptiva para proyectos grandes [dado que significaría problemas potenciales de escalabilidad].
        ### (el bucle es potencialmente infinito al igual que la regresión lineal de la nota al pie 29, eso forma parte de su formalización 
        ### matemática, pero evidentemente no haremos una regresión lineal hasta 'antes de Cristo' o con esas características).
    # En cada iteración, decidimos si se aplica la puerta Hadamard para transformar el estado
    # Aplicamos la puerta Hadamard a cada estado base. Cuando no se aplica Hadamard, el estado se encuentra en
    # superposición. Cuando colapsa, simplemente está determinado entre '0' y '1'. Ésta analogía me ha servido 
    # para explicar la fenomenología de Hegel mediante computación cuántica y regresión lineal-histórica (en las partes eliminadas de la Sección III, sobre Terraria)
    # Sin embargo, la versión sintetizada también incorpora una comprensión implícita sobre la relación entre las Puertas de Hadamard y las negaciones Hegelianas
   
while not colapsado:
    iteracion += 1
    print(f"\n=== Iteración {iteracion} ===")
    print("Estado actual del sistema cuántico (vectores de amplitud):")
    for estado, amplitud in estado_actual.items():
        probabilidad = abs(amplitud)**2
        print(f"  {estado}: Amplitud = {amplitud}  |  Probabilidad = {probabilidad:.4f}")

    decision = random.random()
    if decision < 0.5:
        print("\n>> Decisión interna: Aplicar la puerta Hadamard para transformar la realidad del estado.")
        estado_previo = estado_actual.copy()
        estado_actual = aplicar_puerta_hadamard(estado_actual)
        print(">> Resultado de la transformación:")
        for estado, amplitud in estado_actual.items():
            probabilidad = abs(amplitud)**2
            print(f"  {estado}: Nueva Amplitud = {amplitud}  |  Probabilidad = {probabilidad:.4f}")
    else:
        print("\n>> Decisión interna: Conservar la superposición actual sin intervención; el estado permanece inalterado.")
    
    medicion_decision = random.random()
    if medicion_decision < 0.2:
        print("\n>> Momento de la verdad: Se procede a la medición cuántica, determinando el destino del sistema.")
        resultado = medir_estado(estado_actual)
        print(f"Medición: ¡El sistema colapsa al estado {resultado}!")
        colapsado = True
    else:
        print("\n>> Medición postergada: El sistema continúa en su danza de incertidumbre, flotando en superposición... (sonidos de suspenso)")
    
print("\nEl proceso de medición ha finalizado. Fin de la simulación, y así se resuelve la incertidumbre... (Hegel mira orgulloso desde la distancia)")
