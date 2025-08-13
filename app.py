import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np
import time

# ------------------------
# Page Config
# ------------------------
st.set_page_config(page_title="Sleep & Lifestyle Health Dashboard", page_icon="💤", layout="wide")

# ------------------------
# Sidebar - Calculators & Summary
# ------------------------
st.sidebar.title("📊 Health Tools")

# BMI Calculator
st.sidebar.subheader("⚖ BMI Calculator")
weight = st.sidebar.number_input("Weight (kg)", 30, 200, 60)
height = st.sidebar.number_input("Height (cm)", 100, 250, 170)
if height > 0:
    bmi = weight / ((height / 100) ** 2)
    st.sidebar.write(f"**BMI:** {bmi:.1f}")
    if bmi < 18.5:
        st.sidebar.warning("Underweight")
    elif 18.5 <= bmi < 25:
        st.sidebar.success("Normal")
    elif 25 <= bmi < 30:
        st.sidebar.warning("Overweight")
    else:
        st.sidebar.error("Obese")

# Hydration Calculator
st.sidebar.subheader("💧 Daily Hydration")
hydration_need = weight * 0.033
st.sidebar.write(f"Recommended: **{hydration_need:.1f} L/day**")

# BMR Calculator
st.sidebar.subheader("🔥 BMR Calculator")
age = st.sidebar.number_input("Age", 10, 100, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
activity_level = st.sidebar.selectbox(
    "Activity Level", 
    ["Sedentary", "Light", "Moderate", "Active", "Very Active"]
)

if gender == "Male":
    bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
else:
    bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

activity_multiplier = {"Sedentary": 1.2, "Light": 1.375, "Moderate": 1.55, "Active": 1.725, "Very Active": 1.9}
daily_calories = bmr * activity_multiplier[activity_level]
st.sidebar.write(f"Calories Needed: **{daily_calories:.0f} kcal/day**")

# ------------------------
# Sample Dataset with Features
# ------------------------
data = {
    "sleep_hours": [6, 8, 5, 4, 9, 7, 3, 8, 6, 5],
    "exercise_hours": [0, 1, 0, 0, 2, 1, 0, 3, 1, 0],
    "screen_time": [8, 4, 9, 10, 3, 5, 12, 2, 7, 8],
    "stress_level": ["High", "Low", "High", "High", "Low", "Medium", "High", "Low", "Medium", "High"],
    "caffeine_intake": [3, 1, 4, 5, 0, 2, 6, 0, 2, 4],
    "alcohol_consumption": ["Yes", "No", "Yes", "Yes", "No", "No", "Yes", "No", "No", "Yes"],
    "work_hours": [10, 7, 11, 12, 6, 8, 13, 5, 9, 11],
    "water_intake": [1, 3, 2, 1, 4, 3, 1, 5, 2, 1],
    "junk_food_frequency": ["High", "Low", "High", "High", "Low", "Medium", "High", "Low", "Medium", "High"],
    "smoking": ["Yes", "No", "Yes", "Yes", "No", "No", "Yes", "No", "No", "Yes"],
    "disorder": [
        "Insomnia", "Healthy", "Insomnia", "Insomnia",
        "Healthy", "Mild Sleep Apnea", "Severe Sleep Apnea",
        "Healthy", "Mild Sleep Apnea", "Insomnia"
    ]
}
df = pd.DataFrame(data)

# Label Encoding
label_encoders = {}
for col in ["stress_level", "alcohol_consumption", "junk_food_frequency", "smoking", "disorder"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Train Model
X = df.drop("disorder", axis=1)
y = df["disorder"]
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# ------------------------
# User Input
# ------------------------
st.title("🌙 Sleep & Lifestyle Health Prediction")
col1, col2 = st.columns(2)
with col1:
    sleep_hours = st.slider("😴 Sleep Hours", 0, 12, 7)
    exercise_hours = st.slider("🏃 Exercise Hours", 0, 5, 1)
    screen_time = st.slider("💻 Screen Time (hrs/day)", 0, 15, 6)
    stress_level_input = st.selectbox("😟 Stress Level", label_encoders["stress_level"].classes_)
    caffeine_intake = st.slider("☕ Caffeine Intake (cups/day)", 0, 10, 2)
    alcohol_consumption_input = st.selectbox("🍷 Alcohol Consumption", label_encoders["alcohol_consumption"].classes_)

with col2:
    work_hours = st.slider("💼 Work Hours per Day", 0, 16, 8)
    water_intake = st.slider("💧 Water Intake (liters/day)", 0, 10, 2)
    junk_food_frequency_input = st.selectbox("🍔 Junk Food Frequency", label_encoders["junk_food_frequency"].classes_)
    smoking_input = st.selectbox("🚬 Smoking Habit", label_encoders["smoking"].classes_)

# ------------------------
# Prediction + Gamification
# ------------------------
if st.button("🔍 Predict Disorder & Show Score"):
    # Encode inputs
    stress_level_encoded = label_encoders["stress_level"].transform([stress_level_input])[0]
    alcohol_encoded = label_encoders["alcohol_consumption"].transform([alcohol_consumption_input])[0]
    junk_food_encoded = label_encoders["junk_food_frequency"].transform([junk_food_frequency_input])[0]
    smoking_encoded = label_encoders["smoking"].transform([smoking_input])[0]
    
    user_data = [[
        sleep_hours, exercise_hours, screen_time, stress_level_encoded, caffeine_intake,
        alcohol_encoded, work_hours, water_intake, junk_food_encoded, smoking_encoded
    ]]
    
    prediction = model.predict(user_data)
    disorder_name = label_encoders["disorder"].inverse_transform(prediction)[0]
    
    st.success(f"🩺 Predicted Disorder: **{disorder_name}**")

    # Health Score Calculation
    score = 100
    if sleep_hours < 7: score -= 15
    if exercise_hours < 0.5: score -= 10
    if screen_time > 8: score -= 10
    if water_intake < 2: score -= 10
    if caffeine_intake > 4: score -= 5
    if alcohol_consumption_input == "Yes": score -= 5
    if junk_food_frequency_input != "Low": score -= 5
    if smoking_input == "Yes": score -= 15
    if stress_level_input != "Low": score -= 10
    
    st.info(f"💯 **Your Health Score:** {score}/100")

    # Badges
    badges = []
    if sleep_hours >= 8:
        badges.append("🥇 Sleep Champion")
    if water_intake >= 3:
        badges.append("💧 Hydration Hero")
    if exercise_hours >= 0.5:
        badges.append("🚶 Step Starter")
    if badges:
        st.write("🏅 **Your Badges:**", ", ".join(badges))

    import time

# --- Mini Meditation Timer ---
st.subheader("🧘 Mini Meditation Timer")
st.write("Set your meditation duration and follow the breathing guide.")

# User sets the time
minutes = st.number_input("Set Timer (minutes)", min_value=1, max_value=10, value=2, step=1)

if st.button("Start Meditation"):
    meditation_seconds = minutes * 60
    progress_bar = st.progress(0)
    status_text = st.empty()
    breathing_text = st.empty()

    for i in range(meditation_seconds + 1):
        mins_left, secs_left = divmod(meditation_seconds - i, 60)
        status_text.text(f"Time Remaining: {mins_left:02d}:{secs_left:02d}")

        # Breathing cycle every 6 seconds
        cycle = i % 6
        if cycle < 2:
            breathing_text.markdown("🌬️ **Inhale slowly...**")
        elif cycle < 4:
            breathing_text.markdown("😌 **Hold...**")
        else:
            breathing_text.markdown("💨 **Exhale slowly...**")

        progress_bar.progress(i / meditation_seconds)
        time.sleep(1)

    st.success("✅ Meditation complete! Hope you feel relaxed. 🌿")


# ------------------------
# Collapsible Knowledge Sections
# ------------------------
with st.expander("💡 Myths vs Facts about Sleep"):
    st.write("""
    **Myth:** More sleep is always better  
    **Fact:** Quality matters more than quantity.  

    **Myth:** You can "catch up" on lost sleep on weekends  
    **Fact:** Inconsistent sleep schedules can disrupt your body clock.
    """)

with st.expander("🥗 Foods that help with better sleep"):
    st.write("""
    - Bananas 🍌 (rich in magnesium & potassium)  
    - Almonds 🌰 (contain melatonin)  
    - Warm milk 🥛 (tryptophan helps relaxation)  
    - Chamomile tea 🍵 (natural sleep aid)  
    """)

# ------------------------
# Bottom Health Tips
# ------------------------
st.markdown("---")
st.subheader("🌟 General Health & Lifestyle Tips")
st.markdown("""
### 😴 Better Sleep Habits
- Go to bed and wake up at the same time every day
- Limit caffeine & alcohol before bedtime
- Reduce screen time before sleep
- Keep your bedroom dark and cool

### 🏋️ Healthy Lifestyle
- Exercise at least 30 mins/day
- Drink 2–3 liters of water daily
- Eat fresh fruits and vegetables
- Avoid excessive junk food

### 🧘 Stress Management
- Practice meditation or deep breathing
- Take short breaks during work
- Spend time outdoors
""")
