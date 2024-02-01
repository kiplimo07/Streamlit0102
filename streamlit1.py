import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the page configuration to wide mode with a dark theme
st.set_page_config(layout="wide")

# Custom CSS to incorporate the design from the image and FontAwesome for icons
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.big-font {
    font-size:50px !important;
    font-weight: bold;
    color: white;
}
.medium-font {
    font-size:35px !important;
    color: white;
}
.small-font {
    font-size:25px !important;
    color: white;
}
.reportview-container .main {
    background-color: #1E1E1E;
}
.sidebar .sidebar-content {
    background-color: #262730;
    color: white;
}
.fa {
    padding-right: 5px;
}
</style>
""", unsafe_allow_html=True)

# Header and subheader
st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">PROJECT PORTFOLIO</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">SENIOR DATA ANALYST</p>', unsafe_allow_html=True)


# Sidebar navigation with 'Certifications' page
with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("", ["Welcome", "Data Analytics / Engagement & Monetization Strategies", 
                         "Dashboard / Executive Business Insights", 
                         "Data Analysis / Warehouse & GL Account Optimization", 
                         "Process Automation / Quarterly Royalty Management", 
                         "Scope of Skills", "Certifications", "Contact"])

# Main content based on the navigation
if page == "Welcome":
    st.markdown("### Welcome to my page")
    
    # Your professional introduction
    st.write("""
    As a Senior Data Analyst with a strong focus on integrating business strategy and transforming complex data into strategic assets, I have evolved from intricate statistical analysis to advanced predictive modeling. My expertise lies in turning vast datasets into actionable insights, positioning me ideally for a Full Stack Senior Data Analyst or Data Scientist role. Committed to pioneering data-driven research, I aim to lead innovative strategies in a dynamic corporate setting. My goal is to drive organizational success and innovation by leveraging data intelligence for business growth and collaborative leadership.
    """)


elif page == "Data Analytics / Engagement & Monetization Strategies":
    st.header("Data Analytics / Engagement & Monetization Strategies")
    st.subheader("Executive Summary/Business Objective:")
    st.write("""
    Emphasized maximizing revenue and enhancing player engagement and satisfaction by analyzing behavior and spending patterns during Warcraft's two in-game events.
    """)
    st.subheader("Findings/Strategic Implications:")
    st.write("""
    Identified high-spending segments, especially in Platform 3, Region 1, signaling a priority for future promotions. Observed low spending in Platform 1, Region 5, highlighting the necessity for further research and adjustments to the strategy.
    """)
    st.subheader("Research Question/Data Exploration:")
    st.write("""
    Conducted exploratory data analysis to understand player spending behavior, emphasizing games played, skill levels, dollars spent, and items crafted.
    """)
    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Leveraged Python, K-Means Clustering, and heatmap analysis for an in-depth comparative study of player engagement and spending. Implemented segmentation based on in-game behavior for a comprehensive analysis.
    """)

    # Load the dataset from the GitHub URL
    @st.cache
    def load_data(url):
        data = pd.read_csv(url)
        data['Date'] = pd.to_datetime(data['Date'])
        return data

    data_url = "https://github.com/jasonchang0102/Streamlit0102/raw/main/RAWBliz.csv"
    data = load_data(data_url)

    # Define the event periods
    event_1_start = pd.Timestamp('2017-01-24')
    event_1_end = pd.Timestamp('2017-02-14')
    event_2_start = pd.Timestamp('2017-02-28')
    event_2_end = pd.Timestamp('2017-03-21')

    # Filter the data for each event
    event_1_data = data[(data['Date'] >= event_1_start) & (data['Date'] <= event_1_end)]
    event_2_data = data[(data['Date'] >= event_2_start) & (data['Date'] <= event_2_end)]

    # Set the aesthetic style of the plots
    sns.set_style("whitegrid")

    # Create figure for all four distributions
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Kernel Density Estimate plot for Games Played
    sns.kdeplot(event_1_data['games_played'], color="skyblue", shade=True, label="Event 1", ax=axes[0, 0])
    sns.kdeplot(event_2_data['games_played'], color="salmon", shade=True, label="Event 2", ax=axes[0, 0])
    axes[0, 0].set_title('Bell Curve Distribution of Games Played')
    axes[0, 0].legend()

    # Kernel Density Estimate plot for Skill Last
    sns.kdeplot(event_1_data['skill_last'], color="skyblue", shade=True, label="Event 1", ax=axes[0, 1])
    sns.kdeplot(event_2_data['skill_last'], color="salmon", shade=True, label="Event 2", ax=axes[0, 1])
    axes[0, 1].set_title('Bell Curve Distribution of Skill Last')
    axes[0, 1].legend()

    # Kernel Density Estimate plot for Items Crafted
    sns.kdeplot(event_1_data['items_crafted'], color="skyblue", shade=True, label="Event 1", ax=axes[1, 0])
    sns.kdeplot(event_2_data['items_crafted'], color="salmon", shade=True, label="Event 2", ax=axes[1, 0])
    axes[1, 0].set_title('Bell Curve Distribution of Items Crafted')
    axes[1, 0].legend()

    # Kernel Density Estimate plot for Dollars Spent
    sns.kdeplot(event_1_data['dollars_spent'], color="skyblue", shade=True, label="Event 1", ax=axes[1, 1])
    sns.kdeplot(event_2_data['dollars_spent'], color="salmon", shade=True, label="Event 2", ax=axes[1, 1])
    axes[1, 1].set_title('Bell Curve Distribution of Dollars Spent')
    axes[1, 1].legend()

    # Adjust the layout
    plt.tight_layout()
    
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the page configuration to wide mode with a dark theme
st.set_page_config(layout="wide")

# Custom CSS to incorporate the design from the image and FontAwesome for icons
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.big-font {
    font-size:50px !important;
    font-weight: bold;
    color: white;
}
.medium-font {
    font-size:35px !important;
    color: white;
}
.small-font {
    font-size:25px !important;
    color: white;
}
.reportview-container .main {
    background-color: #1E1E1E;
}
.sidebar .sidebar-content {
    background-color: #262730;
    color: white;
}
.fa {
    padding-right: 5px;
}
</style>
""", unsafe_allow_html=True)

# Header and subheader
st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">PROJECT PORTFOLIO</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">SENIOR DATA ANALYST</p>', unsafe_allow_html=True)


# Sidebar navigation with 'Certifications' page
with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("", ["Welcome", "Data Analytics / Engagement & Monetization Strategies", 
                         "Dashboard / Executive Business Insights", 
                         "Data Analysis / Warehouse & GL Account Optimization", 
                         "Process Automation / Quarterly Royalty Management", 
                         "Scope of Skills", "Certifications", "Contact"])

# Main content based on the navigation
if page == "Welcome":
    st.markdown("### Welcome to my page")
    
    # Your professional introduction
    st.write("""
    As a Senior Data Analyst with a strong focus on integrating business strategy and transforming complex data into strategic assets, I have evolved from intricate statistical analysis to advanced predictive modeling. My expertise lies in turning vast datasets into actionable insights, positioning me ideally for a Full Stack Senior Data Analyst or Data Scientist role. Committed to pioneering data-driven research, I aim to lead innovative strategies in a dynamic corporate setting. My goal is to drive organizational success and innovation by leveraging data intelligence for business growth and collaborative leadership.
    """)


elif page == "Data Analytics / Engagement & Monetization Strategies":
    st.header("Data Analytics / Engagement & Monetization Strategies")
    st.subheader("Executive Summary/Business Objective:")
    st.write("""
    Emphasized maximizing revenue and enhancing player engagement and satisfaction by analyzing behavior and spending patterns during Warcraft's two in-game events.
    """)
    st.subheader("Findings/Strategic Implications:")
    st.write("""
    Identified high-spending segments, especially in Platform 3, Region 1, signaling a priority for future promotions. Observed low spending in Platform 1, Region 5, highlighting the necessity for further research and adjustments to the strategy.
    """)
    st.subheader("Research Question/Data Exploration:")
    st.write("""
    Conducted exploratory data analysis to understand player spending behavior, emphasizing games played, skill levels, dollars spent, and items crafted.
    """)
    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Leveraged Python, K-Means Clustering, and heatmap analysis for an in-depth comparative study of player engagement and spending. Implemented segmentation based on in-game behavior for a comprehensive analysis.
    """)

    # Load the dataset from the GitHub URL
    @st.cache
    def load_data(url):
        data = pd.read_csv(url)
        data['Date'] = pd.to_datetime(data['Date'])
        return data

    data_url = "https://github.com/jasonchang0102/Streamlit0102/raw/main/RAWBliz.csv"
    data = load_data(data_url)

    # Define the event periods
    event_1_start = pd.Timestamp('2017-01-24')
    event_1_end = pd.Timestamp('2017-02-14')
    event_2_start = pd.Timestamp('2017-02-28')
    event_2_end = pd.Timestamp('2017-03-21')

    # Filter the data for each event
    event_1_data = data[(data['Date'] >= event_1_start) & (data['Date'] <= event_1_end)]
    event_2_data = data[(data['Date'] >= event_2_start) & (data['Date'] <= event_2_end)]

    # Set the aesthetic style of the plots
    sns.set_style("whitegrid")

    # Create figure for all four distributions
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Kernel Density Estimate plot for Games Played
    sns.kdeplot(event_1_data['games_played'], color="skyblue", shade=True, label="Event 1", ax=axes[0, 0])
    sns.kdeplot(event_2_data['games_played'], color="salmon", shade=True, label="Event 2", ax=axes[0, 0])
    axes[0, 0].set_title('Bell Curve Distribution of Games Played')
    axes[0, 0].legend()

    # Kernel Density Estimate plot for Skill Last
    sns.kdeplot(event_1_data['skill_last'], color="skyblue", shade=True, label="Event 1", ax=axes[0, 1])
    sns.kdeplot(event_2_data['skill_last'], color="salmon", shade=True, label="Event 2", ax=axes[0, 1])
    axes[0, 1].set_title('Bell Curve Distribution of Skill Last')
    axes[0, 1].legend()

    # Kernel Density Estimate plot for Items Crafted
    sns.kdeplot(event_1_data['items_crafted'], color="skyblue", shade=True, label="Event 1", ax=axes[1, 0])
    sns.kdeplot(event_2_data['items_crafted'], color="salmon", shade=True, label="Event 2", ax=axes[1, 0])
    axes[1, 0].set_title('Bell Curve Distribution of Items Crafted')
    axes[1, 0].legend()

    # Kernel Density Estimate plot for Dollars Spent
    sns.kdeplot(event_1_data['dollars_spent'], color="skyblue", shade=True, label="Event 1", ax=axes[1, 1])
    sns.kdeplot(event_2_data['dollars_spent'], color="salmon", shade=True, label="Event 2", ax=axes[1, 1])
    axes[1, 1].set_title('Bell Curve Distribution of Dollars Spent')
    axes[1, 1].legend()

    # Adjust the layout
    plt.tight_layout()
    
    # Show the KDE plots in Streamlit
    st.pyplot(fig)


















