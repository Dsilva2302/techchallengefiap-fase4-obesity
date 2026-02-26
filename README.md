# Tech Challenge – FIAP (Data Analytics) – Fase 4
## Predição de Nível de Obesidade (Classificação Multiclasse)

### 1) Como rodar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

### 2) Notebook
Abra o `notebook_tc4_obesity.ipynb` para:
- EDA e preparação
- Treinamento do modelo (Random Forest)
- Avaliação (acurácia, matriz de confusão, relatório)
- Exportação de artefatos para o Power BI (`/powerbi_assets`)

### 3) Power BI
Importe os CSVs da pasta `powerbi_assets`:
- `class_distribution.csv`
- `feature_importance_top30.csv`
- `confusion_matrix.csv`
- `classification_report.csv`

E conecte com a base principal (`obesity_dataset.csv.csv`) para construir as páginas:
1. Visão Geral
2. Hábitos e comportamento
3. Perfil demográfico
4. Performance do modelo
