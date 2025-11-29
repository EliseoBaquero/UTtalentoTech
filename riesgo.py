import pandas as pd

sentiment_df = pd.read_csv('sentiment.csv')

user_sentiment_from_sentiment_file = sentiment_df.groupby('ID Usuario')['sentiment_score'].sum().reset_index()
user_sentiment_from_sentiment_file.rename(columns={'sentiment_score': 'Sentimiento acumulado'}, inplace=True)

def classify_risk(score):
    if score < -5:
        return 'High Risk'
    elif -5 <= score <= 0:
        return 'Medium Risk'
    else:
        return 'Low Risk'

user_sentiment_from_sentiment_file['Clasificacion de Riesgo'] = user_sentiment_from_sentiment_file['Sentimiento acumulado'].apply(classify_risk)

# Filtrar solo los usuarios de "High Risk" y guardar en un archivo CSV
high_risk_users = user_sentiment_from_sentiment_file[user_sentiment_from_sentiment_file['Clasificacion de Riesgo'] == 'High Risk']
high_risk_users.to_csv('riesgoalto.csv', index=False)

risk_counts_from_sentiment_file = user_sentiment_from_sentiment_file['Clasificacion de Riesgo'].value_counts().reindex(['High Risk', 'Medium Risk', 'Low Risk'])
risk_counts_from_sentiment_file = risk_counts_from_sentiment_file.fillna(0).astype(int)