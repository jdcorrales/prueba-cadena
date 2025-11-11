from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

from app.prime_utils import PrimeUtils

app = FastAPI(
    title="API - Suma de Números Primos",
    description="Servicio eficiente que calcula la suma de todos los números primos en una lista grande de enteros.",
    version="1.0.0"
)

# Definición del modelo datos de entrada
class NumbersRequest(BaseModel):
    numbers: List[int] = Field(
        ...,
        example=[1,2,3,4,5,6,7,8,9,10],
        description="Lista de números enteros para calcular la suma de los primos."
    )

# Definición del endpoint para ejecutar la suma de números primos
@app.post("/sum-primes")
def calculate_sum_primes(request: NumbersRequest):
    # Crear una instancia de PrimeUtils
    prime_utils = PrimeUtils()

    try:
        # Calcular la suma de números primos usando PrimeUtils
        result = prime_utils.sum_primes(request.numbers)
        # Retornar el resultado y la cantidad de números procesados
        return {"sum_of_primes": result, "count": len(request.numbers)}
    except ValueError as e:
        # Manejar errores de validación y devolver una respuesta HTTP adecuada
        raise HTTPException(status_code=400, detail=str(e))