# 🌐 AI Language Translation Tool

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![CodeAlpha](https://img.shields.io/badge/CodeAlpha-AI%20Internship-7c3aed?style=for-the-badge)

A professional, open-source **AI-powered Language Translation Tool** built with Streamlit and the `translate` library. Translate English text into **15 languages** — no API key or billing required.

---

## 📸 Preview

> _Add a screenshot of the running application here._

---

## 🎥 Demo Video

> **LinkedIn Demonstration Video:**
> 📎 _Paste your LinkedIn video URL here once uploaded._

---

## ✨ Features

| Feature | Details |
|---|---|
| **15 Target Languages** | Spanish, French, German, Hindi, Japanese, Portuguese, Italian, Russian, Chinese, Arabic, Korean, Dutch, Turkish, Polish, Swedish |
| **Character Limit Indicator** | Real-time counter with colour-coded warnings at 500 chars |
| **Session State** | Input text persists across button clicks |
| **Copy to Clipboard** | One-click JS-powered copy button |
| **Error Handling** | Friendly messages for network/service failures |
| **Premium Dark UI** | Glassmorphism design with gradient accents |
| **No API Key Needed** | Uses the free `translate` open-source library |

---

## 🗂️ Project Structure

```
CodeAlpha_LanguageTranslationTool/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation (this file)
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python **3.11** or higher
- pip (comes with Python)

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/<your-username>/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

**2. (Optional) Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the application**
```bash
streamlit run app.py
```

**5. Open in your browser**

Streamlit will automatically open the app at `http://localhost:8501`.

---

## 🖥️ Usage

1. **Enter text** in the source text area (English, up to 500 characters).
2. **Select a target language** from the drop-down menu.
3. Click **✨ Translate**.
4. View the translated result in the green output box.
5. Click **📋 Copy Text** to copy the translation to your clipboard.

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.11+** | Core programming language |
| **Streamlit** | Web UI framework |
| **translate** | Open-source translation library |

---

## 🌍 Supported Languages

| Language | ISO Code | Language | ISO Code |
|---|---|---|---|
| 🇪🇸 Spanish | `es` | 🇧🇷 Portuguese | `pt` |
| 🇫🇷 French | `fr` | 🇮🇹 Italian | `it` |
| 🇩🇪 German | `de` | 🇷🇺 Russian | `ru` |
| 🇮🇳 Hindi | `hi` | 🇨🇳 Chinese (Simplified) | `zh` |
| 🇯🇵 Japanese | `ja` | 🇸🇦 Arabic | `ar` |
| 🇰🇷 Korean | `ko` | 🇳🇱 Dutch | `nl` |
| 🇹🇷 Turkish | `tr` | 🇵🇱 Polish | `pl` |
| 🇸🇪 Swedish | `sv` | | |

---

## 🏢 Internship Attribution

This project was built as **Task 3** of the **CodeAlpha Artificial Intelligence Internship** programme.

> **Organization:** [CodeAlpha](https://www.codealpha.tech/)
> **Programme:** Artificial Intelligence Internship
> **Task:** Language Translation Tool

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ by <strong>[Your Name]</strong> · CodeAlpha AI Internship 2024–2025
</div>
