programa {
  funcao inicio() {

    inteiro n1, n2, n3, n4, n5

    escreva("Digite 5 números inteiros entre 0 e 10\n")
    escreva("Digite o primeiro número: ")
    leia(n1)
    escreva("Digite o segundo número: ")
    leia(n2)
    escreva("Digite o terceiro número: ")
    leia(n3)
    escreva("Digite o quarto número: ")
    leia(n4)
    escreva("Digite o quinto número: ")
    leia(n5)

    escreva("Segue abaixo os números pares que você digitou:\n")
    se (n1 % 2 == 0) {escreva (n1,"\n")}
    se (n2 % 2 == 0) {escreva (n2,"\n")}
    se (n3 % 2 == 0) {escreva (n3,"\n")}
    se (n4 % 2 == 0) {escreva (n4,"\n")}
    se (n5 % 2 == 0) {escreva (n5,"\n")}

}
"Escreva um algoritmo do tipo Pseudocódigo que pergunte ao usuário 5 números inteiros entre 0 e 10 e imprima cada um deles que seja par.