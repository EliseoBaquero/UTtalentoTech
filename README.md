# Proyecto: Detección de Phishing, Anonimización de Datos y Análisis de Riesgo de Churn
Proyecto Hackathon de UTtalento Tech 2025, en una Base de Datos de correos se van a asignar tickets, anonimizar datos personales, hacer predicciones de phising, predicciones de churn, analisis de sentimiento, recomendaciones y visualizaciones. 

---

## Tabla de Contenidos
- [Proyecto](#proyecto)
- [Explicación General](#explicación-general)
- [Detección de Phishing](#detección-phishing)
- [Anonimización de Datos Sensibles](#anonimización-de-datos-sensibles)
- [Creación de Tickets](#creación-de-tickets)
- [Riesgo de Churn](#riesgo-churn)
- [Requerimientos a Instalar](#requerimientos-a-instalar)
- [Equipo](#equipo)

---

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
- Contenido del mensaje (palabras clave, urgencia, etc.).

---

## Anonimización de Datos Sensibles
Para proteger la privacidad de los usuarios, se aplican técnicas de anonimización a los datos, como:
- **Tokenización**: Reemplazo de información sensible (correos o emails) por identificadores únicos por nuevo campo ID Usuario.
- **Enmascaramiento**: Ocultar parcialmente datos (nombres personas y nombre empresa ejemplo: lina martinez por XY o System Bogota por XY).

---

## Creación de Tickets
Se crea un diccionario de palabras automatiza la generación de tickets para:
- Mantenimiento Correctivo
- Mantenimiento Evolutivo

Los tickets se registran en una nueva columna Tipo_mantenimiento.

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
pip install pandas pysentimiento matplotlib seaborn scikit-learn nltk
