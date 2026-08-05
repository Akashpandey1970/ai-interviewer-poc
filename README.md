# ai-interviewer-poc

> Streamlit-based voice interviewer and scenario engine powered by Google Gemini.

![GitHub stars](https://img.shields.io/github/stars/Akashpandey1970/ai-interviewer-poc?style=for-the-badge&logo=github) ![GitHub forks](https://img.shields.io/github/forks/Akashpandey1970/ai-interviewer-poc?style=for-the-badge&logo=github) ![GitHub issues](https://img.shields.io/github/issues/Akashpandey1970/ai-interviewer-poc?style=for-the-badge&logo=github) ![Last commit](https://img.shields.io/github/last-commit/Akashpandey1970/ai-interviewer-poc?style=for-the-badge&logo=github) ![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

## 📑 Table of Contents

- [Description](#description)
- [Key Features](#key-features)
- [Use Cases](#use-cases)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [Contributing](#contributing)
- [License](#license)

## 📝 Description

ai-interviewer-poc is a proof-of-concept module designed for AI-driven career development platforms. It provides interactive voice-based interviews and dynamic scenario generation to simulate real-world technical or role-playing exercises for upskilling.

## ✨ Key Features

- **🎤 Live Voice Transcription** — Captures device microphone acoustics into live text transcripts using streamlit-mic-recorder.
- **🤖 Gemini Structured Evaluations** — Executes evaluation pipelines and structured scenario responses through the Google Gemini API using structured response schemas.
- **🎛️ Sidebar Parameter Controls** — Allows selection and manipulation of Ideal Customer Profile (ICP) parameters directly in the Streamlit user interface.
- **🧱 Clean Architecture Separation** — Isolates system blueprints in config.py, API calls in engine.py, and stateful web interfaces in app.py.

## 🎯 Use Cases

- Running AI-assisted voice practice interviews with automated transcription and feedback.
- Prototyping dynamic scenario generation workflows with Google Gemini structured outputs.
- Evaluating candidate transcriptions against defined Ideal Customer Profile parameters.

## ⚡ Quick Start

```bash

# 1. Clone the repository
git clone https://github.com/Akashpandey1970/ai-interviewer-poc.git

# See the Development Setup section below
```

## 📁 Project Structure

```
.
├── LICENSE
├── app.py
├── config.py
└── engine.py
```

## 👥 Contributors

Thanks to everyone who has contributed to this project:

<p align="left">
<a href="https://github.com/Akashpandey1970" title="Akashpandey1970"><img src="https://avatars.githubusercontent.com/u/185476628?v=4&s=64" width="64" height="64" alt="Akashpandey1970" style="border-radius:50%" /></a>
</p>

[See the full list of contributors →](https://github.com/Akashpandey1970/ai-interviewer-poc/graphs/contributors)

## 👥 Contributing

Contributions are welcome! Here's the standard flow:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/Akashpandey1970/ai-interviewer-poc.git`
3. **Branch**: `git checkout -b feature/your-feature`
4. **Commit**: `git commit -m 'feat: add some feature'`
5. **Push**: `git push origin feature/your-feature`
6. **Open** a pull request

Please follow the existing code style and include tests for new behavior where applicable.

## 📜 License

This project is licensed under the **MIT** License.

---

<div align="center">

[![Made with ReadmeBuddy](https://img.shields.io/badge/Made%20with-ReadmeBuddy-8B5CFF?style=for-the-badge&logo=markdown&logoColor=white)](https://readmebuddy.com)

<sub>Generate beautiful READMEs in seconds → <a href="https://readmebuddy.com">readmebuddy.com</a></sub>

</div>
