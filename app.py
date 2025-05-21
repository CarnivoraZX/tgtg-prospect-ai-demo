import streamlit as st
import openai

st.title("Too Good To Go - B2B Kunde Evaluator (Demo)")

# Load OpenAI API key from secrets
openai.api_key = st.secrets["openai"]["api_key"]

st.write("Indtast virksomhedsdata for at evaluere potentiale:")

business_name = st.text_input("Virksomhedsnavn (fx Bageren A/S)")
business_type = st.selectbox("Virksomhedstype", ["Bager", "Restaurant", "Tankstation", "Café", "Andet"])
location = st.text_input("Lokation (by eller adresse)")

if st.button("Evaluer potentiale"):
    if not business_name or not location:
        st.error("Udfyld venligst både navn og lokation")
    else:
        prompt = f"""
        Vurder potentialet for at virksomheden '{business_name}', som er en '{business_type}' i '{location}', er relevant for Too Good To Go platformen for at sælge overskydende mad. Giv en kort begrundelse.
        """

        with st.spinner("Analyserer..."):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                temperature=0.7,
            )

        result = response.choices[0].text.strip()
        st.subheader("Evaluering")
        st.write(result)
