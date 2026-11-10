
# Markdown Note Taking App

A simple note-taking application built with Django and Django REST Framework that allows users to create, manage, and render notes written in Markdown.

The project provides a RESTful API for managing notes, with support for converting Markdown content into sanitized HTML, allowing notes to be displayed in a properly formatted way.

## Features

- **Create Notes:** Create notes with Markdown content.
- **Retrieve Notes:** Retrieve list of uploaded notes.
- **Markdown Rendering:** Convert Markdown content into HTML.
- **HTML Sanitization:** Sanitize generated HTML to prevent potentially harmful content from being rendered.
- **Authentication:** Session-based authentication for users.

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

## Getting Started

### Prerequisites

- Python 3.x
- Pipenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Jamal-Mounyer/Markdown-Note-taking-App
   cd Markdown-Note-taking-App
   ```

2. Install dependencies:

   ```bash
   pipenv install
   ```

3. Create your environment configuration:

   ```bash
   cp .env.example .env
   ```

   Update the `.env` file with your local configuration.

4. Apply database migrations:

   ```bash
   pipenv run python manage.py migrate
   ```

5. Start the development server:

   ```bash
   pipenv run python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/api/`.

## Project Reference

This project was developed as part of the [Markdown Note-taking App](https://roadmap.sh/projects/markdown-note-taking-app) project on roadmap.sh.
