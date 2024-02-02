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
st.markdown('<p class="small-font">Full Stack Senior Data Analyst</p>', unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("", ["Welcome", "Data Analytics / Engagement & Monetization Strategies", 
                         "Dashboard / Executive Business Insights", 
                         "Data Analysis / Warehouse & GL Account Optimization", 
                         "Process Automation / Quarterly Royalty Management", 
                         "Scope of Skills", "Certifications", "Contact"])



# Main content based on the navigation
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

    st.subheader("Heatmap: Platform & Region x Player Engagement on Average Dollar Spending")

if page == "Welcome":
    st.markdown("### Welcome to my page")
    
    # Your professional introduction
    st.write("""
    As a Senior Data Analyst with a strong focus on integrating business strategy and transforming complex data into strategic assets, I have evolved from intricate statistical analysis to advanced predictive modeling. My expertise lies in turning vast datasets into actionable insights, positioning me ideally for a Full Stack Senior Data Analyst or Data Scientist role. Committed to pioneering data-driven research, I aim to lead innovative strategies in a dynamic corporate setting. My goal is to drive organizational success and innovation by leveraging data intelligence for business growth and collaborative leadership.
    """)



    # Summary of the Heatmap analysis

# ... [Previous Streamlit setup and Project 1 code] ...
elif page == "Dashboard / Executive Business Insights":
    st.header("Dashboard / Executive Business Insights")
    st.subheader("Executive Summary/Business Objective:")
    st.write("""
    Post-merger, the goal is to optimize financial performance by developing a 
    unified data ecosystem in SSMS. This aims to enhance strategic decision-making 
    and stakeholder value, focusing on creating a seamless data environment for dynamic 
    business intelligence.
    """)


    st.subheader("Findings/Strategic Implications:")
    st.write("""
    Analysis uncovers divisions and accounts with promising performance post-merger, 
    indicating opportunities for strategic realignment and efficiencies, leading to 
    potential resource reprioritization to maximize margins and cut costs.
    """)

    st.subheader("Background:")
    st.write("""
    Faced with the challenge of integrating disparate data systems from four pre-merger 
    companies, the aim was to combine these to maintain operational continuity and 
    capitalize on a unified market presence.
    """)

    st.subheader("Research Question/Data Exploration:")
    st.write("""
    Investigates how the merged data environment impacts financial health and 
    efficiency, involving a deep dive into Reverse Schema Building and analysis of 
    combined sales and operational data.
    """)

    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Utilizes advanced data analysis techniques with Python and SQL, and employs 
    Power BI's interactivity for real-time insights, focusing on reverse engineering 
    the data schema in the consolidated analytics platform.
    """)


# ... [Previous Streamlit setup and Project 2 code] ...

elif page == "Data Analysis / Warehouse & GL Account Optimization":
    st.header("Data Analysis / Warehouse & GL Account Optimization")
    st.subheader("Executive Summary/Business Objective:")
    st.write("""
    This project aims to showcase the potential for cost savings and positive impacts 
    on the bottom line to stakeholders, including the CEO and directors, by optimizing 
    financial oversight across various operational categories.
    """)

    st.subheader("Findings/Strategic Implications:")
    st.write("""
    The analysis revealed significant opportunities for cost optimization. Insights 
    into departmental spending patterns, especially in areas like 'SKYLAB' and '3PL 
    Logistics,' led to strategic recommendations for enhanced financial decision-making 
    and stewardship.
    """)

    st.subheader("Research Question/Data Exploration:")
    st.write("""
    Collaborating with team members, we aimed to gather and probe into the financial 
    data, revealing the nature of spending and identifying areas for potential savings.
    """)

    st.subheader("Background:")
    st.write("""
    As an extension of the Executive Dashboard, the focus was on dissecting complex 
    datasets across logistics, freight, and other areas to identify spending trends and 
    variances, vital for strategic financial planning.
    """)

    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Employed Python for data consolidation and SQL for database management, focusing 
    on breaking down expenses, conducting comparative analyses, and identifying 
    outliers and trends.
    """)

# ... [Previous Streamlit setup and Project 3 code] ...
elif page == "Process Automation / Quarterly Royalty Management":
    st.header("Process Automation / Quarterly Royalty Management")
    st.subheader("Executive Summary/Business Objective:")
    st.write("""
    Automate the quarterly royalty management process to transform a month-long task 
    for two financial analysts into a 2-hour automated system. This aims to reduce 
    labor time by 85%, lowering operational costs and increasing efficiency and accuracy.
    """)

    st.subheader("Strategic Implications:")
    st.write("""
    The implementation of this automation has led to an 85% reduction in processing time, 
    offering a model for similar improvements across financial processes and potentially 
    reshaping the organization's fiscal management approach.
    """)

    st.subheader("Background:")
    st.write("""
    The project addresses the inefficiencies of manually processing 99 contracts every 
    quarter, a task that previously occupied two full-time financial analysts for an 
    entire month and was prone to human error.
    """)

    st.subheader("Methodology/Analytical Proficiency:")
    st.write("""
    Utilized Python for data consolidation and Excel VBA for maintaining the data repository 
    and processing notifications to vendors, including custom scripts for automating data 
    extraction and aggregation.
    """)
# ... [Previous Streamlit setup and Project 4 code] ...


elif page == "Certifications":
    st.header("Certifications")

    # List of certifications
    st.write("""
    - **Big Data Technology Fundamentals**  
      Certified by: AWS (June 2019)
    
    - **AWS Cloud Practitioner Essentials**  
      Certified by: AWS (June 2019)
    
    - **Analyzing and Visualizing Data with Power BI**  
      Certified by: EdX (July 2019)
    """)
# ... [Previous Streamlit setup and other project codes] ...

elif page == "Scope of Skills":
    st.header("Scope of Skills")

    # Programming Languages
    st.subheader("Programming Language:")
    st.write("Python, VBA")

    # Data Engineering Tools
    st.subheader("Data Engineering Tools:")
    st.write("ETL, SSMS, AS400, Snowflakes, Power Query, Integration Analysis")

    # Data Analysis Libraries
    st.subheader("Data Analysis Libraries:")
    st.write("Pandas, NumPy, Seaborn, Matplotlib, Openpyxl, SciPy, TensorFlow")

    # Statistical Analysis
    st.subheader("Statistical Analysis:")
    st.write("""
    Descriptive/Inferential Statistics, A/B Testing, Predictive Modeling, Forecasting, 
    Regression Analysis, Hypothesis Testing, & Time Series Analysis
    """)

    # BI Tools
    st.subheader("BI Tools:")
    st.write("Power BI, Google Analytics/Data Studio, Excel")

    # Digital Marketing
    st.subheader("Digital Marketing:")
    st.write("""
    Facebook, Google Ads, Shopify, Google Analytics, Data Studio, Campaign 
    Management, Performance and Content Optimization
    """)

    # Data Modeling
    st.subheader("Data Modeling:")
    st.write("STAR/ER/DAG diagrams, and Normalization")





# ... [Previous Streamlit setup and other project codes] ...

elif page == "Contact":
    st.header("Contact Information")

    # Inspirational Quote
    st.markdown("""
    <p style="font-style: italic;">
        "In God we trust; for all else, we turn to the validation of data. With data science as our compass, we're set to reveal hidden insights that our data is just dying to tell."
    </p>
    """, unsafe_allow_html=True)

    # Contact Details with Icons
    st.markdown("""
    <div style="font-size: 20px;">
        <i class="fa fa-phone"></i> (626) 203 – 3319<br>
        <i class="fa fa-envelope"></i> <a href="mailto:jason.chang01022021@gmail.com">jason.chang01022021@gmail.com</a><br>
        <i class="fa fa-home"></i> Irvine, CA<br>
        <i class="fa fa-linkedin"></i> <a href="https://linkedin.com/in/jchang0102" target="_blank">linkedin.com/in/jchang0102</a>
    </div>
    """, unsafe_allow_html=True)
