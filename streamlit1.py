import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def layout_wrapper(content_func):
    # Define a container for the main content
    main_container = st.container()
    # Define a container for extra space on the right (if needed)
    right_space = st.sidebar.container()

    with main_container:
        content_func()
    
    # Adjust the width of the right_space or add elements here as needed
    with right_space:
        st.write("3")  # Adjust based on need
        
st.set_page_config(layout="wide", page_title="Jason Chang's Portfolio")
st.markdown("""
<link href='https://fonts.googleapis.com/css?family=Bebas+Neue|Lato&display=swap' rel='stylesheet'>
<style>
.big-font { font-family: 'Bebas Neue', cursive; font-size:70px !important; font-weight: 400; color: Black; }
.medium-font { font-family: 'Bebas Neue', cursive; font-size:40px !important; font-weight: bold; color: #D09E55; }
.small-font { font-family: 'Lato', sans-serif; font-size:30px !important; color: Black; }
.reportview-container .main { background-color: #1D262F; }
.sidebar .sidebar-content { background-color: #1D262F; color: white; }
.fa { padding-right: 5px; }
/* Adjust top padding of the main container for all pages */
.reportview-container .main .block-container { padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">PORTFOLIO</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">Full Stack Senior Data Analyst</p>', unsafe_allow_html=True)




with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("", ["Welcome", "Data Analytics / Engagement & Monetization Strategies", "Dashboard / Executive Business Insights", "Data Analysis / Warehouse & GL Account Optimization", "Process Automation / Quarterly Royalty Management", "Scope of Skills", "Certifications", "Contact"])

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




if page == "Welcome":
    content_col, spacer_col = st.columns([0.80, 0.20])  # Adjust the ratio based on your preference
    st.markdown("### Welcome to My Portfolio")
    st.markdown("""
    As a Senior Data Analyst with a strong focus on integrating business strategy and transforming complex data into strategic assets, I have evolved from intricate statistical analysis to advanced predictive modeling. My expertise lies in turning vast datasets into actionable insights. Committed to pioneering data-driven research, I aim to lead innovative strategies in a dynamic corporate setting. My goal is to drive organizational success and innovation by leveraging data intelligence for business growth and collaborative leadership.
    """)

if page == "Data Analytics / Engagement & Monetization Strategies":
 
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
    # Displaying the third image with a wider width
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/333', caption='Average Spending by Number of Games Played: Event 1 vs Event 2', width=600)
    # Displaying the first two images side by side if screen allows
    col1, col2 = st.columns([1, 1])  # Adjust the ratio if needed
 
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/111', caption='Distribution of Spending Across Skill Brackets', width=600)

    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/222', caption='Day-by-Day Churn Rate: Event 1 vs Event 2', width=600)

    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Leveraged Python, K-Means Clustering, and heatmap analysis for an in-depth comparative study of player engagement and spending. Implemented segmentation based on in-game behavior for a comprehensive analysis.
    """)

   

    # Adjusting the width for the last three images
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/444', width=1000)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/555', width=1000)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/666', width=1000)



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
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=.5)
    plt.title("Average Dollars Spent per Player by Region and Platform")
    st.pyplot(plt)

    st.subheader("Conclusion and Strategic Insights:")
    st.write("""
    The analysis provides actionable insights into how player engagement and spending behaviors vary across different segments. By focusing on the high-value segments identified, targeted strategies can be developed to enhance player retention and increase revenue. Additionally, understanding the factors driving player churn during event periods can inform more effective engagement strategies for future events.
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






