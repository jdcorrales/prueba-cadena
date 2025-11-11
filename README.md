# Prueba técnica CADENA S.A.S

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/jdcorrales/prueba-cadena.git
```

2️⃣ Construir y ejecutar el contenedor

```bash
docker-compose up --build
```

---
# 1. Python Exercise:
Write a Python function that takes a list of integers and returns the sum of all prime numbers in the list. Additionally, the function should handle large lists efficiently and include error handling for invalid inputs.
Example:
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 17

## 📘 Descripción

La aplicación es un servicio REST desarrollado con **FastAPI**, que recibe una lista de números enteros y devuelve la **suma de todos los números primos** de dicha lista.

El proyecto está **contenedorizado con Docker Compose** y está optimizado para manejar **listas grandes** de manera eficiente mediante el uso de:
- **Criba de Eratóstenes (Sieve of Eratosthenes)** para rangos amplios consecutivos.
- **Procesamiento concurrente** con `ThreadPoolExecutor` para listas dispersas.
- **Validación y manejo de errores** con FastAPI y Pydantic.

---

## 🚀 Características principales

✅ API REST construida con **FastAPI**
✅ Optimización para grandes volúmenes de datos
✅ Manejo automático de errores y validaciones
✅ Documentación interactiva con **Swagger UI**
✅ Ejecutable fácilmente con **Docker Compose**

---

🌐 Uso de la API python

ingresa al navegador web y ve a la url

👉 http://localhost:5000/docs

Allí encontrarás la documentación generada automáticamente por FastAPI (Swagger UI).

📤 Ejemplo de solicitud

Método: POST
Ruta: /sum-primes

Cuerpo (JSON):

{
  "numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}


Respuesta esperada:

{
  "sum_of_primes": 17,
  "count": 10
}

### Pruebas usando CLI

```bash
curl -X POST "http://localhost:5000/sum-primes" \
  -H "Content-Type: application/json" \
  -d '{"numbers":[1,2,3,4,5,6,7,8,9,10]}'
```

### Ejecutar TEST
```bash
docker-compose run python-app pytest
```

---

# 2. C\# Exercise:
Write a C\# program that reads a string from the console and determines if it is a palindrome (a word, phrase, or sequence that reads the same backward as forward). The program should ignore spaces, punctuation, and case sensitivity. Additionally, the program should handle large strings efficiently and include error handling for invalid inputs.
Example:
Input: "A man a plan a canal Panama"
Output: True

---
🧠 PalindromoApp

Aplicación en C# (.NET 8) que permite verificar si una palabra o frase es un palíndromo.
Incluye un conjunto de pruebas unitarias automatizadas usando xUnit.

1️⃣ Ejecutar la aplicación dentro del contenedor

```bash
docker-compose run cesharp-app
```

2️⃣ Ejecutar los tests dentro del contenedor

```bash
docker-compose run cesharp-app dotnet test tests/PalindromoApp.Tests
```