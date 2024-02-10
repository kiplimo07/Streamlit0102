import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def layout_wrapper(content_func):
    main_container = st.container()
    right_space = st.sidebar.container()
    with main_container:
        content_func()
    with right_space:
        st.write("3")

st.set_page_config(layout="wide", page_title="Jason Chang's Portfolio")

st.markdown("""
<link href='https://fonts.googleapis.com/css?family=Bebas+Neue|Lato&display=swap' rel='stylesheet'>
<style>
.reportview-container .main .block-container { padding-right: 20% !important; }
.big-font { font-family: 'Bebas Neue', sans-serif; font-size: 120px !important; font-weight: 100; color: #3e4047; display: inline-block; max-width: 80%; margin: 0 auto; }
.big2-font { font-family: 'Bebas Neue', sans-serif; font-size: 70px !important; font-weight: 100; color: #3e4047; display: inline-block; margin-bottom: 0px; }
.med2-font { font-family: 'Bebas Neue', sans-serif; font-size: 40px !important; font-weight: 100; color: #D09E55; }
.medium-font { font-family: 'Bebas Neue', sans-serif; font-size: 50px !important; font-weight: 100; color: #D09E55; }
.small-font { font-family: 'Lato', sans-serif; font-size: 30px !important; color: #282D33; }
.streamlit-container .markdown-text-container, .streamlit-container .markdown-text-container p, .streamlit-container .markdown-text-container li { font-family: 'Lato', sans-serif !important; font-size: 40px !important; color: #282D33; }
.reportview-container .main { background-color: #1D262F; }
.sidebar .sidebar-content { background-color: #1D262F; color: white; }
.fa { padding-right: 10px; }
hr { border-top: 2px solid #FFFFFF; width: 100%; margin-left: 0; margin-top: -20px; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
st.markdown('<div><p class="big2-font">PORTFOLIO</p><hr></div>', unsafe_allow_html=True)
st.markdown('<p class="med2-font">Full Stack Senior Data Analyst</p>', unsafe_allow_html=True)

st.markdown("""
<style>
/* Specifically target the main content block for padding adjustments */
.reportview-container .main .block-container {
    padding-top: 0 !important; /* Remove top padding */
    padding-right: 20% !important; /* Maintain right padding */
    padding-left: 20px !important; /* Adjust left padding as needed to ensure it doesn't shift content to the left */
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("",["WELCOME", "DATA ANALYTICS / ENGAGEMENT & MONETIZATION", "DASHBOARD / EXECUTIVE BUSINESS INSIGHTS", "DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION", "PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT", "SCOPE OF SKILLS", "CERTIFICATIONS", "LET'S CONNECT"])


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
    content_col, spacer_col = st.columns([0.50, 0.50])  # Adjust the ratio based on your preference
    st.markdown("### Welcome to My Portfolio")
    st.markdown("""    As a Senior Data Analyst with a strong focus on integrating business strategy and transforming complex data into strategic assets, I have evolved from intricate statistical analysis to advanced predictive modeling. My expertise lies in turning vast datasets into actionable insights. Committed to pioneering data-driven research, I aim to lead innovative strategies in a dynamic corporate setting. My goal is to drive organizational success and innovation by leveraging data intelligence for business growth and collaborative leadership.
    """)

elif page == "DATA ANALYTICS / ENGAGEMENT & MONETIZATION":
 
    st.header("DATA ANALYTICS / ENGAGEMENT & MONETIZATION")
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
    # Displaying the third image with a wider width
    col1, col2 = st.columns([1, 1,])  # Adjust the ratio if needed
 
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/333', width=550)




    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/222', width=550)

    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Leveraged Python, K-Means Clustering, and heatmap analysis for an in-depth comparative study of player engagement and spending. Implemented segmentation based on in-game behavior for a comprehensive analysis.
    """)
    col1, col2 = st.columns([1, 1,])  # Adjust the ratio if needed
 
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/777', caption='Distribution of Spending Across Skill Brackets', width=550)

    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/111', caption='Day-by-Day Churn Rate: Event 1 vs Event 2', width=550)

    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Leveraged Python, K-Means Clustering, and heatmap analysis for an in-depth comparative study of player engagement and spending. Implemented segmentation based on in-game behavior for a comprehensive analysis.
    """)

   

    # Adjusting the width for the last three images
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/444', width=1000)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/555', width=1000)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/666', width=1000)



    # Continue with Methodology/Analytical Proficiency and further analysis


    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Leveraged Python, K-Means Clustering, and heatmap analysis for an in-depth comparative study of player engagement and spending. Implemented segmentation based on in-game behavior for a comprehensive analysis.
    """)

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




    st.subheader("Conclusion and Strategic Insights:")
    st.write("""
        The analysis provides actionable insights into how player engagement and spending behaviors vary across different segments. By focusing on the high-value segments identified, targeted strategies can be developed to enhance player retention and increase revenue. Additionally, understanding the factors driving player churn during event periods can inform more effective engagement strategies for future events.
    """)
    
    # Adding the final image at the correct indentation level
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', width=800)


elif page == "DASHBOARD / EXECUTIVE BUSINESS INSIGHTS":
    st.header("DASHBOARD / EXECUTIVE BUSINESS INSIGHTS")
    
    st.subheader("Objective:")
    st.markdown("""
    Enhance strategic decision-making through a unified data ecosystem post-merger. Focus on leveraging analytics to drive stakeholder value and operational efficiency.
    """, unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', width=1000)
    
    st.subheader("Findings:")
    st.markdown("""
    Highlighted divisions and accounts showing promising performance, indicating opportunities for strategic realignment and resource optimization.
    """, unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', width=1000)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', width=1000)
    
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
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', width=1000)
    
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
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', width=900)

    # VBA Section
    st.markdown("#### VBA", unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', width=900)
    
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
    st.header("CERTIFICATIONS")
    st.subheader(" Big Data Technology Fundamentals - AWS")
    st.subheader(" AWS Cloud Practitioner Essentials - AWS")
    st.subheader(" Analyzing and Visualizing Data with Power BI - EdX")


elif page == "LET'S CONNECT":
    st.header("LET'S CONNECT!!")
    st.markdown("""
    Feel free to connect with me for any inquiries or opportunities.
    <br><br>
    <img src="https://img.icons8.com/material-rounded/24/000000/phone--v1.png" alt="phone_icon" style="vertical-align:middle; width:30px; height:30px;"> **Phone:** (626) 203 – 3319
    <br>
    <img src="https://img.icons8.com/material-outlined/24/000000/email--v1.png" alt="email_icon" style="vertical-align:middle; width:30px; height:30px;"> **Email:** [jason.chang01022021@gmail.com](mailto:jason.chang01022021@gmail.com)
    <br>
    <img src="https://img.icons8.com/material-rounded/24/000000/linkedin--v1.png" alt="linkedin_icon" style="vertical-align:middle; width:30px; height:30px;"> **LinkedIn:** [linkedin.com/in/jchang0102](https://linkedin.com/in/jchang0102)
    <br>
    <img src="https://img.icons8.com/material-outlined/24/000000/map-pin.png" alt="location_icon" style="vertical-align:middle; width:30px; height:30px;"> **Location:** Irvine, CA
    """, unsafe_allow_html=True)
