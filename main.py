import streamlit as st
from data_utils import load_csv, fetch_data
from llm_utils import process_data_with_gemini
import pandas as pd

st.title("AI Data Retrieval Agent")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

selected_column = None

if uploaded_file:
    data = load_csv(uploaded_file)
    column_options = data.columns.tolist()
    selected_column = st.selectbox("Select the main column for entities", options=column_options)
else:
    data = None
    column_options = []
    selected_column = st.selectbox("Select the main column for entities", options=column_options)

query_template = st.text_input("Custom Query Prompt (use {entity} as placeholder)")

if data is not None:
    st.write("Data Preview:")
    st.write(data.head())

    if st.button("Run Query"):
        if query_template and selected_column:
            results = fetch_data(data, selected_column, query_template)
            processed_results = process_data_with_gemini(results, query_template)
            st.write("Results:")
            st.write(processed_results)

            st.download_button("Download Results as CSV", pd.DataFrame(processed_results).to_csv(index=False), file_name="results.csv")
        else:
            st.error("Please provide both a query template and select a main column.")