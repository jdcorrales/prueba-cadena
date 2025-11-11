from fastapi.testclient import TestClient
import sys
import os

from app.main import app

from app.prime_utils import PrimeUtils


class TestPrimeUtils:
    client = TestClient(app)

    prime_utils = PrimeUtils()

    def test_sum_primes_basic(self):
        """Prueba básica de la función sum_primes."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.prime_utils.sum_primes(numbers)
        assert result == 17

    def test_sum_primes_empty_list(self):
        """Debe devolver 0 si la lista está vacía."""
        assert self.prime_utils.sum_primes([]) == 0

    def test_sum_primes_invalid_input(self):
        """Debe lanzar ValueError si la entrada no es válida."""
        try:
            self.prime_utils.sum_primes("no_lista")
        except ValueError as e:
            assert "lista de enteros" in str(e)
        else:
            assert False, "Se esperaba una excepción ValueError"

    def test_post_sum_primes_success(self):
        """Verifica que el endpoint /sum-primes funcione correctamente."""
        response = self.client.post("/sum-primes", json={"numbers": [2, 3, 5, 8, 10]})
        assert response.status_code == 200
        data = response.json()
        assert data["sum_of_primes"] == 10
        assert data["count"] == 5

    def test_post_sum_primes_invalid_body(self):
        """Verifica el manejo de errores para entradas inválidas."""
        response = self.client.post("/sum-primes", json={"numbers": ["a", "b", "c"]})
        assert response.status_code == 422  # Error de validación de Pydantic

    def test_post_sum_primes_large_list(self):
        """Prueba con una lista grande de números consecutivos."""
        large_list = list(range(1, 1001))
        response = self.client.post("/sum-primes", json={"numbers": large_list})
        assert response.status_code == 200
        data = response.json()
        assert "sum_of_primes" in data
        assert data["sum_of_primes"] > 0
