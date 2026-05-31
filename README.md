# Proyecto 2 - Streaming de eventos con Kinesis Firehose + análisis inteligente

Este repositorio contiene los avances, scripts y documentación del proyecto final enfocado en capturar eventos digitales, almacenarlos de forma segura en la nube y generar un análisis breve de lo ocurrido en una ventana de tiempo utilizando inteligencia artificial.

## 🎯 Objetivo del MVP
Simular eventos en tiempo casi real, enviarlos a Kinesis Firehose, almacenarlos en S3, catalogarlos para consulta con Athena y usar Bedrock para explicar los patrones observados.

---

## 🚀 Estado Actual del Despliegue

La base de la infraestructura cloud ha sido desplegada colaborativamente en **AWS (Amazon Web Services)** mediante una cuenta con roles administradores (IAM).

### 1. Capa de Almacenamiento (S3 Raw / Bronze)
* **Servicio:** Amazon S3
* **Bucket Principal:** `ventas-cafeteria-raw-diego`
* **Región:** EE.UU. Este (Norte de Virginia) `us-east-1`
* **Estructura de Directorios:** Prefijo `/ingest-data/` creado con éxito para recibir los objetos JSON del simulador.

### 2. Capa de Ingesta (Streaming con Kinesis Firehose)
* **Estado:** En proceso de activación técnica (Esperando liberación de seguridad por parte de AWS para cuentas nuevas).

---

## 📐 Arquitectura del Pipeline (Sugerida)
`Simulador Python -> Kinesis Firehose -> S3 Raw -> Glue Crawler/Catalog -> Athena -> Resultado agregado -> Bedrock -> Resumen de eventos`

## 📊 Especificaciones del Dataset Sugerido
Los eventos artificiales serán estructurados en formato JSON con los siguientes campos requeridos:
* `event_id`, `event_time`, `user_id`, `event_type`, `product_id`, `device`, `status`, `latency_ms`.

## 👥 Integrantes del Equipo
* Junior Sayet Cruces Isla
* Diego Francisco Cervantes Castillon
