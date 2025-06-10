import pyttsx3
import random
import time


class GeneradorHistorias:
    def __init__(self):
        # Inicializar el motor de texto a voz
        self.engine = pyttsx3.init()
        self.configurar_voz()

        # Elementos para generar historias
        self.personajes = [
            "un valiente caballero", "una sabia princesa", "un astuto ladrón",
            "una poderosa hechicera", "un noble rey", "una feroz dragona",
            "un humilde campesino", "una misteriosa anciana", "un joven aventurero",
            "una talentosa barda", "un sabio ermitaño", "una guerrera implacable"
        ]

        self.lugares = [
            "en un bosque encantado", "en un castillo abandonado", "en una cueva misteriosa",
            "en una ciudad flotante", "en las montañas nevadas", "en un desierto ardiente",
            "en una isla perdida", "en un pueblo fantasma", "en un reino submarino",
            "en una torre mágica", "en un laberinto antiguo", "en un jardín secreto"
        ]

        self.objetos_magicos = [
            "una espada brillante", "un amuleto dorado", "una poción misteriosa",
            "un libro de hechizos", "una llave de cristal", "un espejo mágico",
            "una capa invisible", "un anillo de poder", "una varita encantada",
            "una corona sagrada", "un medallón antiguo", "una gema resplandeciente"
        ]

        self.conflictos = [
            "debe rescatar a alguien importante", "necesita romper una maldición",
            "busca un tesoro perdido", "debe derrotar a un enemigo poderoso",
            "quiere restaurar la paz", "necesita encontrar la verdad",
            "debe proteger su hogar", "busca venganza por una injusticia",
            "quiere demostrar su valor", "debe cumplir una profecía",
            "necesita salvar el reino", "busca redimirse de sus errores"
        ]

        self.resoluciones = [
            "usando su inteligencia y astucia", "con la ayuda de nuevos amigos",
            "descubriendo un poder oculto", "haciendo un gran sacrificio",
            "aprendiendo una lección importante", "encontrando el coraje interior",
            "con perseverancia y determinación", "gracias a un acto de bondad",
            "superando sus miedos", "confiando en su corazón",
            "usando la magia de la amistad", "siendo fiel a sus valores"
        ]

    def configurar_voz(self):
        """Configura las propiedades de la voz"""
        voices = self.engine.getProperty('voices')

        # Intentar usar una voz en español si está disponible
        for voice in voices:
            if 'spanish' in voice.name.lower() or 'es' in voice.id.lower():
                self.engine.setProperty('voice', voice.id)
                break

        # Configurar velocidad y volumen
        self.engine.setProperty('rate', 150)    # Velocidad de habla
        self.engine.setProperty('volume', 0.9)  # Volumen

    def generar_historia(self):
        """Genera una historia aleatoria"""
        personaje = random.choice(self.personajes)
        lugar = random.choice(self.lugares)
        objeto = random.choice(self.objetos_magicos)
        conflicto = random.choice(self.conflictos)
        resolucion = random.choice(self.resoluciones)

        historia = f"""
        Había una vez {personaje} que vivía {lugar}.
        
        Un día, mientras exploraba, encontró {objeto} que cambiaría su destino para siempre.
        
        Pronto descubrió que {conflicto}, y esta seria la aventura más grande de su vida.
        
        Después de muchas pruebas y desafíos, nuestro héroe logró su objetivo {resolucion}.
        
        Y así, {personaje} se convirtió en una leyenda, y su historia se contó durante generaciones.
        
        Fin de la historia.
        """

        return historia.strip()

    def contar_historia(self, historia):
        """Narra la historia usando texto a voz"""
        print("🎭 Contando la historia...")
        print("-" * 50)
        print(historia)
        print("-" * 50)

        # Convertir texto a voz
        self.engine.say(historia)
        self.engine.runAndWait()

    def pausar_narracion(self):
        """Pausa entre secciones de la historia"""
        time.sleep(1)

    def cambiar_velocidad_voz(self, velocidad):
        """Cambia la velocidad de la voz (50-300)"""
        self.engine.setProperty('rate', velocidad)
        print(f"Velocidad de voz cambiada a: {velocidad}")

    def listar_voces_disponibles(self):
        """Muestra las voces disponibles en el sistema"""
        voices = self.engine.getProperty('voices')
        print("Voces disponibles:")
        for i, voice in enumerate(voices):
            print(f"{i}: {voice.name} - {voice.id}")

    def cambiar_voz(self, indice_voz):
        """Cambia la voz usando el índice de la lista"""
        voices = self.engine.getProperty('voices')
        if 0 <= indice_voz < len(voices):
            self.engine.setProperty('voice', voices[indice_voz].id)
            print(f"Voz cambiada a: {voices[indice_voz].name}")
        else:
            print("Índice de voz no válido")

    def crear_historia_personalizada(self):
        """Permite al usuario crear su propia historia"""
        print("\n📝 Creando tu historia personalizada...")
        print("\nPuedes elegir de las opciones disponibles o escribir tu propia idea.")

        # Mostrar opciones disponibles para cada elemento
        print("\nPersonajes disponibles:")
        for i, personaje in enumerate(self.personajes, 1):
            print(f"{i}. {personaje}")
        print("0. Escribir mi propio personaje")

        opcion = input("\nElige un número o escribe tu personaje: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(self.personajes):
            personaje = self.personajes[int(opcion)-1]
        else:
            personaje = opcion if opcion != "0" else input(
                "Escribe tu personaje: ").strip()

        print("\nLugares disponibles:")
        for i, lugar in enumerate(self.lugares, 1):
            print(f"{i}. {lugar}")
        print("0. Escribir mi propio lugar")

        opcion = input("\nElige un número o escribe tu lugar: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(self.lugares):
            lugar = self.lugares[int(opcion)-1]
        else:
            lugar = opcion if opcion != "0" else input(
                "Escribe tu lugar: ").strip()

        print("\nObjetos mágicos disponibles:")
        for i, objeto in enumerate(self.objetos_magicos, 1):
            print(f"{i}. {objeto}")
        print("0. Escribir mi propio objeto")

        opcion = input("\nElige un número o escribe tu objeto: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(self.objetos_magicos):
            objeto = self.objetos_magicos[int(opcion)-1]
        else:
            objeto = opcion if opcion != "0" else input(
                "Escribe tu objeto: ").strip()

        print("\nConflictos disponibles:")
        for i, conflicto in enumerate(self.conflictos, 1):
            print(f"{i}. {conflicto}")
        print("0. Escribir mi propio conflicto")

        opcion = input("\nElige un número o escribe tu conflicto: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(self.conflictos):
            conflicto = self.conflictos[int(opcion)-1]
        else:
            conflicto = opcion if opcion != "0" else input(
                "Escribe tu conflicto: ").strip()

        print("\nResoluciones disponibles:")
        for i, resolucion in enumerate(self.resoluciones, 1):
            print(f"{i}. {resolucion}")
        print("0. Escribir mi propia resolución")

        opcion = input("\nElige un número o escribe tu resolución: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(self.resoluciones):
            resolucion = self.resoluciones[int(opcion)-1]
        else:
            resolucion = opcion if opcion != "0" else input(
                "Escribe tu resolución: ").strip()

        historia = f"""
        Había una vez {personaje} que vivía {lugar}.
        
        Un día, mientras exploraba, encontró {objeto} que cambiaría su destino para siempre.
        
        Pronto descubrió que {conflicto}, y esta seria la aventura más grande de su vida.
        
        Después de muchas pruebas y desafíos, nuestro héroe logró su objetivo {resolucion}.
        
        Y así, {personaje} se convirtió en una leyenda, y su historia se contó durante generaciones.
        
        Fin de la historia.
        """

        return historia.strip()


def main():
    """Función principal del programa"""
    generador = GeneradorHistorias()

    print("🏰 ¡Bienvenido al Generador de Historias Mágicas! 🏰")
    print("=" * 60)

    while True:
        print("\n📖 Opciones disponibles:")
        print("1. Generar y contar una nueva historia")
        print("2. Solo generar historia (sin voz)")
        print("3. Cambiar velocidad de voz")
        print("4. Ver voces disponibles")
        print("5. Cambiar voz")
        print("6. Crear mi propia historia")
        print("7. Salir")

        opcion = input("\n¿Qué te gustaría hacer? (1-7): ").strip()

        if opcion == "1":
            print("\n🎲 Generando historia aleatoria...")
            historia = generador.generar_historia()
            generador.contar_historia(historia)

        elif opcion == "2":
            print("\n🎲 Generando historia aleatoria...")
            historia = generador.generar_historia()
            print("-" * 50)
            print(historia)
            print("-" * 50)

        elif opcion == "3":
            try:
                velocidad = int(
                    input("Ingresa la nueva velocidad (50-300, recomendado 150): "))
                if 50 <= velocidad <= 300:
                    generador.cambiar_velocidad_voz(velocidad)
                else:
                    print("Por favor ingresa un valor entre 50 y 300")
            except ValueError:
                print("Por favor ingresa un número válido")

        elif opcion == "4":
            generador.listar_voces_disponibles()

        elif opcion == "5":
            generador.listar_voces_disponibles()
            try:
                indice = int(
                    input("Ingresa el número de la voz que deseas usar: "))
                generador.cambiar_voz(indice)
            except ValueError:
                print("Por favor ingresa un número válido")

        elif opcion == "6":
            print("\n🎨 Creando tu historia personalizada...")
            historia = generador.crear_historia_personalizada()
            generador.contar_historia(historia)

        elif opcion == "7":
            print("¡Gracias por usar el Generador de Historias! 🌟")
            print("¡Que tengas aventuras mágicas! ✨")
            break

        else:
            print("Opción no válida. Por favor elige un número del 1 al 7.")

        # Pausa antes de mostrar el menú nuevamente
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n¡Programa interrumpido! ¡Hasta la vista! 👋")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
        print("Asegúrate de tener instalado pyttsx3: pip install pyttsx3")
