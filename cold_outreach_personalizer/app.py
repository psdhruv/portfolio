import streamlit as st

st.set_page_config(
    page_title="Cold Outreach Personalizer",
    page_icon="✉️",
    layout="centered"
)

st.markdown("""
<style>
    .block-container { max-width: 760px; padding-top: 2rem; }
    .step-pill { display: inline-block; background: #1a1a2e; color: #fff;
                 border-radius: 20px; padding: 2px 12px; font-size: 0.72rem;
                 font-weight: 700; letter-spacing: 0.06em; margin-bottom: 0.6rem; }
    .banner { background: #e3f2fd; border: 1px solid #90caf9; border-radius: 8px;
              padding: 0.75rem 1rem; font-size: 0.88rem; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("## ✉️ Cold Outreach Personalizer")
st.caption("Fill the form → copy the request → paste into Claude → get your messages")
st.divider()

# ── YOUR INFO ─────────────────────────────────────────────────────────────────
st.markdown('<span class="step-pill">1 · Your Info</span>', unsafe_allow_html=True)
your_name = st.text_input("Your name", value="Dhruv Patel")
your_bg   = st.text_area(
    "Your background",
    value="Data scientist at Uber leading CRM AI products. IIT Kanpur MTech, Rank 1. "
          "Joining Columbia Business School MBA Fall 2026. Transitioning into AI Product Management.",
    height=80
)

st.divider()

# ── THEIR INFO ────────────────────────────────────────────────────────────────
st.markdown('<span class="step-pill">2 · Who You\'re Reaching Out To</span>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    their_name    = st.text_input("Their name",  placeholder="e.g. Priya Sharma")
with c2:
    their_company = st.text_input("Company",     placeholder="e.g. Google")

their_role    = st.text_input("Role / Title", placeholder="e.g. Senior Product Manager, AI")
their_context = st.text_area(
    "Context — LinkedIn bio, a post they wrote, career history, anything specific",
    placeholder="e.g. Led Gemini's recommendation layer. Previously at Meta on Feed ranking. IIT Delhi grad.",
    height=110
)

st.divider()

# ── GOAL & TONE ───────────────────────────────────────────────────────────────
st.markdown('<span class="step-pill">3 · Goal & Style</span>', unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3:
    goal = st.selectbox("What do you want?", [
        "Informational interview (20 min call)",
        "Advice on DS → PM transition",
        "Advice on AI PM recruiting",
        "Referral or intro to their team",
        "Connect before CBS starts",
        "Feedback on my portfolio / work",
    ])
with c4:
    tone = st.selectbox("Tone", [
        "Professional & warm",
        "Casual & direct",
        "Formal",
    ])

platform = st.selectbox("Platform", [
    "LinkedIn message (300 char limit)",
    "LinkedIn InMail (up to 200 words)",
    "Email",
])

st.divider()

# ── GENERATE REQUEST ──────────────────────────────────────────────────────────
if st.button("⚡ Generate Request", type="primary", use_container_width=True):
    if not their_name or not their_role or not their_context:
        st.warning("Fill in the recipient's name, role, and context to continue.")
    else:
        char_note = {
            "LinkedIn message (300 char limit)": "STRICT 300-character limit.",
            "LinkedIn InMail (up to 200 words)":  "Up to 200 words.",
            "Email":                               "3-4 short punchy paragraphs.",
        }[platform]

        request = (
            f"Generate 3 cold outreach message variations for me.\n\n"
            f"SENDER: {your_name} — {your_bg}\n\n"
            f"RECIPIENT: {their_name}, {their_role} at {their_company}\n"
            f"CONTEXT: {their_context}\n\n"
            f"GOAL: {goal}\n"
            f"TONE: {tone}\n"
            f"PLATFORM: {platform} — {char_note}\n\n"
            f"Rules:\n"
            f"- Reference something SPECIFIC about them — no generic flattery\n"
            f"- Lead with who I am in one crisp line\n"
            f"- State the ask clearly, make it easy to say yes\n"
            f"- No filler openers (\"Hope this finds you well\" etc.)\n"
            f"- End with a clear call-to-action\n\n"
            f"Format each as:\n"
            f"**Variation N — [angle]:** [message]\n\n"
            f"End with one line recommending which to send and why."
        )

        st.session_state["request"] = request

if st.session_state.get("request"):
    st.markdown('<span class="step-pill">4 · Copy → Paste into Claude chat → Get your messages</span>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="banner">📋 Copy the text below and paste it directly into your Claude chat window.</div>',
        unsafe_allow_html=True
    )
    st.text_area("Your request (copy this)", value=st.session_state["request"],
                 height=220, key="req_box")
