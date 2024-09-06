# tellco-analysis
Analysis of TellCo for growth opportunities and investment potential.

## Overview

This project focuses on analyzing growth opportunities for TellCo, a mobile service provider in the Republic of Pefkakia. The goal is to determine whether TellCo is worth buying or selling by conducting comprehensive exploratory data analysis (EDA), user engagement analysis, and more.

## Project Structure

- `load_data.py`: Contains functions for loading data from a PostgreSQL database using `psycopg2` and `SQLAlchemy`.
- `notebooks/`: Contains Jupyter notebooks for various tasks:
  - `EDA.ipynb`: Exploratory Data Analysis (Task 1)
  - `quantitative.ipynb`: Quantitative Analysis (Task 2)
  - `correlation.ipynb`: Correlation Analysis (Task 3)
- `scripts/`: Contains additional scripts for data processing and analysis.
- `data/`: Directory for raw and processed datasets.
- `reports/`: Directory for generated reports and visualizations.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database and load the schema and data:
    - Import `schema.sql` and `telecom.sql` into pgAdmin.

## Usage

### Data Loading

- Use `load_data.py` to load data from the PostgreSQL database. Modify the connection details as needed.

### Analysis

- Open the relevant Jupyter notebook (`EDA.ipynb`, `quantitative.ipynb`, `correlation.ipynb`) and run the cells to perform analysis.

## Tasks

### Task 1: Exploratory Data Analysis (EDA)
- Handle missing values and outliers.
- Perform univariate and bivariate analyses.
- Execute dimensionality reduction via PCA.

### Task 2: User Engagement Analysis
- Track user engagement metrics such as session frequency, duration, and total traffic.
- Normalize metrics and apply k-means clustering.
- Compute statistics for each cluster and aggregate total traffic per application.
- Plot the top 3 most used applications.

### Task 3: Correlation Analysis
- Align dates between news and stock price data.
- Perform sentiment analysis on news headlines.
- Calculate daily stock returns.
- Determine the Pearson correlation coefficient between sentiment scores and stock returns.

## Deployment

- The project includes deployment with CI/CD and Docker. Follow the instructions in `docker/` for setting up and running Docker containers.

## Contribution

Feel free to fork the repository and submit pull requests with improvements or fixes.

## Contact

For any questions or feedback, please contact [olani siyum](mailto:olisiyum@gmail.com).

