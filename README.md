# 🚀 Job Hunter Engine: Automation & Data Analysis

Este proyecto es una herramienta de **Automatización de Procesos (RPA)** diseñada para optimizar la búsqueda de empleo en las áreas de Análisis de Datos y Automatización con Python, eliminando manualmente el ruido de búsquedas no deseadas (como perfiles contables).

## 🛠️ Tecnologías utilizadas
- **Python 3.9+**
- **GitHub Actions** (Automatización 100% en la nube)
- **Telegram Bot API** (Notificaciones en tiempo real)
- **SMTP/Gmail API** (Reportes diarios por correo)

## 📁 Estructura del Proyecto
- `src/engine.py`: Cerebro del bot y lógica de ejecución.
- `src/notifications.py`: Gestión de alertas vía Telegram y Email.
- `src/utils.py`: Normalización de queries y generación de URLs.

## 🤖 Automatización
El sistema está configurado para ejecutarse diariamente a las 9:00 AM (ART) mediante GitHub Actions, enviando un reporte consolidado con las vacantes más frescas que coinciden con el stack tecnológico: **Python, SQL y Automation**.

---
*Proyecto desarrollado por Andrés Antolín Díaz Balbás como parte de su portafolio de transición a Data Science.* 
