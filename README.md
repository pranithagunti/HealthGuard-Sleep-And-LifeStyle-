# HealthGuard - Sleep and Lifestyle Analyzer.

## Project overview

HealthGuard is a Streamlit-based Python application that analyzes a user's sleep and lifestyle data and generates personalized, practical recommendations. The app helps users understand and improve their sleep hygiene, monitor stress, track body metrics, and get targeted tips for food, activity, meditation and daily habits.

blob:https://web.whatsapp.com/dfcbcfa5-1798-4988-be1f-3b355ba75072<img width="2560" height="1470" alt="image" src="https://github.com/user-attachments/assets/3f1fd83c-c821-45f9-b50d-7e96c09efa01" />

## Key technologies

* Python
* Streamlit (web UI)
* pandas (data handling)
* scikit-learn (optional analysis / pattern detection)
* matplotlib (plots/visualizations)
* numpy (numerical operations)

## LIVE DEMO:

Demo Link: https://rxrtbmegane7wnkysfhata.streamlit.app

## Main features

* Compute body metrics:

  * BMI (Body Mass Index)
  * BMR (Basal Metabolic Rate) — assumed from "cmr"; update if you meant something else
* Sleep analysis:

  * Analyze sleep patterns (bedtime, wake time, sleep duration, sleep quality)
  * Detect irregular sleep schedule and provide sleep hygiene tips
* Lifestyle analysis:

  * Track daily habits (screen time, caffeine intake, exercise frequency, meal timing)
  * Analyze lifestyle patterns and suggest small habit changes
* Stress tracking:

  * Track subjective stress levels and provide stress-reduction suggestions
* Meditation facility:

  * Provide guided/structured meditation suggestions or short practice steps
* Food & nutrition tips:

  * Suggest general healthy eating tips and scheduling guidance for better sleep
* Recommendations:

  * Actionable, personalized tips to improve sleep and maintain a healthy lifestyle
* Visualization:

  * Plots for sleep trends, activity levels, stress scores, and basic metrics

## Installation

1. Clone the repository:
   git clone [https://github.com/pranithagunti/HealthGuard-Sleep-And-LifeStyle-.git](https://github.com/pranithagunti/HealthGuard-Sleep-And-LifeStyle-.git)
   cd HealthGuard-Sleep-And-LifeStyle-

2. (Recommended) Create and activate a virtual environment:
   python -m venv venv
   On macOS/Linux: source venv/bin/activate
   On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

## Running the app

Start the Streamlit app with:
streamlit run app.py

The app will open in your default browser (usually at [http://localhost:8501](http://localhost:8501)). Follow the on-screen form/inputs to enter your sleep and lifestyle data.

## Typical input fields

* Age, gender, height (cm), weight (kg)
* Typical bedtime and wake-up time
* Daily naps (yes/no and duration)
* Average screen time before bed (minutes)
* Daily caffeine intake (cups, approximate time)
* Exercise frequency and intensity
* Self-reported stress level (e.g., 1–10)
* Meal timing and types (light/heavy before bed)
* Interest in meditation (yes/no, preferred duration)

## Example output (what the app provides)

* Calculated BMI and BMR with interpretation and healthy ranges
* Sleep summary: average sleep duration, sleep consistency score, sleep debt estimate
* Graphs: weekly sleep duration, stress vs sleep graph, activity vs sleep correlation
* Personalized tips: bedtime routine recommendations, caffeine cut-off time, light exposure guidance, short meditation exercises, meal timing suggestions
* Suggested follow-up actions: small changes to try this week, what to track next

## Notes about data & privacy

* The app is intended for educational and personal use only and does not replace professional medical advice.
* No external servers are required — all processing is local by default (unless you change it).
* If you add any data storage or analytics, ensure privacy safeguards and inform users clearly.

## Extending the project

* Add persistent user profiles (local encrypted storage or secure cloud backend)
* Improve sleep-detection with wearable data inputs (optional)
* Add model-based pattern detection with scikit-learn (clustering, anomaly detection)
* Add richer meditation content (audio or step-by-step guided sessions)
* Add alerts or reminders (email / mobile push) for habit nudges

## Development & contribution

* Fork the repo, create a feature branch, and open a pull request.
* Write clear commit messages and include small, focused changes per PR.
* Add unit tests for any new data-processing functions.
* Document any new dependencies in requirements.txt.

## License

MIT LICENSE provided.

## Contact

Open an issue in the repository or contact the maintainer via GitHub at:
[https://github.com/pranithagunti](https://github.com/pranithagunti)

## Acknowledgement / disclaimer

HealthGuard provides general guidance. For medical concerns, consult a qualified healthcare provider. The app is intended to support healthy habits, not to diagnose or treat medical conditions.

---
