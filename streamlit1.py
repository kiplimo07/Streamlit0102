 import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the page configuration and custom CSS
st.set_page_config(layout="wide", page_title="Jason Chang's Portfolio")
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.big-font { font-size:50px !important; font-weight: bold; color: white; }
.medium-font { font-size:35px !important; color: #a47321; }
.small-font { font-size:25px !important; color: white; }
.reportview-container .main { background-color: #1d262f; }
.sidebar .sidebar-content { background-color: #1d262f; color: white; }
.fa { padding-right: 5px; }
</style>
""", unsafe_allow_html=True)

# Header and sidebar setup
st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">PORTFOLIO</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">Full Stack Senior Data Analyst</p>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("", ["Welcome", "Data Analytics / Engagement & Monetization Strategies", "Dashboard / Executive Business Insights", "Data Analysis / Warehouse & GL Account Optimization", "Process Automation / Quarterly Royalty Management", "Scope of Skills", "Certifications", "Contact"])

# Data loading and preprocessing
@st.cache
def load_data(url):
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    data['games_played_bucket'] = data['games_played'].apply(assign_correct_bucket)
    return data

def assign_correct_bucket(games_played):
    if games_played >= 1 and games_played <= 3:
        return 'Very Low'
    elif games_played >= 4 and games_played <= 5:
        return 'Low'
    elif games_played >= 6 and games_played <= 9:
        return 'Medium'
    elif games_played >= 10 and games_played <= 68:
        return 'High'
    else:
        return 'Unknown'

data_url = "https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv"
data = load_data(data_url)



# Main content based on the navigation
if page == "Welcome":
    st.markdown("###Portfolio")
    st.markdown("###Full Stack Data Analyst")
    # Welcome page content here
    st.write("""
    As a Senior Data Analyst with a strong focus on integrating business strategy and transforming complex data into strategic assets, I have evolved from intricate statistical analysis to advanced predictive modeling. My expertise lies in turning vast datasets into actionable insights, positioning me ideally for a Full Stack Senior Data Analyst or Data Scientist role. Committed to pioneering data-driven research, I aim to lead innovative strategies in a dynamic corporate setting. My goal is to drive organizational success and innovation by leveraging data intelligence for business growth and collaborative leadership.
    """)
