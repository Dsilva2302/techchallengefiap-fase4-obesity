# 🚀 Tech Challenge FIAP – Fase 4  
## 🎯 Predição de Nível de Obesidade com Machine Learning

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte do **Tech Challenge – Fase 4** do curso de **Data Analytics da FIAP**.

O objetivo é desenvolver um modelo de Machine Learning capaz de prever o nível de obesidade de um indivíduo com base em características físicas e comportamentais.

---

## 🌐 Aplicação Online (Streamlit)

👉 **Acesse o App aqui:**  
https://techchallengefiap-fase4-obesity-xq43dtybxyfow4ngx4levf.streamlit.app/

---

## 🧠 Modelo Utilizado

Algoritmo: **Random Forest Classifier**

Motivos da escolha:
- Excelente performance para classificação multiclasses
- Baixo risco de overfitting
- Permite análise de importância das variáveis

---

## 📊 Resultado do Modelo

- 🎯 **Acurácia obtida:** 97,4%
- ✔ Supera o requisito mínimo de 75% estabelecido no desafio
- 📌 Variável mais relevante: BMI (Índice de Massa Corporal)

---

## 📂 Estrutura do Projeto

echchallengefiap-fase4-obesity
│
├── app.py
├── notebook_tc4_obesity.ipynb
├── model.joblib
├── requirements.txt
├── README.md
│
├── powerbi_assets/
│ ├── confusion_matrix.csv
│ ├── feature_importance_top30.csv
│ └── classification_report.csv
│
├── mockups/
│ ├── pagina1.png
│ ├── pagina2.png
│ ├── pagina3.png
│ └── pagina4.png
│
└── Relatorio_Tech_Challenge_FIAP_TC4.docx

---

## 🖥 Como Executar Localmente

1. Clone o repositório:

git clone https://github.com/seuusuario/techchallengefiap-fase4-obesity.git

2. Instale as dependências:
pip install -r requirements.txt


3. Execute o aplicativo:
streamlit run app.py


---

## 📈 Dashboard Power BI

O projeto inclui um dashboard analítico contendo:

- Distribuição dos níveis de obesidade
- Relação entre hábitos alimentares e obesidade
- Perfil demográfico
- Matriz de confusão do modelo
- Importância das variáveis

Arquivo:  
📊 `Dashboard_TC_Fase4.pbix`

---

## ⚠ Limitações

- Base de dados não clínica
- Possível overfitting devido à alta acurácia
- Não substitui avaliação médica profissional

---

## 🚀 Próximos Passos

- Validação cruzada
- Teste com base real
- Deploy via API REST
- Integração com sistemas de saúde

---

## 👨‍💻 Autor

Danilo dos Santos Silva  
Tech Challenge – FIAP Data Analytics





