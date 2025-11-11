using System;

namespace PalindromoApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Ingrese una cadena para verificar si es un palíndromo:");
            string input = Console.ReadLine();

            try
            {
                bool result = Palindromo.EsPalindromo(input);
                Console.WriteLine(result);
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
