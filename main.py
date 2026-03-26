import streamlit as st
# Importing our custom 'Brain' and 'AI' modules
from logic import get_readiness_score, get_category
from ai_agent import get_ai_advice

# --- Page Config ---
st.set_page_config(page_title="AI-Pedagogy Sync (APS)", layout="centered")

st.title("🎓 AI-Pedagogy Sync (APS) Framework")
st.write("Assess your AI readiness and get a personalized roadmap.")

# --- Step 1: User Input ---
# These are simple widgets that collect data
subject = st.selectbox("What is your main subject?", 
                      ["Social Science", "Science", "Commerce", "Mathematics", "Other"])

locality = st.radio("Where is your school located?", ["Urban", "Rural"])

# A slider for proficiency (1-5 scale like your survey)
prof_level = st.slider("Rate your current AI proficiency (1=Beginner, 5=Expert)", 1, 5, 3)

# --- Step 2: The Action Button ---
if st.button("Generate My Sync Plan"):
    
    # 1. Calculate the score using our 'Logic' module
    score = get_readiness_score(prof_level, locality)
    category = get_category(score)
    
    # 2. Display the Results
    st.divider()
    st.subheader(f"Your Result: {category}")
    st.progress(score / 100) # A visual loading bar
    st.write(f"**Readiness Score:** {score}/100")
    
    # 3. Get AI Advice from our 'Agent' module
    with st.spinner("Consulting our AI Expert..."):
        advice = get_ai_advice(subject, score, category)
        st.info(advice)

    st.success("Roadmap generated! Good luck on your AI journey.")