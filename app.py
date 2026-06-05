import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="Netflix Interactive Dashboard",
    layout="wide"
)

# Title
st.title("🎬 Netflix Interactive Dashboard")

# File Upload
uploaded_file = st.file_uploader(
    "Upload Netflix Dataset (CSV)",
    type=["csv"]
)

if uploaded_file is not None:

    # Read Dataset
    df = pd.read_csv(uploaded_file)

    # Dataset Info
    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Dataset Columns")
    st.write(df.columns.tolist())

    # Interactive Filter
    content_type = st.selectbox(
        "Select Content Type",
        ["All"] + sorted(df["type"].dropna().unique().tolist())
    )

    if content_type != "All":
        df = df[df["type"] == content_type]

    # Preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Movies vs TV Shows
    st.subheader("Movies vs TV Shows")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.countplot(
        x="type",
        data=df,
        ax=ax
    )

    st.pyplot(fig)

    # Content Ratings
    st.subheader("Content Ratings")

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.countplot(
        y="rating",
        data=df,
        order=df["rating"].value_counts().index[:10],
        ax=ax
    )

    st.pyplot(fig)

    # Release Year Trend
    st.subheader("Release Year Trend")

    yearly = (
        df["release_year"]
        .value_counts()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    yearly.plot(ax=ax)

    ax.set_xlabel("Release Year")
    ax.set_ylabel("Number of Titles")

    st.pyplot(fig)

    # Top Countries
    st.subheader("Top 10 Countries")

    countries = (
        df["country"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(
        x=countries.values,
        y=countries.index,
        ax=ax
    )

    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to view the dashboard.")