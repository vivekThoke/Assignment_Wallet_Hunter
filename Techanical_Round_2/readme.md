# Project Name

## Overview

This project is a Flask-based web application that provides various analytics dashboards. The application uses Chart.js to render different types of charts based on the provided data.

## Features

- Display various analytics dashboards
- Render charts using Chart.js
- Responsive and user-friendly interface

## Requirements

- Docker

## Setup and Running the Project

### Using Docker

1. **Build the Docker image:**

    Open a terminal and navigate to the project directory. Run the following command to build the Docker image:

    ```sh
    docker build -t project-name .
    ```

2. **Run the Docker container:**

    After building the image, run the following command to start the container:

    ```sh
    docker run -p 8000:8000 project-name
    ```

    This will start the Flask application, and it will be accessible at `http://localhost:8000`.
