# Data Visualization Using Real World Data in Python

### Details
- :ninja: **John Mike Asuncion** (BSCPE 1-2)
- Object Oriented Programming `CMPE 103`
- **Professor:** Engr. Danilo C. Madrigalejos, Jr.
### **Assignment**
- Create a GitHub account
- Find existing Python project
- Learn how to upload code in GitHub using `git bash`
- Create a demonstration video
## Overview
This project demonstrates how to visualize real-world data using Python, specifically focusing on `IMDB movies data`. The goal is to clean the data, analyze it, and create various visualizations to gain insights into movie popularity, genres, budgets, and revenues.
## Table of Contents
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Installation](#installation)
## Usage
1. **Download the `.csv` file containing IMDB Movies data.**
    - The script automatically downloads the data from Google Drive.
2. **Data Cleaning and Preparation:**
    - The data is cleaned by removing unnecessary characters and converting data types.
## Visualizations
The following visualizations are created:
1. **Popularity Over Time**
   - Displays how movie popularity has changed over the years using *line plot*.
2. **Movie Genre Distribution**
   - Shows the count of movies in each genre using *bar plot*.
3. **Budget vs Revenue**
   - Compares the budget and revenue of movies to identify trends using *scatter plot*.
4. **Top Movie Production Countries**
   - Highlights the countries that produce the most movies using *pie chart*.
5. **Pairplot**
   - Provides insights into the relationships between budget, revenue, and popularity using *pairplot*.
## Installation
To run this project, you need to have Python installed along with the **required libraries**. You can install the necessary libraries using `pip`:
```bash
pip install matplotlib seaborn pandas numpy gdown
