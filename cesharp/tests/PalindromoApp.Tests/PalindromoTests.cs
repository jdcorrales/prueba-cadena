using Xunit;
using PalindromoApp;
using System;

namespace PalindromoApp.Tests
{
    public class PalindromoTests
    {
        [Theory]
        [InlineData("A man a plan a canal Panama", true)]
        [InlineData("racecar", true)]
        [InlineData("No lemon, no melon", true)]
        [InlineData("Hello World", false)]
        public void EsPalindromo_DeberiaDevolverResultadoCorrecto(string texto, bool esperado)
        {
            bool resultado = Palindromo.EsPalindromo(texto);
            Assert.Equal(esperado, resultado);
        }

        [Fact]
        public void EsPalindromo_EntradaVacia_DeberiaLanzarExcepcion()
        {
            Assert.Throws<ArgumentException>(() => Palindromo.EsPalindromo(""));
        }
    }
}
