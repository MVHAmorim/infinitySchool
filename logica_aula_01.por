programa {
  funcao inicio() {

    inteiro n1, n2, n3, n4, n5

    escreva("Digite 5 n�meros inteiros entre 0 e 10\n")
    escreva("Digite o primeiro n�mero: ")
    leia(n1)
    escreva("Digite o segundo n�mero: ")
    leia(n2)
    escreva("Digite o terceiro n�mero: ")
    leia(n3)
    escreva("Digite o quarto n�mero: ")
    leia(n4)
    escreva("Digite o quinto n�mero: ")
    leia(n5)

    escreva("Segue abaixo os n�meros pares que voc� digitou:\n")
    se (n1 % 2 == 0) {escreva (n1,"\n")}
    se (n2 % 2 == 0) {escreva (n2,"\n")}
    se (n3 % 2 == 0) {escreva (n3,"\n")}
    se (n4 % 2 == 0) {escreva (n4,"\n")}
    se (n5 % 2 == 0) {escreva (n5,"\n")}

}
"Escreva um algoritmo do tipo Pseudoc�digo que pergunte ao usu�rio 5 n�meros inteiros entre 0 e 10 e imprima cada um deles que seja par.