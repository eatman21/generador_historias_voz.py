# Cuentacuentos Mágico 🎭

Un generador de historias mágicas con narración por voz.

## Descripción

Este proyecto es un generador de historias aleatorias que combina diferentes elementos (personajes, lugares y objetos mágicos) para crear cuentos únicos. Además, incluye la funcionalidad de narración por voz utilizando pyttsx3.

## Características

- Generación aleatoria de historias
- Narración por voz
- Personalización de la velocidad de voz
- Múltiples voces disponibles
- Guardado de historias generadas

## Requisitos

- Python 3.x
- pyttsx3

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/eatman21/generador_historias_voz.py.git
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el programa principal:

```bash
python generador_historias_voz.py
```

## Estructura del Proyecto

```
cuentacuentos-magico/
├── generador_historias_voz.py     # Archivo principal
├── README.md                      # Documentación
├── requirements.txt               # Dependencias
├── datos/                         # Carpeta para elementos de historias
│   ├── personajes.txt
│   ├── lugares.txt
│   └── objetos.txt
└── historias_generadas/           # Para guardar historias
```

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios que te gustaría hacer.

## Licencia

Este proyecto está bajo la Licencia MIT.
