# Social Media Platform

A modern, responsive full-stack social media application designed to connect people, facilitate posts, interactive comments, and manage user profiles seamlessly. Built using Django, Tailwind CSS, and Django REST Framework.

 ## Project Brief

The Social Media Platform is a full-featured web application built for tech enthusiasts and general users alike to interact, share thoughts, and engage with content. It provides a clean, responsive user interface combined with robust backend services for authentication, profile customization, and post management.

## Business Rationale

In today's digital landscape, modern design, system performance, and user privacy are vital. This project addresses core business and user experience requirements:

**User Trust & Brand Authority:** A clean, semantic UI powered by Tailwind CSS ensures quick page loads, high visual appeal, and trust across all devices.

**Data Security & Integrity:** Built with Django’s built-in security features (CSRF protection, SQL injection protection, password hashing) and Django REST Framework to handle social interactions safely.

## Technologies Used

Python, Django, Django REST Framework (DRF) and 
Tailwind CSS

***Database & Hosting:*** PostgreSQL / SQLite (Development), Gunicorn, WhiteNoise

***Version Control:*** Git & GitHub

## Accessibility Features

***Semantic HTML:*** Built using `<header>`, `<main>`, `<section>`, and `<article>` structures to provide optimal screen-reader support.

***Responsive Layouts:*** Uses fluid CSS grid and flexbox layouts to ensure clarity across smartphones, tablets, and desktops.

***Input Clarity:*** Explicit form labelling, ARIA attributes, and accessible color contrast.

## Key Features

**Authentication System:** User registration, login, logout, and session management.

**User Profiles:** Custom user avatars, bios, and profile management with fallback avatars.

**Interactive Feed:** Dynamic feed allowing users to create, view, edit, and delete posts.

Comments: Engagement options on every post to foster active discussions.

**REST API:** Fully featured endpoints provided by Django REST Framework for future mobile app or client integrations.

## Git Workflow

To contribute or develop new features, please follow these steps:

Fork the Repository: Create your own copy of the project.

Create a Feature Branch:

``
git checkout -b feature/YourFeatureName
``


Commit Your Changes:

``git commit -m "Add feature description"
``


Push to Branch:

``git push origin feature/YourFeatureName
``


Open a Pull Request (PR): Describe your changes clearly and link any associated issues.

## Set Up Instructions

Prerequisites

Python 3.10.0

Git

Local Installation

Clone the repository:

``git clone https://github.com/rollingsmajiwa/social_media.git``


``cd social_media
``


Create and activate a virtual environment:


**On Windows**
``python -m venv .venv``
``.venv\Scripts\activate``


Install project dependencies:

``pip install -r requirements.txt``


Apply database migrations:

``python manage.py migrate``


Start the development server:

``python manage.py runserver``


Access the application:
Open your browser and navigate to http://127.0.0.1:8000/.

## Author

Rollings Majiwa

GitHub: [https://github.com/rollingsmajiwa](https://github.com/rollingsmajiwa)

Email: [https://github.com/rollingsmajiwa](https://github.com/rollingsmajiwa)

## License

This project is licensed under the MIT License.