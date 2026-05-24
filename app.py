# app.py

import os
import streamlit as st
from dotenv import load_dotenv

# सबसे पहले .env फाइल से चाबी (API Key) लोड करें
load_dotenv()

import engine
from streamlit_mic_recorder import speech_to_text

st.set_page_config(page_title="Production AI Interviewer", layout="wide")
st.title("🎤 Live AI Voice Interviewer & Scenario Player")
st.markdown("---")

# --- INITIALIZE LIFECYCLE PERSISTENT STATE STORAGE ---
if "current_scenario" not in st.session_state:
    st.session_state.current_scenario = None
if "live_transcript" not in st.session_state:
    st.session_state.live_transcript = ""
if "eval_metrics" not in st.session_state:
    st.session_state.eval_metrics = None

# --- SIDEBAR PARAMETERS CONTROL ---
st.sidebar.header("Platform Parameters Input")
icp_type = st.sidebar.selectbox("Audience Class Segment (ICP)", ["high_wage", "low_wage"])

if icp_type == "high_wage":
    default_name, default_lang, default_skill, default_milestone = "Riya Sharma", "en", "stakeholder_communication", "M03"
else:
    default_name, default_lang, default_skill, default_milestone = "Arjun Yadav", "hi", "professional_workplace_etiquette", "M01"

user_name = st.sidebar.text_input("Candidate Name", value=default_name)
milestone_code = st.sidebar.text_input("Milestone Reference", value=default_milestone)
skill_target = st.sidebar.text_input("Evaluation Target Skill", value=default_skill)
language_code = st.sidebar.selectbox("Execution Language", ["en", "hi"], index=0 if default_lang == "en" else 1)
difficulty = st.sidebar.select_slider("Deliberate Practice Difficulty", options=["Easy", "Medium", "Hard"], value="Medium")

input_payload = {
    "icp_type": icp_type,
    "name": user_name,
    "milestone_code": milestone_code,
    "skill_target": skill_target,
    "language": language_code,
    "difficulty": difficulty
}

st.sidebar.subheader("Live Engine Payload Blueprint")
st.sidebar.json(input_payload)

# बटन दबाने पर सीन जनरेट होगा और स्टेट लॉक हो जाएगी
if st.sidebar.button("⚙️ Initialize & Launch AI Interview Session"):
    with st.spinner("Invoking Gemini Engine Core..."):
        try:
            st.session_state.current_scenario = engine.call_scenario_engine(input_payload)
            st.session_state.live_transcript = ""
            st.session_state.eval_metrics = None
            st.rerun()  # स्क्रीन को तुरंत रिफ्रेश करके स्टेट लॉक करें
        except Exception as e:
            st.sidebar.error(f"Engine Exception: {e}")

# --- RENDERING THE SCENARIO PLAYER INTERFACE ---
if st.session_state.current_scenario:
    sc = st.session_state.current_scenario
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(f"🎬 Active Session: {sc['episode_title']}")
        st.info(f"**📍 Location:** {sc['scene']['setting']} | **⏰ Timeline:** {sc['scene']['time']}\n\n**Context:** {sc['scene']['context']}")
        
        st.markdown("### 👥 Present Characters")
        for char in sc['characters']:
            st.markdown(f"- **{char['name']}** ({char['role']}) — *Mood: {char['mood']}*")
            
        st.markdown("---")
        st.error(f"🚨 **{sc['characters'][0]['name']}:** \"{sc['antagonist_opening_line']}\"")
        
        st.markdown("#### 💡 Strategic Options Philosophy")
        for chip in sc['strategy_chips']:
            with st.expander(f"Option {chip['id']}: {chip['label']}"):
                st.write(f"*Philosophy Track:* {chip['philosophy']}")
                
    with col2:
        st.subheader("🎤 Live Audio Capture Sandbox")
        st.write(f"Record your verbal response below. Language format: **{language_code.upper()}**.")
        
        # ब्राउज़र से सीधे आवाज रिकॉर्ड करने का विजेट
        captured_audio_text = speech_to_text(
            start_prompt="🔴 Open Microphone",
            stop_prompt="⏹️ Close & Transcribe",
            language=language_code,
            key='voice_interview_stt_processor'
        )
        
        if captured_audio_text:
            st.session_state.live_transcript = captured_audio_text
            
        if st.session_state.live_transcript:
            st.markdown("### 📝 Audio Transcription:")
            st.warning(st.session_state.live_transcript)
            
            # इवैल्यूएशन को लॉक्ड स्टेट वाले सीन से ही सिंक करें
            if st.button("📊 Submit Answer for Analytics Processing"):
                with st.spinner("Processing analytics metrics pipeline..."):
                    st.session_state.eval_metrics = engine.evaluate_interview_response(
                        st.session_state.current_scenario, 
                        st.session_state.live_transcript
                    )
                    
        if st.session_state.eval_metrics:
            st.markdown("---")
            st.subheader("📈 Performance Metrics Dashboard")
            metrics = st.session_state.eval_metrics
            
            # FIX: डॉट्स (...) हटाने के लिए प्रोग्रेस बार लेआउट
            scores = metrics["scores"]
            
            # प्रत्येक पैमाने के लिए साफ-साफ वैल्यू और बार दिखाएं
            for axis, score_val in scores.items():
                axis_title = axis.capitalize()
                st.markdown(f"**{axis_title}** : `{score_val} / 100`")
                st.progress(int(score_val) / 100)
            
            st.markdown("---")
            st.write(f"**Detailed Justification:** {metrics.get('justification')}")
            st.error(f"⚠️ **Critical Improvement Target:** {metrics.get('critical_improvement')}")

    st.markdown("---")
    with st.expander("🛠️ Inspect Active Node Production Schema Blueprint (JSON)"):
        st.json(sc)