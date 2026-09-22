import base64
import pandas as pd
import streamlit as st
import plotly.express as px
DATA_PATH = "Automobile_clean.csv"
CAR_IMAGE_PATH = "assetscar.jpeg"
NUMERIC_COLS = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration"]
PURPLE = "#6A1B9A"
PURPLE_LIGHT = "#8E24AA"
PURPLE_DARK = "#7B1FA2"
def render_global_style() -> None:
    st.markdown("""
        <style>
        html, body, [class*="css"] {
            color: #1a1a1a;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #111111 !important;
            font-weight: 700 !important;
        }
        p, span, label, div {
            color: #1a1a1a;
        }
        [data-testid="stMetricLabel"] {
            color: #111111 !important;
            font-weight: 600 !important;
        }
        [data-testid="stMetricValue"] {
            color: #000000 !important;
            font-weight: 700 !important;
        }
        </style>
    """, unsafe_allow_html=True)
def render_corner_image(path: str) -> None:
    with open(path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
        .corner-wrap {{
            position: fixed;
            top: 15px;
            right: 20px;
            z-index: 999;
            text-align: center;
            background: linear-gradient(160deg, #f3e5f5, #ffffff);
            padding: 8px;
            border-radius: 18px;
            border: 1px solid #d1a3e0;
            box-shadow: 0 6px 18px rgba(106, 27, 154, 0.25);
        }}
        .corner-car {{
            width: 170px;
            height: auto;
            display: block;
            border-radius: 12px;
        }}
        .corner-credit {{
            margin-top: 6px;
            font-size: 11px;
            color: #6A1B9A;
            font-weight: 700;
            letter-spacing: 0.3px;
        }}
        </style>
        <div class="corner-wrap">
            <img src="data:image/jpeg;base64,{img_b64}" class="corner-car">
            <div class="corner-credit">Made by Sadeen Abdelalrahman</div>
        </div>
    """, unsafe_allow_html=True)
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
def render_sidebar(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filters")
    origin = st.sidebar.multiselect(
        "Origin",
        options=sorted(df["origin"].unique()),
        default=sorted(df["origin"].unique()),
    )
    manufacturer = st.sidebar.multiselect(
        "Manufacturer",
        options=sorted(df["manufacturer"].unique()),
        default=[],
    )
    cyl_min, cyl_max = int(df["cylinders"].min()), int(df["cylinders"].max())
    cylinders = st.sidebar.slider("Cylinders", cyl_min, cyl_max, (cyl_min, cyl_max))
    year_min, year_max = int(df["model_year_full"].min()), int(df["model_year_full"].max())
    year = st.sidebar.slider("Model Year", year_min, year_max, (year_min, year_max))
    result = df[
        df["origin"].isin(origin)
        & df["cylinders"].between(*cylinders)
        & df["model_year_full"].between(*year)
    ]
    if manufacturer:
        result = result[result["manufacturer"].isin(manufacturer)]
    return result
def render_kpis(df: pd.DataFrame) -> None:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Car Count", f"{len(df)}")
    col2.metric("Avg MPG", f"{df['mpg'].mean():.1f}")
    col3.metric("Avg Horsepower", f"{df['horsepower'].mean():.0f} HP")
    col4.metric("Avg Weight", f"{df['weight'].mean():.0f} lbs")
def render_distribution_tab(df: pd.DataFrame) -> None:
    c1, c2 = st.columns(2)
    with c1:
        fig = px.histogram(df, x="mpg", nbins=20, title="MPG Distribution",
                            color_discrete_sequence=[PURPLE])
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig = px.histogram(df, x="cylinders", title="Car Count by Cylinders",
                            color_discrete_sequence=[PURPLE_LIGHT])
        st.plotly_chart(fig, use_container_width=True)
def render_relationships_tab(df: pd.DataFrame) -> None:
    c1, c2 = st.columns(2)
    with c1:
        fig = px.scatter(df, x="weight", y="mpg", color="origin",
                          title="Weight vs MPG by Origin",
                          color_discrete_sequence=px.colors.sequential.Purples_r,
                          hover_data=["manufacturer", "model"])
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        corr = df[NUMERIC_COLS].corr()
        fig = px.imshow(corr, text_auto=".2f", title="Correlation Matrix",
                         color_continuous_scale="Purples")
        st.plotly_chart(fig, use_container_width=True)
    trend = df.groupby("model_year_full")["mpg"].mean().reset_index()
    fig = px.line(trend, x="model_year_full", y="mpg", markers=True,
                  title="MPG Trend Over the Years",
                  color_discrete_sequence=[PURPLE])
    st.plotly_chart(fig, use_container_width=True)
def render_origin_tab(df: pd.DataFrame) -> None:
    c1, c2 = st.columns(2)
    with c1:
        fig = px.box(df, x="origin", y="mpg", color="origin",
                     title="MPG Distribution by Origin",
                     color_discrete_sequence=px.colors.sequential.Purples_r)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        top_makers = df["manufacturer"].value_counts().head(10)
        fig = px.bar(top_makers, orientation="h",
                     title="Top 10 Manufacturers (Car Count)",
                     color_discrete_sequence=[PURPLE_DARK])
        st.plotly_chart(fig, use_container_width=True)
def render_table_tab(df: pd.DataFrame) -> None:
    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Filtered Data (CSV)", data=csv,
                        file_name="filtered_cars.csv", mime="text/csv")
def main() -> None:
    st.set_page_config(page_title="CarInsight Dashboard", layout="wide")
    render_global_style()
    render_corner_image(CAR_IMAGE_PATH)

    df = load_data(DATA_PATH)
    st.title("CarInsight Dashboard")
    st.caption("Interactive analysis of car data (Auto MPG Dataset)")
    filtered = render_sidebar(df)
    if filtered.empty:
        st.warning("No results match the selected filters.")
        st.stop()
    render_kpis(filtered)
    st.divider()
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Distribution", "Relationships", "By Origin", "Data Table"]
    )
    with tab1:
        render_distribution_tab(filtered)
    with tab2:
        render_relationships_tab(filtered)
    with tab3:
        render_origin_tab(filtered)
    with tab4:
        render_table_tab(filtered)
if __name__ == "__main__":
    main()