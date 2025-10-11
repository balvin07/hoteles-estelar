# Encuesta de Satisfacción – Hotel 🏨⭐

Django app que reemplaza **formularios en papel** por una experiencia **moderna y rápida** en cualquier dispositivo.

## Demo en 15 segundos
![Formulario vacío](screenshots/screenshot_form.png)
![Selección de estrellas](screenshots/screenshot_stars.png)
![Página de gracias](screenshots/screenshot_thanks.png)

## Características
✅ **Diseño responsive** – se ve bien en móvil y escritorio  
✅ **Sistema de estrellas interactivo** – sin JavaScript externo  
✅ **Guardado instantáneo** – datos almacenados en SQLite  
✅ **Página de agradecimiento animada** – mejora la percepción de marca  

## Stack
`Python 3.11` `Django 5` `SQLite` `Bootstrap 5` (CDN)

## Instalación local
```bash
git clone https://github.com/balvin07/hotel.git
cd hotel
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
