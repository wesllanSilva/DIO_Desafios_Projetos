
//OBS: Abaixo está somente a parte essencial do código. 
// Não sendo possivel compilar do modo que está(compilando apenas no emulador da DIO)

/*objetivo é criar um algoritmo que avalie o desempenho de testes automatizados. 
O algoritmo deve receber como entrada o número de testes automatizados bem-sucedidos e o número total de testes automatizados realizados. 
Com base nessas informações, ele determinará a taxa de sucesso do teste.*/

using System;

namespace AvaliacaoTestesAutomatizados {
  class Program {
    static void Main(string[] args) {
      // Solicita ao usuário a entrada para o número de testes passados
      int testesPassados = Convert.ToInt32(Console.ReadLine());

      // Solicita ao usuário a entrada para o número total de testes
      int totalTestes = Convert.ToInt32(Console.ReadLine());

      // TODO: Calcule a taxa de sucesso e armazená-la na variável taxaSucesso:
      double taxaSucesso = ((double)testesPassados / totalTestes) * 100;
      // Exibe a taxa de sucesso com 2 casas decimais
      Console.WriteLine($"Taxa de sucesso: {taxaSucesso:F2}%");
    }
  }
}