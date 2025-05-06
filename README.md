# JIRA Resource Management App with AI PM Buddy

## Overview
This Streamlit application provides a comprehensive resource management solution for project managers working with JIRA data. It combines powerful data visualizations with an AI-powered Project Management Assistant to provide insights, recommendations, and scenario planning.

## Features
- **Interactive Dashboard**: Overview of project metrics and key performance indicators
- **Gantt Chart**: Visualize task timelines by assignee
- **Traffic Light Matrix**: At-a-glance task status monitoring
- **Sprint Burnup**: Track progress against total scope
- **PM Daily Brief**: Automated daily summary of action items and alerts
- **Resource Load Visualizations**: Radar charts, bubble charts, and heatmaps
- **AI PM Buddy**: AI-powered assistant for answering PM questions, generating smart briefs, and performing what-if simulations

## AI PM Buddy Features
- **PM FAQ**: Quick answers to common project management questions
- **Smart PM Brief**: Generate comprehensive project status reports with critical blockers, resource risks, and recommendations
- **What-if Simulation**: Analyze the impact of resource unavailability
- **Load Redistribution Planning**: Get AI recommendations for balancing workloads

## Setup Instructions

### 1. Installation
Install the required dependencies:
```bash
pip install -r requirements-streamlit.txt
```

### 2. Configuration
Set up your OpenAI API key:
- Create a `.streamlit/secrets.toml` file with the following content:
```toml
openai_api_key = "your-api-key-here"
```

### 3. Running the App
```bash
streamlit run app.py
```

### 4. Data Import
The app works with Excel files exported from JIRA with the following structure:
- **Issues**: Task details with Start Date, Due Date, Assignee, Status, etc.
- **Worklogs**: Time tracking data with Resource, Date, Time Spent
- **Skills**: Resource skillset mapping
- **Non_Availability**: Resource leave/unavailability data

A sample data file is included (`enriched_jira_project_data.xlsx`) for testing purposes.

## Streamlit Cloud Deployment
This application is ready for deployment on Streamlit Cloud:
1. Push the code to a GitHub repository
2. Connect your Streamlit Cloud account
3. Create a new app pointing to your repository
4. Add your OpenAI API key in the Streamlit Cloud secrets management

## License
MIT License