import streamlit as st

from src.rag import ask

st.set_page_config(
    page_title="Delhi Tourism Assistant"
)

st.title(
    "🏛️ Delhi Tourism Assistant"
)

query = st.text_input(
    "Ask anything about Delhi"
)

if st.button("Ask"):

    answer, sources = ask(
        query
    )

    st.write(answer)

    st.write(
        "Sources:",
        ", ".join(sources)
    )