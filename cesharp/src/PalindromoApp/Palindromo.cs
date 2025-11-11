using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace PalindromoApp
{
    public static class Palindromo
    {
        public static bool EsPalindromo(string texto)
        {
            if (string.IsNullOrWhiteSpace(texto))
                throw new ArgumentException("La cadena no puede estar vacía o ser nula.");

            // Eliminar espacios, puntuación y pasar a minúsculas
            string limpio = Regex.Replace(texto.ToLowerInvariant(), @"[^a-z0-9]", "");

            // Comparar la cadena con su reverso
            return limpio.SequenceEqual(limpio.Reverse());
        }
    }
}
