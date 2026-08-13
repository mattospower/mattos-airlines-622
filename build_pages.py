#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera as páginas estáticas de destino e checkout da Mattos Airlines.
Saída: apenas arquivos .html e .css — nenhum JavaScript é usado em runtime.
Este script é só uma ferramenta de build local para não copiar/colar 6x.
"""
import os

DEST_DIR = os.path.dirname(os.path.abspath(__file__))

destinos = [
    dict(
        slug="lisboa", cidade="Lisboa", ph="ph-lisboa", foto="lisboa.jpg",
        pais="Portugal", continente="Europa", rota="GRU → LIS",
        landmarks=["Torre de Belém", "Alfama", "Praça do Comércio", "Ponte 25 de Abril"],
        sobre="Lisboa combina arquitetura histórica, vistas para o Tejo e uma cena gastronômica vibrante. Ruas de paralelepípedos, elétricos amarelos e miradouros ao pôr do sol fazem da capital portuguesa um dos destinos mais procurados da Mattos Airlines.",
        preco=2190, reserve_ate="30 jul 2026", classe="Executiva",
    ),
    dict(
        slug="nova-york", cidade="Nova York", ph="ph-novayork", foto="nova-york.jpg",
        pais="Estados Unidos", continente="América do Norte", rota="GRU → JFK",
        landmarks=["Central Park", "Times Square", "Brooklyn Bridge"],
        sobre="Nova York impressiona com sua skyline icônica, museus de classe mundial e uma energia que não para. Da Times Square ao Central Park, cada esquina conta uma história diferente — e a Mattos Airlines leva você direto ao coração da Big Apple.",
        preco=3450, reserve_ate="12 ago 2026", classe="Executiva",
    ),
    dict(
        slug="toquio", cidade="Tóquio", ph="ph-toquio", foto="toquio.jpg",
        pais="Japão", continente="Ásia", rota="GRU → NRT",
        landmarks=["Shibuya Crossing", "Templo Senso-ji", "Torre de Tóquio"],
        sobre="Tóquio equilibra tradição e futuro como nenhuma outra cidade: templos centenários ao lado de arranha-céus, gastronomia premiada e um transporte impecável. Uma experiência intensa para quem busca contrastes únicos no Japão.",
        preco=5980, reserve_ate="05 set 2026", classe="Executiva",
    ),
    dict(
        slug="buenos-aires", cidade="Buenos Aires", ph="ph-buenosaires", foto="buenos-aires.jpg",
        pais="Argentina", continente="América do Sul", rota="GRU → EZE",
        landmarks=["La Boca", "Recoleta", "Teatro Colón"],
        sobre="Buenos Aires combina arquitetura europeia, tango nas ruas e uma das melhores carnes do mundo. A capital argentina é vibrante de dia e ainda mais viva à noite, perfeita para quem quer cultura, boemia e boa mesa.",
        preco=1290, reserve_ate="18 jul 2026", classe="Econômica",
    ),
    dict(
        slug="londres", cidade="Londres", ph="ph-londres", foto="londres.jpg",
        pais="Reino Unido", continente="Europa", rota="GRU → LHR",
        landmarks=["Big Ben", "Buckingham Palace", "London Eye"],
        sobre="Londres reúne história milenar, museus gratuitos de primeira linha e uma cena gastronômica surpreendente. Entre palácios reais e mercados de rua, a capital britânica é um destino clássico que nunca sai de moda.",
        preco=3120, reserve_ate="22 ago 2026", classe="Executiva",
    ),
    dict(
        slug="cidade-do-cabo", cidade="Cidade do Cabo", ph="ph-cidadedocabo", foto="cidade-do-cabo.jpg",
        pais="África do Sul", continente="África", rota="GRU → CPT",
        landmarks=["Table Mountain", "Robben Island", "Cape Point"],
        sobre="Cidade do Cabo une montanha, oceano e savana em um só lugar. Entre a Table Mountain e as praias da península, é um dos destinos mais cinematográficos da África, ideal para aventura e natureza.",
        preco=4760, reserve_ate="03 set 2026", classe="Econômica",
    ),
]

def money(v):
    return f"$ {v:,.0f}".replace(",", ".")

ICON = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBhdGggZD0iTTEyIDIxcy03LTYuMi03LTExYTcgNyAwIDEgMSAxNCAwYzAgNC44LTcgMTEtNyAxMXoiLz48Y2lyY2xlIGN4PSIxMiIgY3k9IjEwIiByPSIyLjMiLz48L3N2Zz4="

DEST_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cidade} — Mattos Airlines</title>
  <meta name="description" content="Voe para {cidade} com a Mattos Airlines. {rota} a partir de {preco_fmt}.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <main>
    <section class="hero-carousel" aria-label="Galeria de fotos de {cidade}">
      <header class="site-header">
        <div class="wrap">
          <a class="nav-back" href="index.html">← Destinos</a>
          <a class="brand" href="index.html">Mattos Airlines</a>
        </div>
      </header>

      <div class="carousel-track">
        <div id="slide-1" class="slide {ph}"><img class="photo" src="img/{foto}" alt="{landmark1}, {cidade}" loading="lazy"><img class="landmark-icon" src="{icon}" alt="Ícone de localização: {landmark1}, {cidade}"><span class="tag">{landmark1}</span></div>
        <div id="slide-2" class="slide {ph}"><img class="photo" src="img/{foto}" alt="{landmark2}, {cidade}" loading="lazy"><img class="landmark-icon" src="{icon}" alt="Ícone de localização: {landmark2}, {cidade}"><span class="tag">{landmark2}</span></div>
        <div id="slide-3" class="slide {ph}"><img class="photo" src="img/{foto}" alt="{landmark3}, {cidade}" loading="lazy"><img class="landmark-icon" src="{icon}" alt="Ícone de localização: {landmark3}, {cidade}"><span class="tag">{landmark3}</span></div>
      </div>
      <div class="carousel-arrows">
        <a href="#slide-1" aria-label="Foto anterior">‹</a>
        <a href="#slide-3" aria-label="Próxima foto">›</a>
      </div>
      <div class="carousel-dots">
        <a href="#slide-1" aria-label="Foto 1"></a>
        <a href="#slide-2" aria-label="Foto 2"></a>
        <a href="#slide-3" aria-label="Foto 3"></a>
      </div>
    </section>

    <div class="wrap hero-info">
      <p class="eyebrow">Destino em destaque</p>
      <h1 class="display">{cidade}</h1>
      <p class="place">{pais} · {continente}</p>
      <div class="od-row">
        <span class="tag">{rota}</span>
        <span class="price">a partir de {preco_fmt}</span>
      </div>
      <a class="btn btn-primary btn-block" href="checkout-{slug}.html">Reservar agora</a>
    </div>

    <section class="details">
      <div class="wrap">
        <h2 class="display" style="font-size:1.6rem;margin-bottom:1rem;">Sobre o destino</h2>
        <p class="details-lead">{sobre}</p>

        <div class="perks">
          <p class="perk">7 noites de hospedagem incluídas</p>
          <p class="perk">Café da manhã incluso todos os dias</p>
          <p class="perk">Cancelamento grátis em até 15 dias</p>
        </div>

        <div class="price-cta">
          <div>
            <p class="from">a partir de</p>
            <p class="amount">{preco_fmt}</p>
            <p class="deadline">Reserve até {reserve_ate}</p>
          </div>
          <div class="reserve-block">
            <a class="btn btn-primary" href="checkout-{slug}.html">Reservar viagem</a>
          </div>
        </div>

        <a class="policy-link" href="#">Ver política de cancelamento →</a>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="wrap">
      <span>Mattos Airlines — companhia aérea desde 2026</span>
      <span>{rota}</span>
    </div>
  </footer>

</body>
</html>
"""

CHECKOUT_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Checkout — {cidade} · Mattos Airlines</title>
  <meta name="description" content="Finalize sua reserva para {cidade} com a Mattos Airlines.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <header class="site-header">
    <div class="wrap">
      <a class="nav-back" href="{slug}.html">← Voltar</a>
      <a class="brand" href="index.html">Mattos Airlines</a>
    </div>
  </header>

  <main>
    <section class="checkout-header">
      <div class="wrap">
        <p class="eyebrow">Finalizar reserva</p>
        <h1 class="display">Checkout</h1>

        <div class="trip-summary">
          <div class="trip-thumb {ph}"><img class="photo" src="img/{foto}" alt="{cidade}" loading="lazy"></div>
          <div class="trip-info">
            <h2 class="card-city">{cidade}</h2>
            <p class="card-dates">{rota} · {classe}</p>
            <div class="card-price">
              <span class="from">a partir de</span>
              <span class="amount">{preco_fmt}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="checkout-section">
      <div class="wrap">
        <h2>Selecione as datas</h2>
        <div class="calendar-card">
          <div class="month-nav">
            <span>‹</span>
            <span>Junho 2026</span>
            <span>›</span>
          </div>
          <div class="weekday-row">
            <span>D</span><span>S</span><span>T</span><span>Q</span><span>Q</span><span>S</span><span>S</span>
          </div>
          <div class="day-grid">
            <div class="week">
              <div class="day muted">31</div><div class="day">1</div><div class="day">2</div><div class="day">3</div><div class="day">4</div><div class="day">5</div><div class="day">6</div>
            </div>
            <div class="week">
              <div class="day">7</div><div class="day">8</div><div class="day">9</div><div class="day">10</div><div class="day">11</div><div class="day">12</div><div class="day">13</div>
            </div>
            <div class="week">
              <div class="day">14</div><div class="day">15</div><div class="day">16</div><div class="day">17</div><div class="day">18</div><div class="day">19</div><div class="day">20</div>
            </div>
            <div class="week">
              <div class="day">21</div><div class="day">22</div><div class="day">23</div><div class="day in-range">24</div><div class="day in-range">25</div><div class="day in-range">26</div><div class="day in-range">27</div>
            </div>
            <div class="week">
              <div class="day in-range">28</div><div class="day in-range">29</div><div class="day in-range">30</div><div class="day muted">1</div><div class="day muted">2</div><div class="day muted">3</div><div class="day muted">4</div>
            </div>
          </div>

          <div class="dates-summary">
            <div class="field">
              <span class="tag">Ida</span>
              <span class="val">24 jun 2026</span>
            </div>
            <div class="field">
              <span class="tag">Volta</span>
              <span class="val">01 jul 2026</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="checkout-section">
      <div class="wrap">
        <h2>Passageiros / classe</h2>
        <div class="pax-field">
          <span class="val">1 Adulto, {classe}</span>
          <span class="edit">Editar</span>
        </div>
      </div>
    </section>

    <section class="checkout-section">
      <div class="wrap">
        <h2>Resumo do pagamento</h2>
        <div class="price-lines">
          <div class="price-line">
            <span class="label">Tarifa (1 adulto)</span>
            <span>{tarifa_fmt}</span>
          </div>
          <div class="price-line">
            <span class="label">Taxas e impostos</span>
            <span>{taxas_fmt}</span>
          </div>
          <div class="price-line total">
            <span class="label">Total</span>
            <span>{preco_fmt}</span>
          </div>
        </div>

        <div class="cta-pay">
          <a class="btn btn-primary btn-block" href="#">Confirmar e pagar</a>
        </div>
        <p class="secure-note">Pagamento seguro · Cancelamento grátis em até 15 dias</p>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="wrap">
      <span>Mattos Airlines — companhia aérea desde 2026</span>
      <span>{rota}</span>
    </div>
  </footer>

</body>
</html>
"""

for d in destinos:
    preco_fmt = money(d["preco"])
    taxas = round(d["preco"] * 0.096)
    tarifa = d["preco"] - taxas
    landmarks = d["landmarks"][:3] if len(d["landmarks"]) >= 3 else (d["landmarks"] + d["landmarks"])[:3]

    dest_html = DEST_TEMPLATE.format(
        cidade=d["cidade"], ph=d["ph"], pais=d["pais"], continente=d["continente"],
        rota=d["rota"], preco_fmt=preco_fmt, sobre=d["sobre"],
        reserve_ate=d["reserve_ate"], slug=d["slug"], icon=ICON, foto=d["foto"],
        landmark1=landmarks[0], landmark2=landmarks[1], landmark3=landmarks[2],
    )
    with open(os.path.join(DEST_DIR, f"{d['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(dest_html)

    checkout_html = CHECKOUT_TEMPLATE.format(
        cidade=d["cidade"], ph=d["ph"], rota=d["rota"], classe=d["classe"],
        preco_fmt=preco_fmt, tarifa_fmt=money(tarifa), taxas_fmt=money(taxas),
        slug=d["slug"], foto=d["foto"],
    )
    with open(os.path.join(DEST_DIR, f"checkout-{d['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(checkout_html)

print("Geradas", len(destinos) * 2, "páginas.")
