# Mood Logger – Mochi Health

A Streamlit application that lets users:

- Log a mood of a customer submitted ticket with timestamp and optional notes  
- Store mood entries in a Google Sheet using a service account  
- Visualize mood counts for a selected date or date range  
- Toggle visibility of the bar chart  

---

## Features

### Mood Logging
- Choose an emoji-based mood with five options:  
  - 😄 Happy  
  - 😐 Neutral  
  - 🙁 Unsatisfied  
  - 😞 Angry
  - 🤔 Confused
- Select date and time for the entry  
- Add an optional note  
- Submit directly into a Google Sheet  

### Mood Analytics
- View mood distribution for:
  - A **single date**
  - A **date range**
- Interactive Plotly bar chart
- Option to hide/show chart for a cleaner interface 

### Google Sheets Integration
- Uses a Google Cloud service account  
- Stores all entries in a connected Sheet  
- Authentication handled via local JSON key (not committed to repo)  

### Links
- [Google sheets data store](https://docs.google.com/spreadsheets/d/1Jgv2oIqPVlFLp87fUkjMB6SuCKOn9Q7BasiUPGOds0Y/edit?usp=sharing)
- [Deployed Streamlit App](https://share.streamlit.io/mochi-health/mood-logger/main/app.py)

---

## 📦 Run locally

1. Clone the repository:

```bash
git clone <your-repo-url>
cd mood-logger
```

2. Create venv
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt 
```

4. Run the app and access it at `http://localhost:8501`:

```bash
streamlit run app.py
```

