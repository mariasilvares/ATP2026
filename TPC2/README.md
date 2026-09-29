# TPC2: Adivinha o Número

**Autor(a):** 
- Maria Silvares
- A114934
  
<img width="15%" height="2892" alt="IMG_1584" src="https://github.com/user-attachments/assets/2fa200fc-36b7-4502-90eb-4ac90d1965ac" />


**Resumo:** Neste trabalho foi desenvolvido, em Python, o jogo “Adivinha o número”, com as duas modalidades propostas no enunciado. O utilizador começa por escolher a modalidade através do `input()`. Na primeira modalidade, o computador pensa num número inteiro entre 0 e 100, gerado através da biblioteca `random`, e o utilizador tenta adivinhá-lo. Utilizando um ciclo `while` e estruturas condicionais `if`, `elif` e `else`, o programa verifica cada tentativa e informa se o número pensado é maior, menor ou se o utilizador acertou. O número de tentativas é contado através de uma variável. Na segunda modalidade, o utilizador pensa num número entre 0 e 100 e o computador tenta adivinhá-lo. O computador gera as suas tentativas com `random` e, através das respostas do utilizador — “Acertou”, “O número que pensei é Maior” ou “O número que pensei é Menor” — vai ajustando os valores mínimo e máximo do intervalo de procura. O ciclo `while` continua até o computador descobrir o número. Em ambas as modalidades, quando o número é descoberto, o programa termina e apresenta o número de tentativas utilizadas, cumprindo os requisitos definidos no enunciado.
