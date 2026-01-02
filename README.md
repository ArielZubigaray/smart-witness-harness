# Smart Witness - Agent Harness

Sistema de verificación visual de alarmas desarrollado de forma autónoma con Claude Agent SDK.

## Quick Start

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Configurar OAuth token en `autonomous_agent_demo.py`

3. Ejecutar el harness:
```bash
python autonomous_agent_demo.py --project-dir ./project
```

## URLs de Servicios

| Servicio | URL |
|----------|-----|
| Dashboard | http://localhost:3000 |
| Mock Device | http://localhost:3001 |
| Mock Telegram | http://localhost:3002 |
| Backend API | http://localhost:8000 |
