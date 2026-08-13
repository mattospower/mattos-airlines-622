# Mattos Airlines ✈

Site fictício de uma companhia aérea, feito como trabalho prático de Desenvolvimento Web Front-End.

**Tema:** e-commerce fictício — venda de passagens aéreas.

🔗 **Site publicado:** _adicione aqui o link do GitHub Pages / Netlify / Vercel depois do deploy_

## Stack

Apenas **HTML5 semântico** e **CSS3** puro. Nenhuma linha de JavaScript é executada no navegador — inclusive os elementos que parecem "interativos" (alternância do tipo de viagem, carrossel de fotos) usam apenas recursos nativos de HTML/CSS:

- o carrossel de fotos das páginas de destino usa `overflow-x` + `scroll-snap` + links de âncora (`<a href="#slide-2">`) — não precisa de JS para deslizar entre as fotos;
- a alternância "Ida e volta / Somente ida / Múltiplos destinos" usa `<input type="radio">` nativo, estilizado com `accent-color` e o seletor `:checked`.

## Estrutura

```
mattos/
├── index.html                  → página inicial (obrigatória)
├── lisboa.html, toquio.html... → uma página por destino (6 no total)
├── checkout-lisboa.html...     → uma página de checkout por destino (6 no total)
├── css/
│   └── style.css               → todo o CSS do site, em arquivo externo
├── img/                        → pasta vazia — veja IMAGENS.md para
│                                   saber quais fotos baixar e como nomear
├── IMAGENS.md                  → guia com links para baixar as fotos
│                                   dos destinos (gratuitas, sem direitos
│                                   autorais) e instruções de uso
└── build_pages.py              → script local (Python) usado só para gerar as
                                   6 páginas de destino/checkout a partir de um
                                   template comum, evitando copiar e colar HTML
                                   repetido. Não roda no navegador — a saída
                                   final são arquivos .html estáticos comuns.
```

## Requisitos técnicos atendidos

- **HTML semântico:** `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, hierarquia de `<h1>`–`<h3>`, `alt` descritivo em imagens.
- **CSS Grid:** grade de cards de destino, grade do mapa de rotas, calendário do checkout, campos do formulário de busca.
- **Flexbox:** navegação, linha de rota (aeroporto → aeroporto), botões, resumo de preço.
- **Responsividade:** media queries para desktop, tablet e mobile — sem rolagem horizontal em nenhuma largura.
- **Design:** paleta escura + azul-sinal, tipografia Archivo / IBM Plex Mono / Inter (Google Fonts), cantos arredondados, sombras suaves, transições em botões e cards.

## Rodando localmente

Não precisa de build nem servidor — é só abrir `index.html` no navegador.
Se preferir servir localmente (recomendado para os links relativos funcionarem sem restrição de `file://`):

```bash
python3 -m http.server 8000
# depois acesse http://localhost:8000
```
