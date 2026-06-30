"""
=============================================================
 AI Language Translation Tool
 CodeAlpha Artificial Intelligence Internship
=============================================================
 Author  : [Your Name]
 Project : CodeAlpha_LanguageTranslationTool
 Stack   : Python 3.11+ | Streamlit | translate
 Flow    : Input → Language Selection → Processing → Output
=============================================================
"""

import streamlit as st
from translate import Translator

# ─────────────────────────────────────────────────────────────
# Page Configuration
# Must be the first Streamlit call in the script.
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────
# Custom CSS – Premium Dark-Mode UI
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Google Font ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* ── Global Reset ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── App Background ── */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #1a1a2e 50%, #16213e 100%);
        min-height: 100vh;
    }

    /* ── Main Content Container ── */
    .block-container {
        padding: 2.5rem 2rem 3rem 2rem;
        max-width: 780px;
    }

    /* ── Hero Header ── */
    .hero-header {
        text-align: center;
        padding: 2rem 0 1.5rem 0;
    }
    .hero-header h1 {
        font-size: 2.6rem;
        font-weight: 700;
        background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.3rem;
        line-height: 1.2;
    }
    .hero-header p {
        color: #94a3b8;
        font-size: 1rem;
        font-weight: 400;
        margin-top: 0;
    }

    /* ── Glass Card ── */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.10);
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.4rem;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
    }

    /* ── Section Label ── */
    .section-label {
        color: #a78bfa;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }

    /* ── Character Counter ── */
    .char-counter {
        text-align: right;
        font-size: 0.75rem;
        color: #64748b;
        margin-top: -0.6rem;
        margin-bottom: 0.8rem;
    }
    .char-counter.warning  { color: #f59e0b; }
    .char-counter.overflow { color: #ef4444; }

    /* ── Streamlit Textarea Override ── */
    textarea {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(167, 139, 250, 0.3) !important;
        border-radius: 10px !important;
        color: #e2e8f0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        resize: vertical !important;
    }
    textarea:focus {
        border-color: #a78bfa !important;
        box-shadow: 0 0 0 2px rgba(167, 139, 250, 0.25) !important;
    }

    /* ── Selectbox Override ── */
    .stSelectbox > div > div {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(167, 139, 250, 0.3) !important;
        border-radius: 10px !important;
        color: #e2e8f0 !important;
    }

    /* ── Primary Button ── */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
        color: #fff !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.65rem 1.5rem !important;
        transition: all 0.25s ease !important;
        letter-spacing: 0.02em;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #6d28d9, #4338ca) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 8px 24px rgba(124, 58, 237, 0.45) !important;
    }
    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* ── Success Box Override ── */
    .stAlert[data-baseweb="notification"] {
        border-radius: 12px !important;
    }

    /* ── Result Translation Box ── */
    .result-box {
        background: rgba(52, 211, 153, 0.08);
        border: 1px solid rgba(52, 211, 153, 0.30);
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        color: #d1fae5;
        font-size: 1.05rem;
        line-height: 1.7;
        word-wrap: break-word;
    }

    /* ── Divider ── */
    hr {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.07);
        margin: 1.2rem 0;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        color: #475569;
        font-size: 0.78rem;
        padding-top: 1.5rem;
    }
    .footer span { color: #7c3aed; }

    /* ── Spinner color ── */
    .stSpinner > div { border-top-color: #a78bfa !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────
# Supported Language Map
# key   → display name shown in the selectbox
# value → ISO 639-1 code consumed by the translate library
# ─────────────────────────────────────────────────────────────
LANGUAGE_MAP: dict[str, str] = {
    "🇪🇸 Spanish":    "es",
    "🇫🇷 French":     "fr",
    "🇩🇪 German":     "de",
    "🇮🇳 Hindi":      "hi",
    "🇯🇵 Japanese":   "ja",
    "🇧🇷 Portuguese": "pt",
    "🇮🇹 Italian":    "it",
    "🇷🇺 Russian":    "ru",
    "🇨🇳 Chinese (Simplified)": "zh",
    "🇸🇦 Arabic":     "ar",
    "🇰🇷 Korean":     "ko",
    "🇳🇱 Dutch":      "nl",
    "🇹🇷 Turkish":    "tr",
    "🇵🇱 Polish":     "pl",
    "🇸🇪 Swedish":    "sv",
}

CHAR_LIMIT = 500  # Maximum characters allowed per translation request

# ─────────────────────────────────────────────────────────────
# Session-State Initialisation
# Preserves values across reruns so the UI stays populated
# after the user clicks "Translate".
# ─────────────────────────────────────────────────────────────
if "source_text" not in st.session_state:
    st.session_state["source_text"] = ""
if "translated_text" not in st.session_state:
    st.session_state["translated_text"] = ""
if "selected_lang" not in st.session_state:
    st.session_state["selected_lang"] = list(LANGUAGE_MAP.keys())[0]


# ─────────────────────────────────────────────────────────────
# Helper Function: perform_translation
# ─────────────────────────────────────────────────────────────
def perform_translation(text: str, target_lang_code: str) -> str:
    """
    Translate *text* into the language identified by *target_lang_code*.

    Parameters
    ----------
    text            : The source string to translate.
    target_lang_code: ISO 639-1 code of the target language (e.g. "es").

    Returns
    -------
    Translated string on success, raises an exception on failure.
    """
    # The translate library defaults to English ("en") as the source.
    translator = Translator(to_lang=target_lang_code)
    result = translator.translate(text)
    return result


# ─────────────────────────────────────────────────────────────
# UI – Hero Header
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero-header">
        <h1>🌐 AI Language Translation Tool</h1>
        <p>Powered by open-source translation · No API key required · Instant results</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────
# UI – Input Card
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">📝 Source Text (English)</div>', unsafe_allow_html=True)

# ── INPUT: Text area (state preserved via session_state key) ──
source_text: str = st.text_area(
    label="Enter text to translate",
    value=st.session_state["source_text"],
    height=160,
    max_chars=CHAR_LIMIT,
    placeholder="Type or paste English text here…",
    label_visibility="collapsed",
    key="source_text",          # binds directly to session_state["source_text"]
)

# ── Character counter with colour feedback ──
char_count  = len(source_text)
remaining   = CHAR_LIMIT - char_count
counter_cls = "char-counter"
if remaining <= 50:
    counter_cls += " overflow" if remaining < 0 else " warning"

st.markdown(
    f'<div class="{counter_cls}">{char_count} / {CHAR_LIMIT} characters</div>',
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)  # close glass-card

# ─────────────────────────────────────────────────────────────
# UI – Options Card (Language + Translate Button)
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">🎯 Translation Settings</div>', unsafe_allow_html=True)

# ── SELECTION: Target language drop-down ──
col_lang, col_btn = st.columns([2, 1], gap="medium")

with col_lang:
    selected_display: str = st.selectbox(
        label="Target Language",
        options=list(LANGUAGE_MAP.keys()),
        index=list(LANGUAGE_MAP.keys()).index(st.session_state["selected_lang"]),
        key="selected_lang",   # binds directly to session_state["selected_lang"]
    )

with col_btn:
    st.markdown("<br>", unsafe_allow_html=True)   # vertical alignment nudge
    translate_clicked: bool = st.button("✨ Translate", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)  # close glass-card

# ─────────────────────────────────────────────────────────────
# PROCESSING: Translation Logic
# ─────────────────────────────────────────────────────────────
if translate_clicked:
    # Validate input before sending to the translation engine
    if not source_text.strip():
        st.warning("⚠️ Please enter some text before translating.")
    elif len(source_text) > CHAR_LIMIT:
        st.error(f"❌ Text exceeds the {CHAR_LIMIT}-character limit. Please shorten your input.")
    else:
        target_code: str = LANGUAGE_MAP[selected_display]

        # ── PROCESSING: Call the translation engine ──
        with st.spinner("Translating… please wait."):
            try:
                result = perform_translation(source_text, target_code)
                st.session_state["translated_text"] = result

            # ── ERROR HANDLING: Network or service issues ──
            except Exception as exc:
                st.session_state["translated_text"] = ""
                st.error(
                    f"❌ Translation failed. Please check your internet connection "
                    f"and try again.\n\n**Details:** `{exc}`"
                )

# ─────────────────────────────────────────────────────────────
# OUTPUT: Display Translated Result
# ─────────────────────────────────────────────────────────────
if st.session_state["translated_text"]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">✅ Translation Result</div>', unsafe_allow_html=True)

    # ── OUTPUT: Render translated text in a styled box ──
    st.markdown(
        f'<div class="result-box">{st.session_state["translated_text"]}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Copy-to-Clipboard Button ──
    # Uses Streamlit's st.code as a secondary copy surface and a
    # custom HTML/JS button for a seamless one-click copy experience.
    copy_col, _ = st.columns([1, 2])
    with copy_col:
        copy_js = f"""
        <button onclick="
            navigator.clipboard.writeText(`{st.session_state['translated_text'].replace('`', chr(96))}`)
            .then(() => {{ this.innerText = '✅ Copied!'; setTimeout(() => this.innerText = '📋 Copy Text', 2000); }})
            .catch(() => {{ this.innerText = '⚠️ Failed'; setTimeout(() => this.innerText = '📋 Copy Text', 2000); }});
        " style="
            background: linear-gradient(135deg, #1e40af, #1d4ed8);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1.1rem;
            font-size: 0.88rem;
            font-weight: 600;
            font-family: Inter, sans-serif;
            cursor: pointer;
            transition: all 0.2s ease;
            letter-spacing: 0.02em;
        "
        onmouseover="this.style.background='linear-gradient(135deg,#1e3a8a,#1e40af)'; this.style.transform='translateY(-1px)';"
        onmouseout="this.style.background='linear-gradient(135deg,#1e40af,#1d4ed8)'; this.style.transform='translateY(0)';"
        >📋 Copy Text</button>
        """
        st.markdown(copy_js, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # close glass-card

# ─────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="footer">
        Built with ❤️ for the
        <span>CodeAlpha Artificial Intelligence Internship</span>
        &nbsp;·&nbsp; Powered by Streamlit &amp; translate
    </div>
    """,
    unsafe_allow_html=True,
)
