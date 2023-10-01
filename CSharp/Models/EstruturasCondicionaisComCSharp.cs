
//OBS: Abaixo está somente a parte essencial do código. 
// Não sendo possivel compilar do modo que está(compilando apenas no emulador da DIO)

/*O programa deve verificar duas condições principais:

1. Validade do ID: O ID de teste deve ser um número inteiro.
2. Comprimento da Descrição: A descrição do teste deve ter menos de 50 caracteres.*/




// Aqui é solicitado ao usuário que insira o ID do teste:
int idTeste;
      if (int.TryParse(Console.ReadLine(), out idTeste)) {
        // Solicita ao usuário que insira a descrição do teste:
        string descricaoTeste = Console.ReadLine();

        // Verifica se o ID do teste é válido e a descrição está dentro dos limites:
        if (idTeste > 0 && descricaoTeste.Length <= 50) {
          // TODO: Adicione um Console.WriteLine para verificar se o ID do teste é válido e a descrição está dentro dos limites:
          // TODO: Lembre-se: ID de teste valido. e Descricao valida. 
          Console.WriteLine("ID de teste valido.\nDescricao valida.");

        } else {
          //TODO: Adicione um Console.WriteLine para verificar se o ID do teste é válido:
          //TODO: Lembre-se da validação solicitada na descrição do desafio.
          Console.WriteLine("ID de teste invalido ou descricao muito longa.");

        }
      } else {
        Console.WriteLine("ID de teste invalido.");
      }