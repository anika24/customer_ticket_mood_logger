import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import plotly.graph_objects as go

# --------------------
# GOOGLE SHEETS SETUP
# --------------------

# name of the json file with service account credentials
SERVICE_ACCOUNT_FILE = "mood-logger-mochi-health-ff1b39e615eb.json"

# needed for sheets + drive access
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# authentication using localhost (for local development)
# creds = ServiceAccountCredentials.from_json_keyfile_name(
#     SERVICE_ACCOUNT_FILE,
#     scope
# )
# client = gspread.authorize(creds)

# authentication using streamlit (for deployment)
creds = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["gcp_service_account"],
    scope,
)
client = gspread.authorize(creds)

# open the sheet
SHEET_NAME = "raw_customer_ticket_mood_logs"
sheet = client.open(SHEET_NAME).sheet1

# --------------------
# STREAMLIT UI
# --------------------

# --- Data Input ---
st.title("Mood of the Queue")

st.subheader("Log Mood")

# Mood options: Happy, Angry, Disappointed, Confused, Neutral
mood = st.selectbox("Select mood", ["😊", "😠", "😕", "🤔", "😐"])

st.write("Select the timestamp for the ticket:")
selected_date = st.date_input("Date")
selected_time = st.time_input("Time")

note = st.text_input("Optional note")

selected_timestamp = datetime.combine(selected_date, selected_time).strftime("%Y-%m-%d %H:%M:%S")

if st.button("Submit"):
    sheet.append_row([selected_timestamp, mood, note])
    st.success(f"Mood logged with timestamp {selected_timestamp}")


# --- Visualization ---
st.subheader("Mood Count")

data = sheet.get_all_records()
df = pd.DataFrame(data)

if df.empty:
    st.info("No mood logs yet — submit one above!")
else:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date

    # Option to select single date or date range
    mode = st.radio("View by:", ["Single Date", "Date Range"], horizontal=True)

    if mode == "Single Date":
        selected_date = st.date_input(
            "Select date:",
            value=datetime.today().date(),
            key="single_date",
        )
        filtered = df[df["date"] == selected_date]

    else:  # Date Range
        start_default = df["date"].min()
        end_default = df["date"].max()

        range_selected = st.date_input(
            "Select date range:",
            value=(start_default, end_default),
            key="range_picker",
        )

        if isinstance(range_selected, tuple):
            if len(range_selected) == 2:
                start_date, end_date = range_selected
            elif len(range_selected) == 1:
                # If only one date picked fallback to single date logic
                start_date = range_selected[0]
                end_date = range_selected[0]
            else:
                start_date = start_default
                end_date = end_default
        else:
            start_date = range_selected
            end_date = range_selected

        filtered = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    if filtered.empty:
        st.info("No entries for this selection.")
    else:
        mood_counts = (
            filtered.groupby("mood")
            .size()
            .reset_index(name="count")
        )

        # Option to hide/show bar chart
        show_chart = st.checkbox("Show bar chart", value=True)

        if show_chart:
            # Build numeric x positions, keep emojis as labels
            x_positions = list(range(len(mood_counts)))
            counts = mood_counts["count"].astype(int).tolist()
            labels = mood_counts["mood"].astype(str).tolist()

            if mode == "Single Date":
                chart_title = f"Mood Trend for {selected_date}"
            else:
                chart_title = f"Mood Trend from {start_date} to {end_date}"

            fig = go.Figure()
            fig.add_bar(
                x=x_positions,
                y=counts,
                text=counts,
                textposition="outside",
            )

            fig.update_xaxes(
                tickmode="array",
                tickvals=x_positions,
                ticktext=labels,
                title_text="Mood",
            )
            fig.update_yaxes(
                range=[0, max(counts) * 1.25],
                title_text="Count",
                rangemode="tozero",
            )


            fig.update_layout(
                title=chart_title,
                height=300,
                margin=dict(t=80, b=40, l=40, r=40),
                font=dict(size=13),
                showlegend=False,
            )

            st.plotly_chart(fig, use_container_width=True)
