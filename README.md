# Análisis de Skills más demandadas Remote OK

Proyecto de práctica hecho a mano: extraigo los datos de las skills mas demandadas en Remote OK, usando JSON. Analizo los datos para hacer una comparación entre las skills más populares hoy en día.
---

## Parte 1 — Scraper

Un scraper de los skills más buscados en Remote OK.

Extrae datos de empleos y los exporta a un archivo CSV. También se puede ver la tabla desde el código llamando a la variable `tabla`.

En caso de error, el código esta preparado para avisarte donde falla.

## Parte 2 — Análisis

Analizo las skills más demandadas y genero un gráfico de barras (remoteok_analisis.png).

**Lo que encontré:** en los (aproximadamente) 100 empleos analizados, las categorías más demandadas no son técnicas: lideran exec (roles de liderazgo), customer support (atención al cliente), ops (operaciones), education y marketing. El desarrollo de software (dev) aparece recién en el 7º puesto. Esto sugiere que el trabajo remoto ya no es territorio exclusivo de la programación — abarca operaciones, atención al cliente, educación y muchos roles generales.

**Una aclaración:** los tags de RemoteOK son auto-asignados y tienden a sobre-aplicarse (un mismo aviso puede tener 20+ etiquetas, algunas poco relacionadas con el puesto real). Por eso estos conteos son una aproximación de la demanda, no una medición exacta. Aun así, la tendencia —predominio de roles no técnicos— es lo bastante marcada como para ser significativa.

Fuentes: 
  https://www.cvmaker.com/blog/career/top-remote-jobs
  Remote Ok: https://remoteok.com

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
