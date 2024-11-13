import pandas as pd
from web_search_utils import web_search


def load_csv(file):
    """Load the CSV file into a pandas DataFrame"""
    return pd.read_csv(file)


def fetch_data(data, column_name, query_template):
    """Fetch search results for each entity from the specified column of the DataFrame using a web search"""
    entities = data[column_name].tolist()

    results = []

    for entity in entities:
        query = query_template.format(entity=entity)
        search_results = web_search(query)
        results.append({"entity": entity, "search_results": search_results})

    return results
