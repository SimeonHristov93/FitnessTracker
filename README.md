# Fitness Tracker

A comprehensive web application for tracking your fitness journey, built with Django.

## Features

*   **Workout Management:** Create, update, and delete workout plans.
*   **Exercise Library:** Maintain a database of exercises with detailed instructions and muscle groups.
*   **Progress Tracking:** Log your workouts, track duration, calories burned, and rate your sessions.
*   **Dashboard:** Visualize your progress with statistics on completed workouts, total training time, and more.
*   **Search:** Effortlessly find workouts and exercises with a powerful search feature.
*   **Responsive Design:** Fully responsive interface optimized for desktop and mobile devices.

## Tech Stack

*   **Backend:** Django (Python)
*   **Frontend:** HTML, Tailwind CSS (via CDN), JavaScript
*   **Database:** PostgreSQL

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/SimeonHristov93/FitnessTracker.git
    cd FitnessTracker
    ```

2.  **Create a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the root directory and add the following variables:

    ```env
    SECRET_KEY=django-insecure-t@ei6mlsfz=5=43-!w63pr1a4n7-82dfra^lfr44m-)qix=gbl
    DEBUG=False
    DB_NAME=fitness_tracker_db
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_HOST=127.0.0.1
    DB_PORT=5432
    ```

5.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Access the application at `http://127.0.0.1:8000/`.

## Usage

*   **Workouts:** Browse the list of available workouts or create your own custom plans.
*   **Exercises:** Explore the exercise library to learn new movements.
*   **Log Workout:** Record your completed workouts to track your progress over time.
*   **Dashboard:** View your fitness statistics and recent activity on the dashboard.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
