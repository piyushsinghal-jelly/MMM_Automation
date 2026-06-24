# streamlit file
import streamlit as st
# from src import main


import streamlit as st

# st.title("My First Streamlit App")

# st.write("Welcome! This webpage was made with Python and Streamlit.")

# name = st.text_input("What is your name?")

# if st.button("Say hello"):
#     if name:
#         st.success(f"Hello, {name}! 👋")
#     else:
#         st.warning("Please enter your name first.")

# number = st.slider("Choose a number", min_value=0, max_value=100, value=50)
# st.write(f"You selected: {number}")

# number = st.slider("Choose a number", min_value=0, max_value=200, value=100)
# st.write(f"You selected: {number}")

import streamlit as st

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="MMM Automation POC",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------
# Sidebar navigation
# -------------------------------------------------
st.sidebar.title("MMM Automation")

page = st.sidebar.radio(
    "Navigation",
    [
        "Introduction",
        "Data Collection",
        "Data Validation",
        "Channel Aggregation",
        "Statistical Analysis",
        "Model Training",
    ],
)

# -------------------------------------------------
# Landing page / Introduction
# -------------------------------------------------
if page == "Introduction":

    st.title("MMM Automation POC")
    st.subheader("Marketing Mix Modeling Workflow Automation")

    st.divider()

    st.markdown(
        """
        ### Welcome

        This application is a **Proof of Concept (POC)** for automating and
        standardizing the Marketing Mix Modeling workflow.

        The current version focuses on the **Data Validation** stage, helping
        users review input data before it is used for channel aggregation,
        statistical analysis, and model training.
        """
    )

    st.info(
        "Current POC scope: Data Validation. "
        "The remaining sections are included as planned workflow stages."
    )

    st.markdown("### POC Workflow")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("#### 1. Data Collection")
        st.caption("Upload and organize raw marketing, revenue, and control-variable data.")

    with col2:
        st.markdown("#### 2. Data Validation")
        st.caption("Check data quality, missing values, duplicates, date continuity, and data types.")

    with col3:
        st.markdown("#### 3. Channel Aggregation")
        st.caption("Map granular media sources into standardized MMM channels.")

    with col4:
        st.markdown("#### 4. Statistical Analysis")
        st.caption("Review trends, correlations, distributions, and key data diagnostics.")

    with col5:
        st.markdown("#### 5. Model Training")
        st.caption("Prepare validated data for Meridian model training and evaluation.")

    st.divider()

    st.markdown("### What is available now?")

    left, right = st.columns(2)

    with left:
        st.success(
            """
            **Available in this POC**

            - Data quality checks  
            - Missing-value identification  
            - Duplicate-row checks  
            - Date-range and weekly continuity checks  
            - Data-type validation  
            - Initial dataset review  
            """
        )

    with right:
        st.warning(
            """
            **Planned for future phases**

            - Automated channel mapping  
            - Statistical diagnostics  
            - Meridian model input creation  
            - Model training and comparison  
            - Automated reporting  
            """
        )

    st.divider()

    st.markdown(
        """
        ### Getting started

        Use the sidebar and select **Data Validation** to begin reviewing your
        MMM input dataset.
        """
    )

    if st.button("Go to Data Validation →", type="primary"):
        st.session_state["selected_page"] = "Data Validation"
        st.info("Select **Data Validation** from the sidebar to continue.")


# -------------------------------------------------
# Placeholder pages
# -------------------------------------------------
elif page == "Data Collection":
    st.title("Data Collection")
    st.info("This module is planned for a future phase of the POC.")

elif page == "Data Validation":
    st.title("Data Validation")
    st.write("This is where your data-validation workflow will be added.")

elif page == "Channel Aggregation":
    st.title("Channel Aggregation")
    st.info("This module is planned for a future phase of the POC.")

elif page == "Statistical Analysis":
    st.title("Statistical Analysis")
    st.info("This module is planned for a future phase of the POC.")

elif page == "Model Training":
    st.title("Model Training")
    st.info("This module is planned for a future phase of the POC.")