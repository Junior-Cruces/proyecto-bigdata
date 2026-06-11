# Pipeline de Datos AWS Serverless - Caso Cafetería ☕

Este repositorio contiene el MVP (Producto Mínimo Viable) para la captura, procesamiento y análisis inteligente de eventos transaccionales en tiempo real utilizando una arquitectura 100% Serverless en Amazon Web Services (AWS).

## 👥 Integrantes
* Cruces Isla, Junior Sayet
* Cervantes Castillon, Diego Francisco

## 🏗️ Arquitectura del Sistema
El flujo de datos se divide en 4 capas elásticas:
1. **Ingestión (Capa Bronze):** Simulación de interacciones de usuarios mediante un script de Python, almacenando los archivos crudos en formato **JSON Lines** en un bucket de **Amazon S3**.
2. **Catalogación (Capa Silver):** Uso de **AWS Glue Crawler** para mapear la estructura de forma automática en el Data Catalog.
3. **Analítica (Capa Gold):** Consultas SQL interactivas sobre el Data Lake utilizando **Amazon Athena**.
4. **Capa de Inteligencia:** Conexión de métricas con **Amazon Bedrock** (Modelo Nova 2 Lite) para la generación automatizada de reportes ejecutivos.

## 📊 Hallazgo Técnico Crítico
Tras la agregación analítica de los eventos en Athena, se detectó una anomalía severa en el rendimiento por canales de acceso:
* **Mobile (Celulares):** 151.6 ms (Fluido)
* **Desktop (Computadoras):** 197.5 ms (Fluido)
* **Tablets (Tabletas):** **685.0 ms (Crítico - Latencia alta)**

*Impacto de negocio:* El canal de Tablets representa un riesgo inminente de abandono de carrito de compras debido a problemas de renderizado o diseño responsivo.
