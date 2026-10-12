import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from st_link_analysis.component.icons import SUPPORTED_ICONS
import json

st.set_page_config(layout="wide")

# st.write(", ".join(SUPPORTED_ICONS))

# Load the data
with open("./data/network.json", "r") as f:
    elements = json.load(f)

node_styles = [
    NodeStyle("COMPANY", "#309A60", "name", "person"),
    NodeStyle("PERSON", "#2A629A", "name", "business"),
]

edge_styles = [
    EdgeStyle("FOUNDER", labeled=True, directed=True),
    EdgeStyle("CEO", labeled=True, directed=True),
    EdgeStyle("EMPLOYEE", labeled=True, directed=True),
]

layout = {"name": "cose", "animate": "end", "nodeDimensionsIncludeLabels": False}

st_link_analysis(
    elements, node_styles=node_styles, edge_styles=edge_styles,
    layout=layout, key="xyz"
)
