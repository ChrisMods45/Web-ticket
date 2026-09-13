# ChrisAim Ticket Web

Primera parte del sistema de tickets para Telegram.

## Qué incluye
- Página principal estilo ChrisAim.
- Página de transcript.
- Ruta demo: `/transcript/demo`
- Diseño responsive para móvil y PC.
- Configuración básica para Render.
- Endpoint `/health`.

## Probar localmente

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Luego abre:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/transcript/demo

## Subir a Render
1. Sube esta carpeta a GitHub.
2. En Render crea un Web Service desde el repositorio.
3. Render puede detectar `render.yaml`.
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

## Próximo paso
Cambiar `TICKETS` por una base de datos y conectar el bot de Telegram para:
- crear tickets,
- guardar mensajes,
- cerrar tickets,
- generar token privado,
- enviar el enlace del transcript por Telegram.
