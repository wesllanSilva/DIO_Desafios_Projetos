//OBS: Abaixo está somente a parte essencial do código. 
// Não sendo possivel compilar do modo que está(compilando apenas no emulador da DIO)


/*O programa solicitará ao usuário que insira a quantidade de testes bem-sucedidos 
e a quantidade total de testes realizados. 
Em seguida, o programa calculará a taxa de sucesso dos testes 
e aplicará os s critérios para determinar se a funcionalidade está pronta para ser lançada:*/



// Solicita ao usuário a quantidade de testes bem-sucedidos:
int testesBemSucedidos = int.Parse(Console.ReadLine());

// Solicita ao usuário a quantidade de testes totais:
int testesTotais = int.Parse(Console.ReadLine());

// TODO: Implemente as condições para o cálculo da taxa de sucesso:
double taxaSucesso = ((double)testesBemSucedidos / testesTotais) * 100;
// TODO: Implemente uma estrutura condicional (if/else) para avaliar a taxa de sucesso e tomar decisões com base nela:
if (taxaSucesso >= 80.0)
{
Console.WriteLine("A funcionalidade esta pronta para lancamento.");
}
else
{
Console.WriteLine("A funcionalidade nao esta pronta para lancamento.");
}