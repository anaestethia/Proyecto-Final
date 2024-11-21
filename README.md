# Game Library API

## Descripción
La Game Library API es una API para gestionar una biblioteca de videojuegos, permitiendo a los usuarios registrar videojuegos, agregar reseñas y marcar favoritos.

## Requisitos
- Python 3.8 o superior
- PostgreSQL o SQLite

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/anaestethia/Proyecto-Final.git
   cd Proyecto-Final
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   venv/Scripts/activate  # En Linux usa `source venv/bin/activate`
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura el archivo `.env` con el archivo `.env.example` cambiando las credenciales por las tuyas

5. Ejecuta la aplicación:
   ```bash
   uvicorn main:app --reload
   ```

## Documentación
La documentación de la API está disponible en `/docs`.