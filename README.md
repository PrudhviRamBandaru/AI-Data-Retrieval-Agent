# AI Data Retrieval Agent

This project is an AI-powered data retrieval agent designed to automate web searches and extract information for a list of entities provided in a CSV or Google Sheet. Using Streamlit for the interface, the agent allows users to upload datasets, specify custom queries, and receive structured information extracted from web results using SerpAPI and the Gemini API.

## Features

- **CSV/Google Sheets Upload**: Upload a CSV file or link to a Google Sheet to fetch a dataset.
- **Dynamic Query Input**: Customize a query prompt with placeholders for each entity.
- **Automated Web Search**: For each entity, the agent conducts web searches based on the provided query template.
- **LLM-Based Data Extraction**: Uses the Gemini API for parsing and extracting structured information from web results.
- **Download Results**: View and download extracted information in CSV format.

## Project Setup

### Prerequisites

- **Python 3.x**
- **API Keys**: Set up accounts and API keys for:
  - [SerpAPI](https://serpapi.com/)
  - [Google Gemini API](https://cloud.google.com/)

### Running the Application

- **Clone this Repository**
```bash
https://github.com/PrudhviRamBandaru/AI-Data-Retrieval-Agent.git
```

- **Navigate into the project directory**
```bash
cd ai-data-retrieval-agent
```

- **Start the Streamlit app**
```bash
python -m streamlit run main.py
```

### Video Link
https://drive.google.com/file/d/1sWDNR3svyL04TXoyr_AY7Xu4O6233dIq/view?usp=sharing
