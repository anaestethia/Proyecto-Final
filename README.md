# Game Library API

## Descripción
La Game Library API es una API para gestionar una biblioteca de videojuegos, permitiendo a los usuarios registrar videojuegos, agregar reseñas y marcar favoritos.

## Requisitos
- Python 3.8 o superior
- PostgreSQL o SQLite

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/game_library_api.git
   cd game_library_api
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```bash
   pip install fastapi[all] sqlalchemy passlib python-dotenv python-jose
   ```

4. Configura el archivo `.env` con tus credenciales de base de datos.

5. Ejecuta la aplicación:
   ```bash
   uvicorn main:app --reload
   ```

## Documentación
La documentación de la API está disponible en `/docs`.