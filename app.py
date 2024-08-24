import streamlit as st
from PIL import Image
import base64

# Set page title and favicon
st.set_page_config(page_title="Gayasuddin Portfolio", page_icon=":bar_chart:")

# Sidebar for navigation
st.sidebar.header("Navigation")
selected_section = st.sidebar.selectbox(
    "Choose a section",
    ["About Me", "Skills", "Projects", "Education", "Certifications", "Contact"]
)

# Function to display content based on the selected section
def display_section(section):
    if section == "About Me":
        st.title("Gayasuddin - Data Analyst")
        st.subheader("Welcome to my portfolio website! :wave:")
        st.write("## About Me :memo:")

        # CSS to make the photo round and center it
        st.markdown(
            """
            <style>
            .profile-photo {
                display: block;
                margin-left: auto;
                margin-right: auto;
                border-radius: 50%;
                width: 200px;
                height: 200px;
                object-fit: cover;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Load the image from the file system
        image_path = "Gayasuddin_Photo.jpg"
        image = Image.open(image_path)

        # Display the image with CSS applied
        st.markdown(
            f'<img src="data:image/jpg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" class="profile-photo">',
            unsafe_allow_html=True
        )

        st.write("""
        My name is Gayasuddin, and I have completed my B.Tech in Computer Science and Engineering from IIMT University. 

        Additionally, I bring to the table six months of internship experience at CodersCave, where I served as a Data Analyst Intern. During this time, I honed my skills in Python, SQL, Power BI, Excel, Statistics, Machine Learning, Tableau, Data Analytics, Business Analysis, and Data Science. 

        I am eager to leverage these skills, along with my passion for data science, to contribute meaningfully to your organization.
        """)

        # Resume download button
        resume_path = "Gayasuddin.pdf"
        with open(resume_path, "rb") as resume_file:
            resume_data = resume_file.read()

        st.download_button(
            label="Download Resume :file_folder:",
            data=resume_data,
            file_name="Gayasuddin.pdf",
            mime="application/pdf"
        )

    elif section == "Skills":
        st.write("## Skills :rocket:")
        st.write("""
        - **Programming & Libraries**: Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly
        - **Data Visualization & Analysis Tools**: Streamlit, Power BI, Excel, Google Sheets, Jupyter Notebook
        - **Databases & SQL**: SQL, MySQL, PostgreSQL, SQLite
        - **Data Science & Machine Learning**: Data Science, Machine Learning, Statistics, Data Analysis, Product Analysis, Business Analysis
        - **Product & Web Analytics**: Mixpanel, Amplitude
        - **Soft Skills**: Communication, Critical Thinking, Problem Solving
        """)

    elif section == "Projects":
        st.write("## Projects :bar_chart:")
        st.write("### 1. Global Terrorism Patterns: A Data Analysis Perspective (Jan 2024)")
        st.write("""
        - **Description**: An in-depth data analysis of global terrorism trends, identifying key insights, including the deadliest year (2014), hotspots, attack methods, and prominent organizations. This analysis offers a valuable perspective on the evolving landscape of terrorism, aiding security and policy efforts.
        - **Skills Used**: Python and Streamlit
        - [GitHub](https://github.com/GayasuddinMohd/Global-Terrorism-Patterns-A-Data-Analysis-Perspective)
        - [Live](https://global-terrorism-patterns-a-data-analysis-perspective-fhyspzyt.streamlit.app/)
        """)

        st.write("### 2. Airlines Data Analysis (Jun 2023)")
        st.write("""
        - **Description**: Analyzed airline performance and revenue data to address profitability challenges amidst regulatory and economic pressures. Used Python and SQL to extract, clean, and analyze database data, identifying trends in ticket bookings, revenue, and occupancy rates. Provided actionable insights to optimize flight scheduling, pricing, and operations, aiming to boost occupancy rates and profitability.
        - **Skills Used**: Python, SQL, and Streamlit
        - [GitHub](https://github.com/GayasuddinMohd/Airlines-Data-Analysis-)
        - [Live](https://u43xftqvbcfmptwkp9cayh.streamlit.app/)
        """)

        st.write("### 3. Vrinda Store Data Analysis (Dec 2022)")
        st.write("""
        - **Description**: Conducted data analysis on Vrinda Store's sales data for 2022 to understand customer behavior and enhance sales strategies for 2023. Utilized Microsoft Excel to analyze sales trends, order status, customer demographics, and channel performance, deriving actionable insights to improve sales performance. Identified that women customers aged 30-49, residing in Maharashtra, Karnataka, and Uttar Pradesh, are key contributors to sales, and recommended targeting them with tailored ads and offers through channels like Amazon, Flipkart, and Myntra to boost sales in the following year.
        - **Skills Used**: MS Excel
        - [GitHub](https://github.com/GayasuddinMohd/Vrinda-Store-Data-Analysis)
        - [Live](https://onedrive.live.com/edit?id=308364DE6ED0BDEC!s8be81602bed04100ae272ba124647438&resid=308364DE6ED0BDEC!s8be81602bed04100ae272ba124647438&cid=308364de6ed0bdec&ithint=file%2Cxlsx&nav=MTVfe0Q2MkNDNEZGLUYwM0UtNDA5Qy04QzkzLTg3MjdCQTYzRkM2Q30&redeem=aHR0cHM6Ly8xZHJ2Lm1zL3gvYy8zMDgzNjRkZTZlZDBiZGVjL0VRSVc2SXZRdmdCQnJpY3JvU1JrZERnQmUwcXVydjJnMUZ4d1RXYzhhNi1zakE_ZT1oaW5DTGkmbmF2PU1UVmZlMFEyTWtORE5FWkdMVVl3TTBVdE5EQTVReTA0UXprekxUZzNNamRDUVRZelJrTTJRMzA&migratedtospo=true&wdo=2)
        """)

    elif section == "Education":
        st.write("## Education :mortar_board:")
        st.write("""
        - **B.Tech in Computer Science and Engineering** - IIMT University (2020 - 2024)
        - **Intermediate** - LRS Academy (2019 - 2020)
        - **High School** - LRS Academy (2017 - 2018)
        """)

    elif section == "Certifications":
        st.write("## Certifications :trophy:")
        st.write("""
        - **Python Fundamentals for Beginners** - Great Learning (Issued on 2023)
        - **Data Science Foundations** - Great Learning (Issued on 2023)
        - **Basics of Machine Learning** - Great Learning (Issued on 2023)
        """)

    elif section == "Contact":
        st.write("## Contact :phone:")
        st.write("""
        - **LinkedIn**: [linkedin.com/in/gayasuddin](https://www.linkedin.com/in/gayasuddin)
        - **GitHub**: [github.com/GayasuddinMohd](https://github.com/GayasuddinMohd)
        - **Kaggle**: [kaggle.com/gayasuddin](https://www.kaggle.com/gayasuddin)
        - **Email**: mohdfayaz7017052276@gmail.com
        """)

# Display the selected section
display_section(selected_section)
