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

---

2. ¿Qué es AWS Lambda y cómo respalda la computación sin servidor (serverless)?
Proporciona un ejemplo de una aplicación sin servidor usando AWS Lambda con fragmentos de código.

Es un servicio de computación sin servidor (serverless) que permite ejecutar código sin aprovisionar ni administrar servidores.

Solo escribes tu función y AWS se encarga de:

* Ejecutarla bajo demanda.
* Escalar automáticamente según la carga.
* Cobrarte solo por el tiempo de ejecución (en milisegundos) y la memoria usada.

La arquitectura serverless se basa en eventos. En lugar de mantener servidores encendidos, el código se ejecuta únicamente cuando ocurre un evento desencadenante (trigger), como:

* Una solicitud HTTP (API Gateway).
* Un nuevo archivo en S3.
* Un mensaje en una cola SQS o SNS.
* Un cambio en una tabla DynamoDB.
* Un evento programado (CloudWatch Events).

Con esto:

* No pagas por servidores inactivos.
* Escala automáticamente según la demanda.
* Reduces mantenimiento (no hay parches, ni administración de infraestructura).

### Ejemplo:

La aplicación implementa un **backend sin servidor (serverless)** usando:

- **AWS Lambda:** ejecuta la lógica del backend.
- **Amazon API Gateway:** expone la API REST al público.
- **Amazon DynamoDB:** almacena los datos de usuarios.

## 🧱 Arquitectura

Cliente HTTP

↓

Amazon API Gateway (endpoint REST)

↓

AWS Lambda (ejecuta la lógica del backend)

↓

Amazon DynamoDB (guarda los datos)

1. El cliente envía una solicitud HTTP (`POST` o `GET`) a la API.
2. API Gateway invoca la función **Lambda**.
3. Lambda procesa la solicitud y lee/escribe en **DynamoDB**.
4. Lambda devuelve una respuesta JSON al cliente.

## 🧩 Código de la función Lambda (Python)

```python
import json
import boto3
from datetime import datetime

# Conexión a DynamoDB
dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('Usuarios')

def lambda_handler(event, context):
    # Determinar método HTTP
    metodo = event['httpMethod']

    if metodo == 'POST':
        body = json.loads(event['body'])
        usuario = {
            'id': body['id'],
            'nombre': body['nombre'],
            'fecha_registro': datetime.utcnow().isoformat()
        }
        tabla.put_item(Item=usuario)
        return {
            'statusCode': 201,
            'body': json.dumps({'mensaje': 'Usuario creado', 'usuario': usuario})
        }

    elif metodo == 'GET':
        id_usuario = event['queryStringParameters']['id']
        respuesta = tabla.get_item(Key={'id': id_usuario})
        return {
            'statusCode': 200,
            'body': json.dumps(respuesta.get('Item', {}))
        }

    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Método no soportado'})
        }
```

Configuración en AWS
1. Crear una tabla DynamoDB

Nombre de la tabla: Usuarios

Clave primaria: id (Tipo: String)

2. Crear la función Lambda

Runtime: Python 3.9

Rol IAM: permisos de acceso a DynamoDB (AmazonDynamoDBFullAccess)

Subir el código anterior o editarlo directamente en la consola de AWS.

3. Crear una API en Amazon API Gateway

Crear una API REST.

Recurso: /usuarios

Métodos: POST y GET

Integración: Lambda Function

Implementar y desplegar (Deploy API).

🧪 Pruebas con cURL
➕ Crear usuario (POST)
``` bash
curl -X POST https://tu-api.amazonaws.com/usuarios \
-H "Content-Type: application/json" \
-d '{"id": "001", "nombre": "User Name"}'
```

🔍 Consultar usuario (GET)
``` bash
curl "https://tu-api.amazonaws.com/usuarios?id=001"
```

---
3. Explica el concepto de DevOps y su importancia en el desarrollo moderno de software.
Describe las prácticas y herramientas clave utilizadas en DevOps, enfocándote en los servicios de AWS como AWS CodeCommit, AWS CodeBuild, AWS CodeDeploy y AWS CodePipeline.

# ⚙️ DevOps y su importancia en el desarrollo moderno de software

## 🧠 ¿Qué es DevOps?

**DevOps** es una filosofía y conjunto de prácticas que **integran el desarrollo de software (Dev)** y las **operaciones de TI (Ops)** con el objetivo de mejorar la **colaboración**, **automatización**, **velocidad de entrega** y **calidad** del software.

Su propósito es **romper las barreras tradicionales** entre los equipos de desarrollo y operaciones, permitiendo entregar aplicaciones más rápido, con menos errores y respondiendo de forma ágil a las necesidades del negocio.

---

## 🚀 Importancia de DevOps en el desarrollo moderno

En el contexto actual, donde las organizaciones requieren actualizaciones continuas y despliegues rápidos, DevOps ofrece:

| Beneficio | Descripción |
|------------|-------------|
| ⚡ **Entrega continua (Continuous Delivery)** | Permite lanzar nuevas versiones de software de forma frecuente y confiable. |
| 🧩 **Colaboración mejorada** | Une equipos antes aislados (desarrollo, QA, operaciones) bajo objetivos comunes. |
| 🔄 **Automatización** | Reduce errores humanos al automatizar compilación, pruebas y despliegues. |
| 🧠 **Monitoreo constante** | Facilita la detección temprana de fallos y el aprendizaje continuo. |
| 💰 **Eficiencia en costos y tiempo** | Menos tiempo invertido en tareas manuales y más foco en innovación. |

DevOps no es una herramienta, sino una **cultura apoyada por procesos automatizados** y un conjunto de servicios tecnológicos.

---

## 🧰 Prácticas clave de DevOps

| Práctica | Descripción |
|-----------|-------------|
| **Integración continua (CI)** | Los desarrolladores integran código frecuentemente en un repositorio compartido donde se ejecutan pruebas automáticas. |
| **Entrega continua (CD)** | Automatiza el despliegue del código validado hacia entornos de producción o preproducción. |
| **Infraestructura como código (IaC)** | La infraestructura se gestiona y aprovisiona mediante archivos de configuración (ej. AWS CloudFormation, Terraform). |
| **Monitoreo y retroalimentación** | Se observan métricas y logs para optimizar rendimiento, seguridad y experiencia del usuario. |
| **Automatización de pruebas** | Cada cambio se valida mediante pruebas unitarias, de integración y funcionales. |

---

## ☁️ Herramientas de AWS para DevOps

AWS proporciona un conjunto completo de servicios administrados que facilitan la implementación de prácticas DevOps:

### 1. 🧾 **AWS CodeCommit**
> Sistema de control de versiones privado y seguro basado en **Git**, administrado por AWS.

- Permite almacenar y versionar el código fuente.
- Integra permisos y autenticación con AWS IAM.
- Ideal para equipos distribuidos.

**Ejemplo de uso:**
```bash
git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/mi-repositorio
git add .
git commit -m "Primera versión"
git push origin main
```

### 2. 🏗️ AWS CodeBuild
> Servicio de compilación y pruebas automatizadas que genera artefactos listos para desplegar.

- Ejecuta tareas de build dentro de contenedores gestionados.
- Compatible con múltiples lenguajes (Python, Java, Node.js, C#, etc.).
- Se integra fácilmente con CodeCommit, CodePipeline o GitHub.
**Ejemplo de uso (buildspec.yml)**
``` yaml
version: 0.2
phases:
  install:
    commands:
      - echo "Instalando dependencias..."
      - pip install -r requirements.txt
  build:
    commands:
      - echo "Ejecutando pruebas..."
      - pytest
artifacts:
  files:
    - '**/*'
```
### 3. 🚀 AWS CodeDeploy
> Automatiza el despliegue de aplicaciones en distintos entornos:
- Instancias EC2
- Clústeres ECS
- AWS Lambda
- Servidores on-premise
Permite actualizaciones sin tiempo de inactividad (deployments blue/green o rolling).

**Ejemplo de configuración (appspec.yml)**
``` yaml
version: 0.0
os: linux
files:
  - source: /
    destination: /var/www/html
hooks:
  AfterInstall:
    - location: scripts/restart_server.sh
      timeout: 180
      runas: root
```

### 🔄 AWS CodePipeline
> Servicio que orquesta todo el flujo CI/CD, conectando CodeCommit, CodeBuild y CodeDeploy.

Cada cambio en el repositorio desencadena automáticamente una serie de etapas:

- CodeCommit: Detecta el cambio de código.
- CodeBuild: Compila y prueba el código.
- CodeDeploy: Despliega la nueva versión.

**Ejemplo visual del flujo:**

[CodeCommit] → [CodeBuild] → [CodeDeploy] → [Producción]

---
4. Describe el proceso para configurar una tubería de integración y entrega continua (CI/CD) usando AWS CodePipeline y AWS CodeBuild.
Proporciona un ejemplo de cómo implementar (desplegar) una aplicación web usando estos servicios con fragmentos de código.

# Configuración de una tubería CI/CD con AWS CodePipeline y AWS CodeBuild para una aplicación Vue.js desplegada en Amazon S3

## 🧩 Introducción

Este flujo permite que cada cambio en el código fuente se compile, se pruebe y se despliegue automáticamente en un bucket de S3, donde se aloja la aplicación web estática de **Vue.js**.


## ⚙️ Arquitectura general del proceso CI/CD

1. **Repositorio del código fuente**: El código se almacena en **AWS CodeCommit**
2. **CodePipeline**: Orquesta el flujo de trabajo completo (fuente → build → despliegue).
3. **CodeBuild**: Compila y construye la aplicación Vue.js.
4. **Amazon S3**: Aloja los archivos estáticos generados (HTML, JS, CSS).
5. **Amazon CloudFront (opcional)**: Distribuye el contenido globalmente con caché y HTTPS.

---

## 🧱 Paso a paso para configurar la tubería CI/CD

### 1. Crear el bucket S3 para el hosting
```bash
aws s3 mb s3://mi-vue-app-bucket
aws s3 website s3://mi-vue-app-bucket/ --index-document index.html --error-document index.html
```

Habilita el acceso público o configura una distribución de CloudFront para servir la aplicación.

### 2. Configurar el archivo buildspec.yml para AWS CodeBuild

Dentro del proyecto Vue, crea el archivo buildspec.yml en la raíz del repositorio. Este archivo define las fases de compilación y despliegue.

``` yaml
version: 0.2

phases:
  install:
    runtime-versions:
      nodejs: 18
    commands:
      - echo "Instalando dependencias..."
      - npm install
  build:
    commands:
      - echo "Construyendo la aplicación Vue..."
      - npm run build
  post_build:
    commands:
      - echo "Copiando archivos al bucket S3..."
      - aws s3 sync dist/ s3://mi-vue-app-bucket/ --delete
artifacts:
  files:
    - '**/*'
  base-directory: dist
```
### 3. Crear un proyecto de CodeBuild
En la consola de AWS CodeBuild:

- Selecciona Create Build Project.
- Fuente: CodeCommit.
- Entorno de build: “Managed image” → Ubuntu → Node.js runtime.
- Agrega permisos para acceder a S3.
- Especifica el archivo buildspec.yml.

El rol IAM del proyecto debe incluir permisos como:
``` json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:*"],
      "Resource": ["arn:aws:s3:::mi-vue-app-bucket/*"]
    }
  ]
}
```

### 4. Crear la tubería en AWS CodePipeline

En la consola de AWS CodePipeline:

Paso 1 – Fuente
 - Elige el proveedor CodeCommit.
 - Conecta el repositorio y la rama principal.

Paso 2 – Build
 - Selecciona el proyecto de CodeBuild creado anteriormente.

Paso 3 – Deploy
- Tipo: Amazon S3.
- Especifica el bucket mi-vue-app-bucket.

Cada vez que se haga un commit al repositorio, la tubería ejecutará automáticamente la construcción y despliegue.

🚀 Despliegue automático

Una vez configurado todo:

Cada push al repositorio activa CodePipeline.

CodeBuild instala dependencias, ejecuta npm run build y sincroniza con S3.

El sitio web se actualiza automáticamente en la URL de S3 o CloudFront.