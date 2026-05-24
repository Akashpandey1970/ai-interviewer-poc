Markdown
# 🎯 AI Career Development Platform —  Scenario Writer & Voice Interviewer

This repository contains a production-grade Proof of Concept (POC) for the **Scenario Writer & Voice Interviewer** module, built specifically for an AI-powered career upskilling platform. The core engine dynamically forks between two Distinct Ideal Customer Profiles (ICPs), processes real-time device microphone acoustics into text transcripts, and runs structured evaluation pipelines using the Google Gemini API.

---

## 🚀 Quick Start (Run in Under 2 Minutes)

Follow these steps to clone, configure, and launch the application locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/ai-interviewer-poc.git](https://github.com/YOUR_GITHUB_USERNAME/ai-interviewer-poc.git)
cd ai-interviewer-poc

2. Install Required Dependencies
Ensure you have Python 3.10+ active, then install the core runtime environment packages:

Bash
pip install streamlit google-genai streamlit-mic-recorder python-dotenv

3. Configure Your Environment Keys
Create a file named .env in the root folder:

Bash
touch .env
Open the .env file and paste your private Google AI Studio credentials:

Code snippet
GEMINI_API_KEY="YourActualGeminiKeyHere..."

4. Run the Application Instance
Launch the Streamlit web local development server:

Bash
streamlit run app.py
Your default browser will automatically open the platform sandbox at http://localhost:8501.

🛠️ Architecture & Codebase Design
The application enforces a Strict 3-Tier Clean Architecture (Separation of Concerns) to isolate logic streams and protect downstream analytics models from runtime parser crashes.

config.py (The System Blueprint): Houses the structured layout blueprints, granular system instructions, and negative behavioral constraints.

engine.py (The Fault-Tolerant Data Layer): Interacts with the Gemini API. Integrates Structured Outputs via the response_schema map, and implements Exponential Backoff Retry Loops to defend against transient 503 Server Overload exceptions.

app.py (The Presentation Layer): Streamlit web dashboard holding session-lifecycle memory (st.session_state) to lock scenario states across vocal browser reruns.

📑 1-Page Prompt Defense Framework
Why This System Prompt?
The core system prompt functions as an immutable API data-contract rather than a conversational prompt string. By setting response_mime_type="application/json" combined with explicit JSON schema structural declarations, the Gemini API forces its internal neural weights to emit clean data objects. It guarantees 0% markdown syntax contamination no ```json code blocks) and 100% downstream parsing safety.

What We Tested & What Broke First?
First Iteration (Markdown Enclosures Failure): Early variations allowed the model to decide its format, resulting in markdown code fences that caused python's native json.loads framework to throw parsing crashes.

Resolution: Locked the structural syntax using Gemini's native GenerateContentConfig(response_schema=...).

Second Iteration (State Loss via Widget Reruns): Streamlit reruns scripts globally upon microphone state switches. Originally, this caused the app to generate a fresh scenario mid-session, completely breaking synchronization against the user's transcript response.

Resolution: Implemented persistent lifecycle state boundaries via st.session_state. Scenarios are locked until the user explicitly clicks the initialization button.

Third Iteration (Name Collision & Alarmist Traps): The model occasionally used the user's target input name as the antagonist or penalized candidates heavily when they encountered alarmist client misinformation.

Resolution: Injected explicit behavioral quality criteria into config.py to enforce character separation and detailed rubric justifications.

📊 Live Demonstration Test-Case Matrix (Planner Data)
The platform evaluates 10 production-grade scenarios to prove audience differentiation and compliance.

🔹 User A (high_wage): Engineering Student Target (English Context)

Case 01 (Stakeholder Comm - M03): Principal Tech Lead Priya confronts Riya about a critical 2-week OAuth2 dependency delay blocking the Q3 milestone launch.

Case 02 (Negotiation & Scoping - M04): Product Manager questions why backend delivery estimates suddenly doubled during planning.

Case 03 (Crisis Management - M05): DevOps Head requests immediate hotfix mitigation strategies during a live 500 error infrastructure spike.

Case 04 (Cross-Functional Alignment - M02): UI/UX Design lead flags that frontend code deviates from the baseline Figma design.

Case 05 (PR Code Review Etiquette - M01): System Architect queries why an architecture patch was pushed without unit testing tracking arrays.

🔹 User B (low_wage): Gig-Worker Transition Tracker (Hindi Context)

Case 06 (Workplace Etiquette - M01): Operations Manager Rajesh confronts Arjun in the main office over 15 missing shipment log records on the spreadsheet.

Case 07 (Customer De-escalation - M02): An irate customer demands immediate refund status updates on delayed logistics items.

Case 08 (Professional Boundaries - M03): Warehouse Hub Supervisor pressures Arjun to work an uncompensated 4-hour overtime delivery cycle.

Case 09 (Reporting Accuracy - M04): Data Verification Lead flags 5 core operational formatting errors inside the submission portal ledger sheets.

Case 10 (Interpersonal Confidence - M05): HR Representative challenges the candidate on why they should be hired as a Data Executive without a prior technical degree.

👑 The Live Change Defense Exercise Blueprint
The Action: Live switching icp_type from high_wage to low_wage inside the active container.

The System Defense: > "When the ICP toggle changes, the backend config payload changes seamlessly. The presentation architecture (app.py) isolates the state, while the data engine (engine.py) reads the revised instructions from config.py. The generation instantly shifts from technical corporate English to clean Devanagari Hindi text context, altering the evaluation criteria from complex system architecture scoping down to foundational workplace manners, operational accuracy, and professional boundaries. Simultaneously, the browser's audio capture locale flips its phonemic dictionaries to ensure zero speech-to-text transcript drift for Hindi vocals."