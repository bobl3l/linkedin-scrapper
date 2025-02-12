# LinkedIn Job Scraper

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.9.3-green) ![Pandas](https://img.shields.io/badge/Pandas-1.3.0-orange) ![Plotly](https://img.shields.io/badge/Plotly-5.3.1-red)

This is a personal project to scrape and analyze job postings from LinkedIn. The goal is to understand the demand for specific roles, programming languages, and technologies in the job market. The project uses BeautifulSoup for web scraping, Pandas for data processing, and Plotly for visualization.

# Project Overview
This project scrapes job postings from LinkedIn for specific roles, programming languages, and technologies. It then analyzes the data to identify trends in job demand and visualizes the results using interactive charts.

# Key Features:
Scraping: Collects job postings from LinkedIn.

Analysis: Analyzes job demand for roles, languages, and technologies.

Visualization: Generates interactive bar charts to visualize trends.

# How It Works
Scraping Job Postings:

The script scrapes job postings from LinkedIn using BeautifulSoup.

It extracts details like job title, company name, location, and job description.

Analyzing Data:

The script analyzes the scraped data to count the number of job postings for specific roles, languages, and technologies.

Example:

python
Copy
role_number = {}
for div in divisions:
    role_number[div] = numbers_scrapper(div).replace(",", "")
    role_number[div] = int(role_number[div])
Visualizing Results:

The script generates interactive bar charts using Plotly to visualize the results.

Example:

python
Copy
fig = go.Figure(go.Bar(
    y=labels,
    x=values,
    orientation='h',
    marker=dict(color="steelblue")
))
fig.show()

# Data Analysis
The project analyzes the following:

Roles: Cyber Security, Cloud, Data Analyst, Full Stack, Frontend, Backend, QA/Test, DevOps, Web, Mobile, System Administrator, Quant, AI.

Languages: JavaScript, TypeScript, HTML/CSS, SQL, Python, Java, C++, C#, Ruby, Kotlin, Go, Objective-C, Flutter, Swift, Scala, PHP, R.

Technologies: React, Next.js, LLM, AI, CMS, WordPress, AWS, Node.js, Angular, Redux, Django, Flask, .NET, Spring, Vue, Express.js.

# Visualizations
The project generates the following visualizations:

Roles: A horizontal bar chart showing the number of job postings for each role.

Languages: A horizontal bar chart showing the number of job postings for each programming language.

Technologies: A horizontal bar chart showing the number of job postings for each technology.

# Notes
Ethical Scraping: Be mindful of LinkedIn's terms of service and avoid overloading their servers. Add delays between requests to scrape responsibly.

Limitations: The script may need adjustments if LinkedIn changes its website structure.

This project is a great way to explore web scraping, data analysis, and visualization techniques. Feel free to modify and extend it to suit your needs! 🚀
