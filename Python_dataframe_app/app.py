import streamlit as st
import pandas as pd

# 1. Cache the loaded data
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Load Titanic dataset
file = "data/titanic.csv"
df = load_data(file)

# 2. Define widget layout configuration
create_data = {
    "Name": "text",
    "Sex": "multiselect",
    "Embarked": "multiselect",
    "Ticket": "text",
    "Pclass": "multiselect"
}

# 3. Dynamic Widget Builder & Filtering Logic
filtered_df = df.copy()

st.sidebar.header("Filter Options")

for column, widget_type in create_data.items():
    if column in df.columns:
        if widget_type == "text":
            search_term = st.sidebar.text_input(f"Search {column}", value="")
            if search_term:
                filtered_df = filtered_df[filtered_df[column].astype(str).str.contains(search_term, case=False, na=False)]
                
        elif widget_type == "multiselect":
            unique_options = df[column].dropna().unique().tolist()
            selected_options = st.sidebar.multiselect(f"Select {column}", options=unique_options, default=unique_options)
            if selected_options:
                filtered_df = filtered_df[filtered_df[column].isin(selected_options)]

# 4. Display UI Outputs
st.title("Streamlit AutoPandas (Native Solution)")

st.header("Original DataFrame")
st.dataframe(df, use_container_width=True)

st.header("Result DataFrame")
st.dataframe(filtered_df, use_container_width=True)
