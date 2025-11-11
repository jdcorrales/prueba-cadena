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

# Ejecutar la aplicación dentro del contenedor

```bash
docker-compose run cesharp-app
```

# Ejecutar los tests dentro del contenedor

```bash
docker-compose run cesharp-app dotnet test tests/PalindromoApp.Tests
```
---

## Servicios de AWS y Conceptos de Desarrollo desde la Perspectiva de un Desarrollador

1. Describe las diferencias entre Amazon RDS y Amazon DynamoDB. Proporciona casos de uso en los que cada servicio sería más apropiado desde la perspectiva de un desarrollador.

# 🆚 Comparativa: Amazon RDS vs Amazon DynamoDB

| 🌟 **Característica** | 🗃️ **Amazon RDS (Relacional)** | ⚡ **Amazon DynamoDB (NoSQL)** |
|------------------------|--------------------------------|--------------------------------|
| 🧩 **Tipo de base de datos** | Relacional (SQL) | NoSQL (clave-valor / documento) |
| 🧱 **Modelo de datos** | Tablas, filas y columnas con relaciones | Claves y atributos flexibles (sin relaciones) |
| 💬 **Lenguaje de consulta** | SQL (consultas complejas, joins, subconsultas) | API con operaciones básicas (`GetItem`, `PutItem`, `Query`, `Scan`) |
| 📜 **Esquema** | Fijo y estructurado | Flexible y dinámico |
| 🔒 **Transacciones** | Totalmente ACID (Atomicity, Consistency, Isolation, Durability)(consistentes y atómicas) | ACID limitadas, introducidas en 2019 |
| ⚖️ **Consistencia** | Siempre fuerte (ACID) | Eventual o fuerte opcional |
| 📈 **Escalabilidad** | Vertical (aumentar tamaño de instancia o réplicas) | Horizontal automática y sin intervención manual |
| ⚡ **Rendimiento** | Milisegundos altos (depende del hardware y consultas) | Milisegundos bajos o microsegundos con **DAX** |
| 🧰 **Administración** | Requiere mantenimiento (backups, actualizaciones, monitoreo) | Casi sin mantenimiento (**serverless**) |
| 💰 **Costo** | Basado en tipo de instancia y almacenamiento | Basado en capacidad provisionada o bajo demanda |
| 🧠 **Casos de uso ideales** | ERP, CRM, sistemas financieros, gestión de inventarios | Juegos, IoT, e-commerce, sesiones de usuario, catálogos |
| ⚙️ **Motores soportados** | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server | Motor propietario de AWS |

## Casos de uso
🧠 Amazon RDS (Relacional)

✔️ Cuando se necesita integridad referencial.
✔️ Cuando se maneja una alta transaccionalidad.
✔️ Cuand se necesita desarrollar aplicaciones atómicas.

Ejemplo: Desarrollo de sistemas bancarios, de nómina, ERP, CRM donde las transacciones deben ser totalmente consistentes y autidables.

⚡ Amazon DynamoDB (NoSQL)
✔️ Cuando se requiere una escalabilidad y baja latencia con datos simples y acceso rápido
✔️ Idela para aplicaciones moviles, IoT, catálogos de productos o sistemas de sesiones.
✔️ Cuando la estructura de los datos es flexible o cambio con frecuencia

Ejemplo: Desarrollo de una aplicación de comercio electrónico que maneja muchos productos y sesiones simultaneas, que necesita rapidez más que consistencia relacional.



