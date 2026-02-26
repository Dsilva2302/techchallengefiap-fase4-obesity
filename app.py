import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Tech Challenge FIAP – Obesidade", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load("model.joblib")

model = load_model()

st.title("Predição de Nível de Obesidade (Tech Challenge – FIAP)")
st.caption("Informe os dados abaixo e clique em **Prever**.")

# Inputs (compatíveis com o dataset)
col1, col2, col3 = st.columns(3)

with col1:
    Gender = st.selectbox("Gênero", ["Female", "Male"])
    Age = st.number_input("Idade", min_value=1, max_value=120, value=25, step=1)
    Height = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=1.70, step=0.01)
    Weight = st.number_input("Peso (kg)", min_value=10.0, max_value=300.0, value=70.0, step=0.1)

with col2:
    family_history = st.selectbox("Histórico familiar de sobrepeso", ["yes", "no"])
    FAVC = st.selectbox("Consumo frequente de comida calórica (FAVC)", ["yes", "no"])
    FCVC = st.slider("Consumo de vegetais (FCVC) – 1 a 3", 1, 3, 2)
    NCP = st.slider("Número de refeições principais (NCP) – 1 a 4", 1, 4, 3)
    CAEC = st.selectbox("Comer entre refeições (CAEC)", ["no", "Sometimes", "Frequently", "Always"])

with col3:
    SMOKE = st.selectbox("Fuma (SMOKE)", ["yes", "no"])
    CH2O = st.slider("Consumo de água (CH2O) – 1 a 3", 1, 3, 2)
    SCC = st.selectbox("Monitora calorias (SCC)", ["yes", "no"])
    FAF = st.slider("Atividade física (FAF) – 0 a 3", 0, 3, 1)
    TUE = st.slider("Tempo em dispositivos (TUE) – 0 a 2", 0, 2, 1)
    CALC = st.selectbox("Consumo de álcool (CALC)", ["no", "Sometimes", "Frequently", "Always"])
    MTRANS = st.selectbox("Meio de transporte (MTRANS)", 
                          ["Public_Transportation", "Automobile", "Walking", "Motorbike", "Bike"])

BMI = Weight / (Height * Height)
st.metric("BMI calculado", f"{BMI:.2f}")

if st.button("Prever"):
    row = {
        "Gender": Gender,
        "Age": float(Age),
        "Height": float(Height),
        "Weight": float(Weight),
        "family_history": family_history,
        "FAVC": FAVC,
        "FCVC": int(FCVC),
        "NCP": int(NCP),
        "CAEC": CAEC,
        "SMOKE": SMOKE,
        "CH2O": int(CH2O),
        "SCC": SCC,
        "FAF": int(FAF),
        "TUE": int(TUE),
        "CALC": CALC,
        "MTRANS": MTRANS,
        "BMI": float(BMI),
    }
    X = pd.DataFrame([row])
    pred = model.predict(X)[0]
    st.success(f"**Predição:** {pred}")
