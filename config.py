# config.py

SYSTEM_PROMPT = """
You are the core AI Scenario Writer module for a production career upskilling platform. 
Your single job is to output a structured scenario object following the platform configuration.

### TARGET AUDIENCE FORKING (ICP) STRICT RULES:
1. If icp_type is "high_wage":
   - Context must be white-collar corporate, tech stack, or engineering team stand-ups.
   - Language must be professional English ("en").
2. If icp_type is "low_wage":
   - Context must be office-administration, data entry, client customer service, or transitioning from gig work (delivery/hospitality).
   - Language must be Hindi ("hi"), written entirely in the Devanagari script.

### CONTENT QUALITY CRITERIA:
- `characters`: The first character in the array MUST be the antagonist who speaks the opening line.
- `antagonist_name`: NEVER use the user's input name (e.g., input_data['name']) as a character or antagonist name. The antagonist must be a different persona (e.g., Rajesh, Priya, David, Sarah) who confronts the user.
"""

EVAL_SYSTEM_PROMPT = """
You are an expert technical and behavioral workplace evaluator. 
Analyze the user's verbal response against the setup scenario, the baseline antagonist line, and the provided scoring rubric guidelines.

### ENHANCEMENT - PRODUCTION CRITERIA:
You must output a valid JSON object containing raw numeric scores (0-100) for each rubric axis, along with text feedback. 
Do not include markdown code fences (```json). Output ONLY the raw JSON string matching this schema:
{
  "scores": {
    "communication": 85,
    "composure": 70,
    "clarity": 90,
    "strategy": 75,
    "outcome": 80
  },
  "justification": "Detailed explanation of scores in the requested language context ('en' or 'hi' script).",
  "critical_improvement": "The #1 thing the candidate needs to change to pass this milestone."
}
"""

JSON_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "episode_title": {"type": "STRING"},
        "scene": {
            "type": "OBJECT",
            "properties": {
                "setting": {"type": "STRING"},
                "time": {"type": "STRING"},
                "context": {"type": "STRING"}
            },
            "required": ["setting", "time", "context"]
        },
        "characters": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "name": {"type": "STRING"},
                    "role": {"type": "STRING"},
                    "mood": {"type": "STRING"}
                },
                "required": ["name", "role", "mood"]
            }
        },
        "antagonist_opening_line": {"type": "STRING"},
        "strategy_chips": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "id": {"type": "STRING"},
                    "label": {"type": "STRING"},
                    "philosophy": {"type": "STRING"}
                },
                "required": ["id", "label", "philosophy"]
            }
        },
        "success_criteria": {"type": "ARRAY", "items": {"type": "STRING"}},
        "rubric": {
            "type": "OBJECT",
            "properties": {
                "communication": {"type": "STRING"},
                "composure": {"type": "STRING"},
                "clarity": {"type": "STRING"},
                "strategy": {"type": "STRING"},
                "outcome": {"type": "STRING"}
            },
            "required": ["communication", "composure", "clarity", "strategy", "outcome"]
        },
        "transfer_targets": {"type": "ARRAY", "items": {"type": "STRING"}}
    },
    "required": ["episode_title", "scene", "characters", "antagonist_opening_line", "strategy_chips", "success_criteria", "rubric", "transfer_targets"]
}