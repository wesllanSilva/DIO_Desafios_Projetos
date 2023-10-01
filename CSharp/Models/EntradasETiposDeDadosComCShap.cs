
//OBS: Abaixo está somente a parte essencial do código. 
// Não sendo possivel compilar do modo que está(compilando apenas no emulador da DIO)


/*Neste desafio, vamos criar um programa que simula um algoritmo para registrar falhas em testes de um sistema. 
O programa solicitará ao usuário que insira o nome do teste e a descrição do erro correspondente. 
Em seguida, ele exibirá uma mensagem do erro formatado
*/

using System;

namespace SimulacaoFalhaTeste {
  class Program {
    static void Main(string[] args) {
     string teste = Console.ReadLine();
      string descricaoDoErro = Console.ReadLine();
      Console.WriteLine($"O teste falhou. Descricao: {descricaoDoErro}");
    }
  }
}