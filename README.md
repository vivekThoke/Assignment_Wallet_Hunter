# Admin Dashboard Design
For this round, you need to propose 30 analytics/visualizations that would be useful for an Admin Dashboard for managing Telegram groups.

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
    docker build -t admin-dashboard .
    ```

2. **Run the Docker container:**

    After building the image, run the following command to start the container:

    ```sh
    docker run -p 8000:8000 admin-dashboard
    ```

    This will start the Flask application, and it will be accessible at `http://localhost:8000`.

## Project Structure

### [app.py](http://_vscodecontentref_/1)

The main Flask application file that sets up routes and renders templates.

### [code_file.py](http://_vscodecontentref_/2)

Contains functions to fetch and process data for the analytics.

### `Dockerfile`

Defines the Docker image for the project.

### `requirements.txt`

Lists the Python dependencies for the project.

### `templates/`

Contains HTML templates for rendering the dashboard and analytics pages.

---

# Analytics Proposal
For this round, you need to propose 20 analytics

## Overview

This project contains various data analysis and visualization tasks performed using Jupyter Notebooks. The analysis includes group engagement, member activity, message interactions, and more.

## Features

- Data analysis using pandas
- Visualization using matplotlib and seaborn
- Jupyter Notebooks for interactive analysis

## Requirements

- Jupyter Notebook
- pandas
- matplotlib
- seaborn

## Setup and Running the Project

### Using Jupyter Notebook

1. **Install the required packages:**

    Open a terminal and navigate to the project directory. Run the following command to install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

2. **Start Jupyter Notebook:**

    Run the following command to start Jupyter Notebook:

    ```sh
    jupyter notebook
    ```

    This will open Jupyter Notebook in your default web browser.

## Project Structure

### `analytics.ipynb`

Contains various data analysis tasks related to group engagement and member activity.

### [app.py](http://_vscodecontentref_/3)

A Flask application file for serving the analysis results.

### `assignment1.ipynb`

Contains additional data analysis tasks and visualizations.

### [data/](http://_vscodecontentref_/4)

Contains CSV files with mock data and a script to generate mock datasets.

### `logs/`

Contains log files for the application.

### `static/`

Contains static files like CSS for styling.

### `templates/`

Contains HTML templates for rendering the analysis results.