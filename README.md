# Melhor abetura para jogar no Termoo

Esse projeto tem como objetivo replicar o processo de [definição da melhor palavra de abertura para o Wordle](https://towardsdatascience.com/finding-the-best-wordle-opener-with-machine-learning-ce81331c5759), executada por Harrison Hoffman, mas utilizando a versão do jogo em português, chamada [Termoo](https://term.ooo/).

Poucas alterações foram necessárias, pois é alta a semelhança entre as versões em inglês e português. Destaca-se que as maiores modificações tiveram de ser executadas em uma etapa de preprocessamento, visto que a língua portuguesa utiliza caracteres que não pertencem ao ascii, como `á` ou `ç`.

As lista de palavras em português foi retirada diretamente do [repositório de palavras do Termo](https://github.com/fserb/pt-br), bastando uma filtragem das palavras que possuem 5 letras.

## Referências:

[Best Opener Wordle](https://github.com/hfhoffman1144/Best-Wordle-Opener-ML)

[Repositório de palavras Termoo](https://github.com/fserb/pt-br)
