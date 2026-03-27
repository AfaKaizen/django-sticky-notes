Sticky Notes - Django Web Application

A clean and simple Sticky Notes web app built with Django. Users can register, login, and manage their personal colorful sticky notes with full CRUD functionality.

![Sticky Notes](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

Features

- User Registration & Login System
- Create, Read, Update, and Delete personal notes
- Color picker for each sticky note
- Search notes by title or content
- Responsive design with Bootstrap 5
- Secure authentication (users can only access their own notes)
- Clean and modern UI with hover effects
- Character counter while writing notes
- Success messages for better UX



Tech Stack

- Backend: Django (Python)
- Database: SQLite
- Frontend: Bootstrap 5 + Font Awesome
- Authentication: Django's built-in auth system



How to Run Locally

1. Clone the Repository

```bash
git clone https://github.com/yourusername/sticky-notes.git
cd sticky_notes_project
2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate     # For Windows
3. Install Dependencies
pip install -r requirements.txt
4. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser (Optional)
python manage.py createsuperuser
6. Run the Development Server
python manage.py runserver
Open your browser and go to: http://127.0.0.1:8000/



Project Structure
textsticky_notes_project/
├── manage.py
├── sticky_notes_project/       # Django project settings
├── notes/                      # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── templates/                  # Base templates
├── static/                     # Static files (optional)
├── db.sqlite3
├── requirements.txt
└── README.md



Pin important notes
Masonry (Pinterest-style) layout
Dark mode
Note tags
Export notes as JSON/Text



License
This project is open-source and available under the MIT License.



Made with ❤️ using Django