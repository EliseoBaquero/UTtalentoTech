# Proyecto: Detección de Phishing, Anonimización de Datos y Análisis de Riesgo de Churn
Proyecto Hackathon de UTtalento Tech 2025, en una Base de Datos de correos se van a asignar tickets, anonimizar datos personales, hacer predicciones de phising, predicciones de churn, analisis de sentimiento, recomendaciones y visualizaciones. 

---

## Tabla de Contenidos
- [Equipo](#equipo)
- [Proyecto](#proyecto)
- [Explicación General](#explicación-general)
- [Detección de Phishing](#detección-phishing)
- [Anonimización de Datos Sensibles](#anonimización-de-datos-sensibles)
- [Creación de Tickets](#creación-de-tickets)
- [Riesgo de Churn](#riesgo-churn)
- [Requerimientos a Instalar](#requerimientos-a-instalar)
- [Equipo](#equipo)

---
## Equipo

| Nombre                | Usuario de GitHub                          |
|-----------------------|--------------------------------------------|
| Eliseo Baquero         | [@eliseobaquero](https://github.com/eliseobaquero) |
| Santiago Ramirez  | [@SantiagoRamirez](https://github.com/SantyR30) |
| Nombre del miembro 2  | [@usuariogithub2](https://github.com/usuariogithub2) |

## Proyecto
Este proyecto está enfocado en la **detección de phishing**, **anonimización de datos sensibles**, **creación de tickets** y **análisis de riesgo de churn** para mejorar la seguridad y retención de clientes en la organización Vortex.

---

## Explicación General
El proyecto integra múltiples herramientas y técnicas para:
- Identificar correos o mensajes fraudulentos (phishing).
- Proteger la privacidad de los usuarios mediante la anonimización de datos.
- Automatizar la creación de tickets para el tipo de mantenimiento Correctivo o evolutivo.
- Analizar el sentimiento de los usuarios y clasificar su riesgo de abandono (churn).

---

## Detección de Phishing
Se implementan algoritmos de **machine learning** y reglas heurísticas para detectar patrones sospechosos en correos electrónicos, mensajes o enlaces. Las características analizadas incluyen:
- Dominios sospechosos.
- Estructura de URLs.
- Contenido del mensaje.
- se usa el archivo phising.py
- El Archivo BDcorreos.csv, tiene cuato columnas y 2005 filas.
- El mismo se dividio para entrenamiento (80%) y para testeo (20%).
- Se utilizo un XGBoost Model que dio las siguientes metricas.
- Se detecto que existian 28 emails con phising con las siguientes metricas.
- Accuracy: 0.9975
- Precision: 1.0000
- Recall: 0.8333
- F1-Score: 0.9091
- Se crea un nuevo archivo classified_emails.csv sin los email de phising.

---

## Anonimización de Datos Sensibles
Para proteger la privacidad de los usuarios, se aplican técnicas de anonimización a los datos, como:
- **Tokenización**: Reemplazo de información sensible (correos o emails) por identificadores únicos por nuevo campo ID Usuario.
- **Enmascaramiento**: Ocultar parcialmente datos (nombres personas y nombre empresa ejemplo: lina martinez por XY o System Bogota por XY).
- se usa el archivo anonimizacion.py
- se crea un primer archivo solo con los email, se eliminan los duplicados y se les crea a cada uno un numero de usuario unico BDUsuarios.csv
- se genera un nuevo archivo despues de la anonimizacion BDanonimo_final.csv

---

## Creación de Tickets
Se crea un diccionario de palabras automatiza la generación de tickets para:
- Mantenimiento Correctivo
- Mantenimiento Evolutivo

Los tickets se registran en una nueva columna Tipo_mantenimiento.
- se usa el archivo ticket.py
- se genera un archivo clasificacion.csv este incluye una columna de tipo_mantenimiento
---

## Riesgo de Churn
Se analiza el sentimiento de los usuarios a partir de sus mensajes de correo para clasificar su riesgo de abandono:
- **High Risk**: Usuarios con sentimiento negativo acumulado.
- **Medium Risk**: Usuarios con sentimiento neutral o ligeramente negativo.
- **Low Risk**: Usuarios con sentimiento positivo.

Los resultados se acumulan por usuario creando un nuevo archivo riesgoalto.csv para su posterior análisis:
- `riesgoalto.csv`: Lista de usuarios con alto riesgo de churn.
- se espera que la alta directiva ofrezca una solución a estos clientes.

---
## Requerimientos a Instalar
Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install pandas pysentimiento matplotlib seaborn scikit-learn nltk.

---
