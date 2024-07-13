# Weather Forecast Project

This project provides a weather forecast using an API key in Django. It fetches the current weather data for a specified location using the Weather API and displays it on the website.

But here in my code, just i am checking place by giving latitude and longitude.
You can check any type of data in weather report by modifying the code.


## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory and add your API key:**

    ```plaintext
    WEATHER_API_KEY=your_api_key_here
    ```

### Configuration

Ensure that the `.env` file is added to `.gitignore` to prevent it from being committed to the repository. Your `.gitignore` file should include:

just type  .env   in your .gitignore file

---run the server---
python manage.py runserver


---make sure that your project is in this structure---
weather_project/
├── weather_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── weather/
│   ├── migrations/
│   ├── templates/
│   │   └── weather/
│   │       └── weather.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
