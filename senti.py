import pandas as pd
from pysentimiento.analyzer import create_analyzer

df = pd.read_csv('clasificacion.csv')
analyzer = create_analyzer(task="sentiment", model_name="pysentimiento/robertuito-sentiment-analysis", lang="es")

def get_sentiment_score(sentiment_result):
    if sentiment_result.output == 'POS':
        return 1
    elif sentiment_result.output == 'NEU':
        return 0
    elif sentiment_result.output == 'NEG':
        return -1
    return 0

df['sentiment_results'] = df['descriptions_anonymized'].apply(lambda x: analyzer.predict(x))
df['sentiment_score'] = df['sentiment_results'].apply(get_sentiment_score)
sentiment_output_df = df[['ID Usuario', 'descriptions_anonymized', 'sentiment_results', 'sentiment_score']]
sentiment_output_df.to_csv('sentiment.csv', index=False)