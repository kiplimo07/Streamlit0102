import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the wide layout and page title
st.set_page_config(layout="wide", page_title="Jason Chang's Portfolio")

# Function to set the background color of the main content area to a specific shade of light blue
def set_background_color():
    st.markdown("""
    <style>
    body {
        background-color: #F2F9FF !important;
    }
    .reportview-container .main {
        background-color: #F2F9FF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Apply the custom CSS to set the background color
set_background_color()

# Additional styles and fonts
st.markdown("""
<link href='https://fonts.googleapis.com/css?family=Bebas+Neue|Lato&display=swap' rel='stylesheet'>
<style>
.reportview-container .main .block-container { padding-right: 10% !important; }
.big-font { font-family: 'Bebas Neue', sans-serif; font-size: 94px !important; font-weight: 100; color: #3e4047; display: inline-block; margin: 0 auto; margin-top: -40px; }
.big2-font { font-family: 'Bebas Neue', sans-serif; font-size: 60px !important; font-weight: 100; color: #3e4047; display: inline-block; margin-bottom: 0px; margin-top: 20px; }
.med2-font { font-family: 'Bebas Neue', sans-serif; font-size: 26px !important; font-weight: 100; color: #D09E55; margin-top: -20px; }
.medium-font { font-family: 'Bebas Neue', sans-serif; font-size: 38px !important; font-weight: 100; color: #D09E55; }
.small-font { font-family: 'Lato', sans-serif; font-size: 30px !important; color: #282D33; }
.streamlit-container .markdown-text-container, .streamlit-container .markdown-text-container p, .streamlit-container .markdown-text-container li { font-family: 'Lato', sans-serif !important; font-size: 30px !important; color: #282D33; }
.reportview-container .main { background-color: #F2F9FF; }
.sidebar .sidebar-content { background-color: #1D262F; color: white; }
.fa { padding-right: 4px; }
hr { border-top: 1px solid #FFFFFF; width: 95%; margin-left: 0;margin-top: 5px;}
</style>
""", unsafe_allow_html=True)

# JavaScript for UI interaction remains the same
st.markdown(
    """
    <script>
    const navButtons = document.querySelectorAll('.stRadio > div');
    navButtons.forEach(button => {
        button.addEventListener('click', () => {
            window.scrollTo(0, 0);
        });
    });
    </script>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("", ["WELCOME", "DATA ANALYTICS / ENGAGEMENT & MONETIZATION", "DASHBOARD / EXECUTIVE BUSINESS INSIGHTS", "DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION", "PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT", "SCOPE OF SKILLS", "CERTIFICATIONS", "LET'S CONNECT"])

@st.cache
def load_data(url):
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    data['games_played_bucket'] = data['games_played'].apply(assign_correct_bucket)
    return data

def assign_correct_bucket(games_played):
    if games_played >= 1 and games_played <= 3: return 'Very Low'
    elif games_played >= 4 and games_played <= 5: return 'Low'
    elif games_played >= 6 and games_played <= 9: return 'Medium'
    elif games_played >= 10 and games_played <= 68: return 'High'
    else: return 'Unknown'

data_url = "https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv"
data = load_data(data_url)

if page == "WELCOME":
    # Custom markdown for titles and subtitles only on the WELCOME page
    st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
    st.markdown('<div><p class="big2-font">PORTFOLIO</p><hr></div>', unsafe_allow_html=True)
    st.markdown('<p class="med2-font">Full Stack Senior Data Analyst</p>', unsafe_allow_html=True)

    content_col, spacer_col = st.columns([0.50, 0.50])  # Adjust the ratio based on your preference
    st.markdown("### Welcome to My Portfolio")
    st.markdown("""As a Senior Data Analyst with a strong focus on integrating business strategy and transforming complex data into strategic assets, I have evolved from intricate statistical analysis to advanced predictive modeling. My expertise lies in turning vast datasets into actionable insights. Committed to pioneering data-driven research, I aim to lead innovative strategies in a dynamic corporate setting. My goal is to drive organizational success and innovation by leveraging data intelligence for business growth and collaborative leadership.""")

# The rest of your code for other pages...

elif page == "DATA ANALYTICS / ENGAGEMENT & MONETIZATION":
 
    st.header("DATA ANALYTICS / ENGAGEMENT & MONETIZATION")
    st.subheader("Situation")
    st.write("""
    In an effort to maximize revenue and enhance player engagement and satisfaction in Warcraft, we identified the need to analyze player behavior and spending patterns during two key in-game events. The primary challenge was understanding how different segments of players interacted with these events and identifying opportunities to improve both engagement and monetization.
    """)

    st.subheader("Task")
    st.write("""
    My task was to lead the data analytics process, focusing on:

Identifying high-spending player segments for targeted promotions.
Understanding low spending trends in specific regions and platforms for strategic adjustments.
Conducting exploratory data analysis to grasp player spending behaviors related to games played, skill levels, dollars spent, and items crafted.
    """)

    st.subheader("Action")
    st.write("""
 Data Exploration and Analysis:
Conducted comprehensive exploratory data analysis to investigate player spending behavior, employing Python for data manipulation and analysis.
Utilized K-Means Clustering to segment players based on their in-game behavior, focusing on engagement metrics like games played, skill levels, and spending.
Performed heatmap analysis to identify patterns of player engagement and spending during the events, facilitating a comparative study between different segments.
Strategic Implementation:
Identified high-spending segments in Platform 3, Region 1 as a priority for future promotions, based on their significant contribution to revenue.
Highlighted low spending in Platform 1, Region 5, indicating the need for further research and strategic adjustment to improve engagement and spending in this segment.

    """)
    # Displaying the third image with a wider width
    col1, col2 = st.columns([1, 1,])  # Adjust the ratio if needed
 
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/333', width=480)




    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/222', width=480)

    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Leveraged Python, K-Means Clustering, and heatmap analysis for an in-depth comparative study of player engagement and spending. Implemented segmentation based on in-game behavior for a comprehensive analysis.
    """)
    col1, col2 = st.columns([1, 1,])  # Adjust the ratio if needed
 
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/777', caption='Distribution of Spending Across Skill Brackets', width=480)

    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/111', caption='Day-by-Day Churn Rate: Event 1 vs Event 2', width=480)

   

   

    # Adjusting the width for the last three images
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/444', width=900)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/555', width=900)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/666', width=900)



    ##




    event_1_start, event_1_end = pd.Timestamp('2017-01-24'), pd.Timestamp('2017-02-14')
    event_2_start, event_2_end = pd.Timestamp('2017-02-28'), pd.Timestamp('2017-03-21')

    event_1_data = data[(data['Date'] >= event_1_start) & (data['Date'] <= event_1_end)]
    event_2_data = data[(data['Date'] >= event_2_start) & (data['Date'] <= event_2_end)]

    sns.set_style("whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(8, 6)) # Adjusted for a common width of 1300 pixels

    sns.kdeplot(event_1_data['games_played'], shade=True, color="skyblue", label="Event 1", ax=axes[0, 0])
    sns.kdeplot(event_2_data['games_played'], shade=True, color="salmon", label="Event 2", ax=axes[0, 0])
    axes[0, 0].set_title('Distribution of Games Played')

    sns.kdeplot(event_1_data['skill_last'], shade=True, color="skyblue", label="Event 1", ax=axes[0, 1])
    sns.kdeplot(event_2_data['skill_last'], shade=True, color="salmon", label="Event 2", ax=axes[0, 1])
    axes[0, 1].set_title('Distribution of Skill Last')

    sns.kdeplot(event_1_data['items_crafted'], shade=True, color="skyblue", label="Event 1", ax=axes[1, 0])
    sns.kdeplot(event_2_data['items_crafted'], shade=True, color="salmon", label="Event 2", ax=axes[1, 0])
    axes[1, 0].set_title('Distribution of Items Crafted')

    sns.kdeplot(event_1_data['dollars_spent'], shade=True, color="skyblue", label="Event 1", ax=axes[1, 1])
    sns.kdeplot(event_2_data['dollars_spent'], shade=True, color="salmon", label="Event 2", ax=axes[1, 1])
    axes[1, 1].set_title('Distribution of Dollars Spent')




    plt.tight_layout()
    st.pyplot(fig)



    heatmap_data = data.groupby(['region', 'platform']).dollars_spent.mean().unstack()
    plt.figure(figsize=(8, 6)) # Adjusted for a common width of 1000 pixels
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=.4)
    plt.title("Average Dollars Spent per Player by Region and Platform")
    st.pyplot(plt)




    st.subheader("Result")
    st.write("""
        The data-driven approach yielded actionable insights, enabling the development of targeted strategies to enhance player retention and increase revenue. Specifically:

A 21% increase in player engagement and spending in the identified high-value segments through targeted promotions and tailored in-game events.
Initiated a strategic review and adjustment for underperforming segments, resulting in a marked improvement in player satisfaction and reduced churn rate by 15% during subsequent events.
    """)
    
    # Adding the final image at the correct indentation level
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', width=850)


elif page == "DASHBOARD / EXECUTIVE BUSINESS INSIGHTS":
    st.header("DASHBOARD / EXECUTIVE BUSINESS INSIGHTS")
    
    st.subheader("Objective:")
    st.markdown("""
    Enhance strategic decision-making through a unified data ecosystem post-merger. Focus on leveraging analytics to drive stakeholder value and operational efficiency.
    """, unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', width=950)
    
    st.subheader("Findings:")
    st.markdown("""
    Highlighted divisions and accounts showing promising performance, indicating opportunities for strategic realignment and resource optimization.
    """, unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', width=950)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', width=950)
    
    st.subheader("Methodology:")
    st.markdown("""
    Utilized Python for data manipulation and SQL for data querying. Employed Power BI for dynamic dashboards showcasing real-time business intelligence.
    """, unsafe_allow_html=True)


elif page == "DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION":
    st.header("DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION")
    
    st.subheader("Objective:")
    st.markdown("""
    Identify cost-saving opportunities across logistics and warehouse operations to impact the bottom line positively.
    """, unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', width=950)
    
    st.subheader("Findings:")
    st.markdown("""
    Revealed inefficiencies in 'SKYLAB' and '3PL Logistics', suggesting areas for cost optimization and process improvements.
    """, unsafe_allow_html=True)
    
    st.subheader("Methodology:")
    st.markdown("""
    Analyzed financial data using Python, with a focus on dissecting spending patterns and identifying optimization opportunities.
    """, unsafe_allow_html=True)


elif page == "PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT":
    st.header("PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT")
    
    # Objective
    st.subheader("Objective:")
    st.markdown("""
Streamline the quarterly royalty management process, reducing time spent by financial analysts from a month-long task to a 2-hour automated process.
    """, unsafe_allow_html=True)

    # Python Section
    st.markdown("#### PYTHON", unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', width=950)

    # VBA Section
    st.markdown("#### VBA", unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', width=950)
    
    # Impact
    st.subheader("Impact:")
    st.markdown("""
Achieved an 85% reduction in process time, significantly lowering operational costs and enhancing efficiency and accuracy in royalty management.
    """, unsafe_allow_html=True)
    
    # Methodology
    st.subheader("Methodology:")
    st.markdown("""
Developed a custom Python script for data consolidation and utilized Excel VBA for automating data extraction and report generation.
    """, unsafe_allow_html=True)





if page == "SCOPE OF SKILLS":
    st.header("SCOPE OF SKILLS")
    
    st.markdown("#### Programming Languages:", unsafe_allow_html=True)
    st.markdown("*Proficient in Python and VBA.*", unsafe_allow_html=True)
    
    st.markdown("#### Data Engineering Tools:", unsafe_allow_html=True)
    st.markdown("*Experienced in ETL, SSMS, AS400, Snowflakes, Power Query, System Integration Analysis.*", unsafe_allow_html=True)
    
    st.markdown("#### Data Analysis Libraries:", unsafe_allow_html=True)
    st.markdown("*Skilled in using Pandas, NumPy, Seaborn, Matplotlib, Openpyxl, SciPy, TensorFlow.*", unsafe_allow_html=True)
    
    st.markdown("#### Statistical Analysis:", unsafe_allow_html=True)
    st.markdown("*Descriptive/Inferential Statistics, A/B Testing, Predictive Modeling, Forecasting, Regression Analysis, Hypothesis Testing, & Time Series Analysis.*", unsafe_allow_html=True)
    
    st.markdown("#### BI Tools:", unsafe_allow_html=True)
    st.markdown("*Proficient in Power BI, Google Analytics, and Data Studio.*", unsafe_allow_html=True)
    
    st.markdown("#### Digital Marketing:", unsafe_allow_html=True)
    st.markdown("*Facebook, Google Ads, Shopify, Google Analytics, Data Studio, Campaign Management, Performance and Content Optimization.*", unsafe_allow_html=True)
    
    st.markdown("#### Data Modeling:", unsafe_allow_html=True)
    st.markdown("*STAR/ER/DAG diagrams, and Normalization.*", unsafe_allow_html=True)




elif page == "CERTIFICATIONS":
    st.header("**CERTIFICATIONS**")
    st.subheader(" Big Data Technology Fundamentals - AWS")
    st.subheader(" AWS Cloud Practitioner Essentials - AWS")
    st.subheader(" Analyzing and Visualizing Data with Power BI - EdX")

elif page == "LET'S CONNECT":
    st.header("LET'S CONNECT!!")
    st.markdown("""
    Feel free to connect with me for any inquiries or opportunities.
    <br><br>
    <img src="https://img.icons8.com/material-rounded/48/000000/phone--v1.png" alt="phone_icon" style="vertical-align:middle; width:35px; height:35px;"> <span style="font-size:20px; vertical-align:middle;">**Phone:** (626) 203 – 3319</span>
    <br>
    <img src="https://img.icons8.com/material-outlined/48/000000/email--v1.png" alt="email_icon" style="vertical-align:middle; width:35px; height:35px;"> <span style="font-size:20px; vertical-align:middle;">**Email:** jason.chang01022021@gmail.com</span>
    <br>
    <img src="https://img.icons8.com/material-rounded/48/000000/linkedin--v1.png" alt="linkedin_icon" style="vertical-align:middle; width:35px; height:35px;"> <span style="font-size:20px; vertical-align:middle;">**LinkedIn:** linkedin.com/in/jchang0102</span>
    <br>
    <img src="https://img.icons8.com/material-outlined/48/000000/map-pin.png" alt="location_icon" style="vertical-align:middle; width:35px; height:35px;"> <span style="font-size:20px; vertical-align:middle;">**Location:** Irvine, CA</span>
    """, unsafe_allow_html=True)
