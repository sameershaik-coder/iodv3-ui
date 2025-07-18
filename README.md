# IODv3 UI

## Technology Stack
- **Backend**: Python (Django)
- **Frontend**: 
  - HTML
  - Tailwind CSS
  - JavaScript (Vanilla, HTMX, Alpine.js)
  - Node.js (for CSS build)
- **Testing**: Selenium/pytest
- **Database**: PostgreSQL/MySQL/SQLite

## Project Structure
```
iodv3-ui/
├── config/                 # Main project configuration
│   ├── settings.py        # Django settings (DB, apps, middleware)
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
│
├── core/                  # Main application
│   ├── views.py          # View controllers
│   ├── models.py         # Database models
│   └── templates/        # App-specific templates
│
├── templates/            # Global templates
│   └── base.html        # Base template with common layout
│
├── static/              # Static files (CSS, JS, images)
│
├── default/            # Tailwind CSS app
│   └── static/         # Generated CSS output
│
├── manage.py           # Django CLI management script
└── requirements.txt    # Python dependencies
```

## Default Directory Purpose

The `default` directory is the Tailwind CSS application directory created during Django-Tailwind initialization.

### Key Components:
1. **Tailwind Configuration** (`tailwind.config.js`)
   - Customize colors, fonts, spacing
   - Define plugins
   - Set up content paths for purging unused CSS

2. **Source Files** (`src/`)
   - Contains Tailwind CSS source files
   - Main input file for Tailwind directives

3. **Compiled Output** (`static/css/dist/`)
   - Contains production-ready CSS
   - Referenced by Django templates

## Development Setup

### Dependencies
- Django web framework
- django-tailwind
- django-browser-reload
- HTMX

### Running the Application
You need two terminal windows:

```bash
# Terminal 1: Tailwind CSS compiler
python manage.py tailwind start

# Terminal 2: Django server
python manage.py runserver
```

### Configuration Note
The name "default" comes from the `TAILWIND_APP_NAME = 'default'` setting in Django configuration.