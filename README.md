# Petroleo-vs-Petroleras
Análisis de la relación entre los precios del petróleo y las acciones energéticas mediante Python
# 📊 ¿El petróleo mueve a las petroleras… o al revés?

Este proyecto analiza la relación entre el precio del petróleo y las principales compañías energéticas (Repsol, BP, Shell, Exxon y Chevron) utilizando Python.

---

## 🧠 Objetivo

Responder a una pregunta sencilla pero relevante:

> ¿Existe una relación predictiva entre el petróleo y las acciones del sector energético?

---

## 🔍 Metodología

El análisis se ha dividido en dos partes:

### 1. Análisis estadístico

- Descarga de datos históricos con `yfinance`
- Cálculo de retornos diarios
- Correlación contemporánea
- Correlación con desfase (lag)
- Análisis bidireccional:
  - Petróleo → acciones
  - Acciones → petróleo

---

### 2. Dependencia condicional

Se estudia el comportamiento del petróleo bajo ciertas condiciones del mercado:

- ¿Qué ocurre cuando una petrolera sube con fuerza?
- Análisis de retornos condicionados
- Comparación de distribuciones

---

### 3. Validación mediante estrategia

Se construye una estrategia simple:

- Entrada en petróleo tras movimientos significativos en petroleras
- Comparación con estrategia buy & hold
- Evaluación de métricas (rentabilidad, drawdown, Sharpe)
- Inclusión de costes de transacción
- Análisis de robustez

---

## 📊 Resultados principales

- Existe una correlación moderada (~0.5) entre petróleo y petroleras
- No se observa capacidad predictiva lineal significativa
- Se identifica una **dependencia condicional relevante**:
  - Cuando las petroleras suben con fuerza, el petróleo tiende a presentar retornos superiores
- La estrategia basada en este comportamiento:
  - Mejora al mercado en ciertos periodos
  - Depende del régimen del mercado energético

---

## 🧠 Conclusión

El petróleo no parece ser predecible de forma continua, pero sí presenta comportamientos anómalos en momentos concretos del sector energético.

Esto sugiere un fenómeno de:

- Dependencia no lineal
- Propagación de información dentro del sector

---

## ⚠️ Limitaciones

- Posible dependencia del periodo analizado (especialmente 2020–2022)
- Resultados sensibles a condiciones de mercado
- La estrategia no garantiza resultados futuros

---

## 📁 Estructura del proyecto
