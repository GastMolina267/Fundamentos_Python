# 🐍 Tema 9: Pathlib en Python

## 📁 Introducción a Pathlib

Pathlib es una poderosa biblioteca en Python que proporciona una interfaz orientada a objetos para trabajar con rutas de archivos y directorios. Este módulo forma parte de la biblioteca estándar de Python desde la versión 3.4, ofreciendo una alternativa más intuitiva y segura a las funciones tradicionales de manejo de rutas.

## 🌟 Características principales

- **Orientado a objetos**: Trabaja con rutas como objetos en lugar de cadenas.
- **Multiplataforma**: Funciona de manera consistente en diferentes sistemas operativos.
- **Seguro**: Evita problemas comunes relacionados con la manipulación de cadenas.
- **Intuitivo**: Proporciona métodos claros y fáciles de usar para operaciones comunes.

## 🚀 ¿Qué aprenderás?

En esta sección, nos enfocamos en:

- 🔗 **Gestión de rutas y archivos**: Aprende a navegar, crear y manipular rutas de manera multiplataforma.
- 🗂 **Operaciones avanzadas**: Realiza operaciones como creación, lectura, modificación y eliminación de archivos con métodos elegantes y potentes.
- 🛠 **Manipulación multiplataforma**: Asegura que tu código funcione sin problemas en diferentes sistemas operativos.
- 💡 **Aplicación de la POO**: Descubre cómo `Pathlib` utiliza la Programación Orientada a Objetos para facilitar el manejo de rutas y archivos.

## 🛠️ Instalación

Pathlib viene incluido en Python 3.4+. No es necesaria ninguna instalación adicional.

```python
from pathlib import Path
```

## 🚀 Uso básico

```python
from pathlib import Path

# Crear una ruta
ruta = Path("carpeta/subcarpeta/archivo.txt")

# Obtener el nombre del archivo
print(ruta.name)  # Salida: archivo.txt

# Obtener la extensión
print(ruta.suffix)  # Salida: .txt

# Comprobar si existe
print(ruta.exists())  # Salida: True o False
```

## 📚 Temas cubiertos

1. Creación de rutas
2. Navegación por el sistema de archivos
3. Operaciones con archivos y directorios
4. Patrones de búsqueda (globbing)
5. Propiedades de archivos y directorios

## 🔗 Enlaces útiles

- [Documentación oficial de Pathlib](https://docs.python.org/3/library/pathlib.html)
- [Tutorial de Real Python sobre Pathlib](https://realpython.com/python-pathlib/)

## 🎯 ¿Por qué elegir `Pathlib`?

`Pathlib` es más que una simple herramienta; es una forma moderna y elegante de manejar rutas y archivos. Al utilizarlo, tu código será más limpio, mantenible y compatible con diferentes plataformas, sin sacrificar la funcionalidad.

## 🤝 Contribución

¡Tus contribuciones son bienvenidas! Si encuentras errores o tienes sugerencias para mejorar este README, no dudes en abrir un issue o enviar un pull request.

---

¡Feliz coding con Pathlib! 🎉
