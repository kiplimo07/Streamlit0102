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
.big-font { font-size:50px !important; font-weight: bold; color: white; }
.medium-font { font-size:35px !important; color: #a47321; }
.small-font { font-size:25px !important; color: white; }
.reportview-container .main { background-color: #1d262f; }
.sidebar .sidebar-content { background-color: #1d262f; color: white; }
.fa { padding-right: 5px; }
</style>
""", unsafe_allow_html=True)

# Header and subheader
st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">PORTFOLIO</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">Full Stack Senior Data Analyst</p>', unsafe_allow_html=True)

# Sidebar navigation setup
with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("", ["Welcome", "Data Analytics / Engagement & Monetization Strategies", 
                         "Dashboard / Executive Business Insights", 
                         "Data Analysis / Warehouse & GL Account Optimization", 
                         "Process Automation / Quarterly Royalty Management", 
                         "Scope of Skills", "Certifications", "Contact"])



# Define the assign_correct_bucket function
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

# Load the dataset with a corrected approach
@st.cache
def load_data(url):
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    data['games_played_bucket'] = data['games_played'].apply(assign_correct_bucket)
    # Include any other necessary data processing here
    return data

# Ensure the corrected URL for raw GitHub content is used
data_url = "https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv"
data = load_data(data_url)


# Main content based on the navigation
if page == "Welcome":
    st.markdown("### Welcome to my Portfolio")
    st.markdown("""
    As a Senior Data Analyst with a strong focus on integrating business strategy and transforming complex data into strategic assets, 
    I have evolved from intricate statistical analysis to advanced predictive modeling. My expertise lies in turning vast datasets into actionable insights, 
    positioning me ideally for a Full Stack Senior Data Analyst or Data Scientist role. Committed to pioneering data-driven research, 
    I aim to lead innovative strategies in a dynamic corporate setting. My goal is to drive organizational success and innovation by leveraging data intelligence for business growth and collaborative leadership.
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
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

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

    # Show the plot
    st.pyplot(fig)
    st.subheader(" ")
    # Assuming 'data' DataFrame is already loaded and processed with necessary columns
    # Group by criteria and calculate average dollars spent
    grouped_data = data.groupby(['region', 'platform', 'games_played_bucket', 'Event'])['dollars_spent'].mean().reset_index()

    # Pivot for heatmap
    heatmap_data = grouped_data.pivot("region", "platform", "dollars_spent")

    # Generate heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f")
    plt.title("Average Dollars Spent per Player by Region and Platform")
    plt.ylabel("Region")
    plt.xlabel("Platform")

    st.pyplot(plt)

    st.markdown("""
    **Heatmap Analysis:** The heatmap visualizes the average dollars spent per player across different regions and platforms. 
    It highlights that Platform 3, Region 1, has the highest spending, indicating a key segment for targeted marketing efforts to maximize ROI. 
    Conversely, Platform 1, Region 5 shows lower spending, suggesting a need for further investigation and tailored engagement strategies.
    """)

elif page == "Dashboard / Executive Business Insights":
    st.header("Dashboard / Executive Business Insights")
    st.markdown("""
    **Objective:** Enhance strategic decision-making through a unified data ecosystem post-merger. Focus on leveraging analytics to drive stakeholder value and operational efficiency.
    
    **Findings:** Highlighted divisions and accounts showing promising performance, indicating opportunities for strategic realignment and resource optimization.
    
    **Methodology:** Utilized Python for data manipulation and SQL for data querying. Employed Power BI for dynamic dashboards showcasing real-time business intelligence.
    """)


elif page == "Data Analysis / Warehouse & GL Account Optimization":
    st.header("Data Analysis / Warehouse & GL Account Optimization")
    st.markdown("""
    **Objective:** Identify cost-saving opportunities across logistics and warehouse operations to impact the bottom line positively.
    
    **Findings:** Revealed inefficiencies in 'SKYLAB' and '3PL Logistics', suggesting areas for cost optimization and process improvements.
    
    **Methodology:** Analyzed financial data using Python, with a focus on dissecting spending patterns and identifying optimization opportunities.
    """)

elif page == "Process Automation / Quarterly Royalty Management":
    st.header("Process Automation / Quarterly Royalty Management")
    st.markdown("""
    **Objective:** Streamline the quarterly royalty management process, reducing time spent by financial analysts from a month-long task to a 2-hour automated process.
    
    **Impact:** Achieved an 85% reduction in process time, significantly lowering operational costs and enhancing efficiency and accuracy in royalty management.
    
    **Methodology:** Developed a custom Python script for data consolidation and utilized Excel VBA for automating data extraction and report generation.
    """)


elif page == "Scope of Skills":
    st.header("Scope of Skills")
    st.markdown("""
    - **Programming Languages:** Proficient in Python and VBA.
    - **Data Engineering Tools:** Experienced with ETL processes, SSMS, and Snowflake.
    - **Data Analysis Libraries:** Skilled in using Pandas, NumPy, Seaborn, and Matplotlib.
    - **BI Tools:** Proficient in Power BI, Google Analytics, and Data Studio.
    - **Digital Marketing:** Knowledgeable in campaign management and optimization across platforms like Facebook and Google Ads.
    """)

elif page == "Certifications":
    st.header("Certifications")
    st.markdown("""
    - **Big Data Technology Fundamentals** - AWS
    - **AWS Cloud Practitioner Essentials** - AWS
    - **Analyzing and Visualizing Data with Power BI** - EdX
    """)

elif page == "Contact":
    st.header("Contact Information")
    st.markdown("""
    Feel free to connect with me for any inquiries or opportunities.
    
    - **Phone:** (626) 203 – 3319
    - **Email:** [jason.chang01022021@gmail.com](mailto:jason.chang01022021@gmail.com)
    - **LinkedIn:** [linkedin.com/in/jchang0102](https://linkedin.com/in/jchang0102)
    """, unsafe_allow_html=True)

