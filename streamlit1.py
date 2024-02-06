# Page Configuration
st.set_page_config(layout="wide", page_title="Jason Chang's Portfolio")

# Custom Styles and Theme Settings
st.markdown("""
<style>
    /* Header styles */
    .big-font { font-family: 'Bebas Neue', sans-serif; font-size: 110px !important; font-weight: 600; color: #383f47; text-align: center; }
    .big2-font { font-family: 'Bebas Neue', sans-serif; font-size: 70px !important; font-weight: 400; color: #383f47; text-align: center; }
    .med2-font { font-family: 'Bebas Neue', sans-serif; font-size: 45px !important; font-weight: 400; color: #D09E55; text-align: center; }
    .medium-font { font-family: 'Bebas Neue', sans-serif; font-size: 55px !important; font-weight: 400; color: #D09E55; }
    .small-font { font-family: 'Lato', sans-serif; font-size: 45px !important; color: #282D33; }

    /* Main content and sidebar background color */
    .reportview-container .main { background-color: #1D262F !important; }
    .sidebar .sidebar-content { background-color: #1D262F !important; color: white; }

    /* Apply Lato font and adjust size for markdown elements */
    .markdown, .streamlit-container .markdown-text-container *, .stMarkdown {
        font-family: 'Lato', sans-serif !important;
        font-size: 20px !important;
    }

    /* Sidebar styles */
    .sidebar .sidebar-content {
        background-color: #1D262F; color: white;
    }
    .fa { padding-right: 15px; }

    /* Horizontal line style */
    hr {
        border-top: 2px solid #FFFFFF;
        width: 100%;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Navigation hover effect */
    .stRadio > div { transition: background-color 0.3s ease; }
    .stRadio > div:hover { background-color: #2A2F36; cursor: pointer; }
    .stRadio label:hover { color: #D09E55 !important; font-weight: 500; }

    /* Adjust padding and margins */
    .reportview-container .main .block-container { padding-top: 1rem; padding-right: 16.66%; }
    .sidebar .sidebar-content { padding: 20px; }
</style>
""", unsafe_allow_html=True)
