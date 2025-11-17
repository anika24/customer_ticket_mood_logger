# Mood Logger – Mochi Health

A Streamlit application that lets users:

- Log a mood of a customer submitted ticket with timestamp and optional notes  
- Store mood entries in a Google Sheet
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

## How to run locally

1. Clone the repository:

```bash
git clone https://github.com/anika24/customer_ticket_mood_logger.git
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

4. Enable Google Sheets integration:

1. Go to **Google Cloud Console → IAM & Admin → Service Accounts**
2. Create a **new service account**
3. Generate a **JSON key** for the service account
4. Download the JSON file and place it in the project root (this file is gitignored)
5. Share your Google Sheet with the service account email  
   → e.g., `your-service-account@your-project.iam.gserviceaccount.com`
6. Update `app.py` accordingly

5. Run the app and access it at `http://localhost:8501`:

```bash
streamlit run app.py
```

