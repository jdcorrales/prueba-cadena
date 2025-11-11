from concurrent.futures import ThreadPoolExecutor
import math

class PrimeUtils:

    def is_prime(self, n: int) -> bool:
        """Verifica si un número es primo (para valores grandes no consecutivos)."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        r = int(math.sqrt(n))
        for i in range(5, r + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def sieve_sum_primes(self, numbers: list[int]) -> int:
        """Suma de primos optimizada para listas grandes consecutivas."""
        if not numbers:
            return 0

        max_n = max(numbers)
        if max_n < 2:
            return 0

        sieve = [True] * (max_n + 1)
        sieve[0:2] = [False, False]
        for i in range(2, int(math.sqrt(max_n)) + 1):
            if sieve[i]:
                sieve[i*i:max_n+1:i] = [False] * len(range(i*i, max_n+1, i))

        primes_set = {i for i, is_p in enumerate(sieve) if is_p}
        return sum(n for n in numbers if n in primes_set)

    def sum_primes(self, numbers: list[int]) -> int:
        """Detecta automáticamente el mejor método de cálculo."""
        if not isinstance(numbers, list):
            raise ValueError("La entrada debe ser una lista de enteros.")

        if not all(isinstance(x, int) for x in numbers):
            raise ValueError("Todos los elementos deben ser números enteros.")

        n = len(numbers)

        # Para listas pequeñas o dispersas, usamos hilos
        if n < 100_000:
            with ThreadPoolExecutor() as executor:
                results = executor.map(lambda x: x if self.is_prime(x) else 0, numbers)
                return sum(results)
        else:
            # Para listas muy grandes, usamos la criba
            return self.sieve_sum_primes(numbers)