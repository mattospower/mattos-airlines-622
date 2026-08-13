# Imagens dos destinos

O site já está pronto para usar fotos reais — só falta baixar e salvar
na pasta `img/` com esses nomes exatos (o HTML já aponta pra eles):

| Arquivo               | Cidade          | Sugestão de busca                          |
|------------------------|-----------------|---------------------------------------------|
| `img/lisboa.jpg`       | Lisboa          | Torre de Belém ao pôr do sol                 |
| `img/nova-york.jpg`    | Nova York       | Skyline de Nova York / Central Park          |
| `img/toquio.jpg`       | Tóquio          | Monte Fuji com a skyline de Tóquio           |
| `img/buenos-aires.jpg` | Buenos Aires    | Obelisco de Buenos Aires ao entardecer       |
| `img/londres.jpg`      | Londres         | Big Ben e o Tâmisa ao entardecer             |
| `img/cidade-do-cabo.jpg` | Cidade do Cabo | Table Mountain com o oceano                  |

## Onde baixar (uso livre, sem pagar e sem precisar dar crédito)

Unsplash e Pixabay liberam as fotos para uso comercial e pessoal sem
exigir atribuição (mas é sempre educado citar o fotógrafo se quiser).

- **Lisboa:** https://unsplash.com/s/photos/torre-de-belem
- **Nova York:** https://unsplash.com/s/photos/new-york-skyline
- **Tóquio:** https://unsplash.com/s/photos/mount-fuji-tokyo
- **Buenos Aires:** https://unsplash.com/s/photos/buenos-aires-obelisco
- **Londres:** https://unsplash.com/s/photos/big-ben
- **Cidade do Cabo:** https://unsplash.com/s/photos/table-mountain

Se não achar o que quer no Unsplash, procure o mesmo termo em
https://pixabay.com ou https://www.pexels.com — mesma regra de uso livre.

## Como baixar e usar

1. Abra o link, escolha uma foto **na orientação paisagem** (mais larga
   que alta) e com boa resolução (pelo menos 1200px de largura).
2. Clique em "Download" (no Unsplash, escolha o tamanho "Medium" ou
   "Large" — não precisa do arquivo original gigante).
3. Renomeie o arquivo baixado exatamente como na tabela acima
   (ex: `lisboa.jpg`) e mova para a pasta `img/` do projeto.
4. Pronto — o site já vai carregar a foto automaticamente em três
   lugares: no card da home, no topo da página do destino e na
   miniatura do checkout.

Se o arquivo baixado for `.png` ou `.webp` em vez de `.jpg`, funciona
igual — só troque a extensão no nome do arquivo E também dentro dos
arquivos `.html` (procure por `.jpg` e troque, ou me avise que eu ajusto).

## Se preferir não baixar imagens agora

Sem problema — o site já tem um degradê de cor bonito (que imita o tom
de cada foto) como fundo de cada card e foto, então ele funciona e fica
apresentável mesmo sem nenhuma imagem na pasta `img/`.
