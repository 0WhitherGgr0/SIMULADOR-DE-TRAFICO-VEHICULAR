
import time
import random
import multiprocessing

# Definición de la clase Carro para representar vehículos
class Carro:
    def __init__(self, nombre):
        self.nombre = nombre

    def cruzar_interseccion(self, interseccion):
        print(f"{self.nombre} cruzó la intersección {interseccion}")

    def esperar_interseccion(self, interseccion):
        print(f"{self.nombre} esperando en la intersección {interseccion}")

    def detenerse_interseccion(self, interseccion):
        print(f"{self.nombre} se detiene en la intersección {interseccion}")

# Definición de la clase Semaforo para representar semáforos
class Semaforo:
    def __init__(self, interseccion):
        self.interseccion = interseccion
        self.ciclos = 5  # Número de ciclos del semáforo

    # Método para controlar el semáforo y el cruce de carros
    def controlar(self, carros):
        for ciclo in range(self.ciclos):
            print(f"Semáforo en la intersección {self.interseccion} - Verde")
            self.permitir_cruce(carros)
            time.sleep(5) # Simular 5 segundos en verde

            print(f"Semáforo en la intersección {self.interseccion} - Amarillo")
            self.esperar_cruce(carros)
            time.sleep(2) # Simular 2 segundos en amarillo

            print(f"Semáforo en la intersección {self.interseccion} - Rojo")
            self.detener_cruce(carros)
            time.sleep(5) # Simular 5 segundos en rojo
     # Método para permitir que los carros crucen
    def permitir_cruce(self, carros):
        for carro in carros:
            carro.cruzar_interseccion(self.interseccion)

    # Método para hacer que los carros esperen en la intersección
    def esperar_cruce(self, carros):
        for carro in carros:
            carro.esperar_interseccion(self.interseccion)

    # Método para hacer que los carros se detengan en la intersección
    def detener_cruce(self, carros):
        for carro in carros:
            carro.detenerse_interseccion(self.interseccion)

if __name__ == "__main__":
    interseccion = "Avenida Principal" # Nombre de la intersección

  # Crear tres objetos Carro
    carro1 = Carro("Carro 1")
    carro2 = Carro("Carro 2")
    carro3 = Carro("Carro 3")

    # Colocar los carros en una lista
    carros_en_interseccion = [carro1, carro2, carro3]

    # Crear un objeto Semaforo para la intersección
    semaforo = Semaforo(interseccion)

    # Crear un proceso para controlar el semáforo y el cruce de carros
    proceso = multiprocessing.Process(target=semaforo.controlar, args=(carros_en_interseccion,))

    # Iniciar el proceso
    proceso.start()

    # Esperar a que el proceso termine
    proceso.join()