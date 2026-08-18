## Análisis de Skills más demandadas Remote-OK

Proyecto de práctica hecho a mano: extraigo los datos de los ganadores del Balón de Oro desde Wikipedia, los limpio, y después los analizo para encontrarles una historia. Es un pipeline de datos completo, de punta a punta.

Es mi primer proyecto, y ojalá el primero de muchos que en el futuro me consigan trabajo. :)

---

## Parte 1 — Scraper

Un scraper de los ganadores del Balón de Oro, desde el primero (1956) hasta el último (2025, ganado por Dembélé).

Extrae desde Wikipedia todos los ganadores del título y los exporta a un archivo CSV. También se puede ver la tabla desde el código llamando a la variable `tabla`.

Para limpiar los datos uso expresiones regulares (por ejemplo, para sacar las referencias `[ ]`). Además, salteo el año 2020, ya que no hubo entrega de premios debido al Covid-19.

El CSV tiene 70 filas: 1 de encabezado (Año, Jugador, Club, Puntos) y 69 de ganadores.

## Parte 2 — Análisis

Analizo la evolución de los puntos de los ganadores en los últimos 5 años y genero un gráfico de líneas (`grafico.png`).

**Lo que encontré:** en 2021, 2022 y 2023 los puntos son bajos, y el salto posterior se debe a que **cambiaron el sistema de puntuación** (no a que los jugadores hayan sido "mejores"):

- Antes, cada periodista votaba su top 5, con los puntos distribuidos así: 6, 4, 3, 2, 1.
- Después de 2023, pasaron a votar su top 10, con otra distribución: 15, 12, 10, 8, 7, 5, 4, 3, 2, 1.

Otro datos claves:
  1. la cantidad de periodistas votantes también cambió — 180 en 2021, 100 en 2022, y solo 92 en 2023.
  2. En 2022 cambiaron los criterios de evaluación, siendo el mayor cambio que se toma en cuenta el rendimiento individual en la temporada (agosto - julio) y ya no más el año natural (enero - diciembre

Por eso, el salto en los puntos no refleja un cambio en el nivel de los jugadores, sino un cambio en la forma de contar.


Fuentes: 
  https://www.ole.com.ar/messi/balon-oro-votacion-criterio-fecha_0_oG2WCLGtR.html ; 
  https://www-topendsports-com.translate.goog/sport/soccer/awards/ballondor-voting.htm?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sge ; 
  https://www.elespanol.com/deportes/futbol/20241028/vota-balon-oro-hace-clasificacion-final-premio-dado-uefa-france-football/896910869_0.html
---

## Requisitos

- Python 3.10 o superior
- pandas
- requests
- matplotlib

## Cómo ejecutarlo

```
pip install pandas requests matplotlib 
```

```
# Parte 1 — Scraper (genera remote_ok.csv)
python remote_ok.py

# Parte 2 — Análisis (genera remoteok_analisis.png)
python analisis_skills_remote_ok.py
```

---

*Fecha: 18-08-2026*
