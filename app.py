import streamlit as st
import pandas as pd

from core.clone_repo import clone_repository
from core.parser import extract_python_functions
from core.reviewer import review_code
from core.confidence import confidence_label


st.set_page_config(
    page_title="AI Code Review Agent",
    layout="wide"
)

st.title("🤖 AI Code Review Agent")

st.markdown(
    """
AI-powered GitHub repository analyzer using:

- AST Parsing
- Automated Code Review
- Confidence Scoring
- Severity Classification
"""
)

# Input
repo_url = st.text_input(
    "Enter GitHub Repository URL",
    "https://github.com/pallets/flask"
)

if st.button("Run Code Review"):

    # Clone Repo
    with st.spinner("Cloning repository..."):
        repo_path = clone_repository(repo_url)

    # Parse Repo
    with st.spinner("Parsing repository..."):
        parsed_data = extract_python_functions(repo_path)

    st.success(f"Parsed {len(parsed_data)} functions/classes.")

    reviews = []

    # Review first 20 items only
    progress_bar = st.progress(0)

    for idx, item in enumerate(parsed_data[:20]):

        result = review_code(item["code"])

        for issue in result["issues"]:

            reviews.append({

                "File": item["file"],
                "Function/Class": item["name"],
                "Issue Type": issue["type"],
                "Severity": issue["severity"],
                "Confidence": issue["confidence"],
                "Confidence Label": confidence_label(issue["confidence"]),
                "Comment": issue["comment"]
            })

        progress_bar.progress((idx + 1) / 20)

    if reviews:

        df = pd.DataFrame(reviews)

        # Metrics
        col1, col2, col3 = st.columns(3)

        col1.metric("Total Issues", len(df))

        col2.metric(
            "High Severity",
            len(df[df["Severity"] == "high"])
        )

        col3.metric(
            "Medium Severity",
            len(df[df["Severity"] == "medium"])
        )

        st.divider()

        # Filter
        severity_filter = st.selectbox(
            "Filter by Severity",
            ["All", "low", "medium", "high"]
        )

        filtered_df = df

        if severity_filter != "All":

            filtered_df = df[df["Severity"] == severity_filter]

        # Table
        st.subheader("Review Results")

        st.dataframe(
            filtered_df,
            use_container_width=True
        )

        # Severity Chart
        st.subheader("Severity Distribution")

        severity_counts = df["Severity"].value_counts()

        st.bar_chart(severity_counts)

        # Confidence Chart
        st.subheader("Confidence Distribution")

        confidence_counts = df["Confidence Label"].value_counts()

        st.bar_chart(confidence_counts)

        # Download CSV
        csv = filtered_df.to_csv(index=False)

        st.download_button(
            label="📥 Download CSV Report",
            data=csv,
            file_name="code_review_report.csv",
            mime="text/csv"
        )

    else:

        st.warning("No issues detected.")