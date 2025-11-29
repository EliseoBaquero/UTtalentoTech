import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('BDcorreos.csv')

phishing_keywords = [
    "urgente", "verificar cuenta", "alerta de seguridad", "acción requerida",
    "actividad sospechosa", "actualización de contraseña", "haga clic aquí",
    "confirmar información", "cuenta suspendida", "actividad inesperada",
    "restablecer contraseña", "pago fallido"
]

def label_phishing(row):
    combined_text = str(row['subject']) + " " + str(row['descriptions'])
    combined_text_lower = combined_text.lower()
    for keyword in phishing_keywords:
        if keyword in combined_text_lower:
            return 1
    return 0

df['is_phishing'] = df.apply(label_phishing, axis=1)

df['fecha_recepcion_requerimiento'] = pd.to_datetime(df['fecha_recepcion_requerimiento'])
df['hour_of_day'] = df['fecha_recepcion_requerimiento'].dt.hour
df['day_of_week'] = df['fecha_recepcion_requerimiento'].dt.dayofweek
df['email_domain'] = df['email'].apply(lambda x: x.split('@')[1])
df['subject_length'] = df['subject'].apply(len)
df['description_length'] = df['descriptions'].apply(len)

categorical_cols = ['email_domain', 'day_of_week']
df['day_of_week'] = df['day_of_week'].astype(str)
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
df = df.drop(columns=['email', 'subject', 'descriptions', 'fecha_recepcion_requerimiento'])

X = df.drop('is_phishing', axis=1)
y = df['is_phishing']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

X_all = df.drop('is_phishing', axis=1)
df['predicted_phishing'] = (model.predict_proba(X_all)[:, 1] > 0.5).astype(int)
phishing_count = df['predicted_phishing'].sum()

non_phishing_df = df[df['predicted_phishing'] == 0].copy()
non_phishing_df.to_csv('classified_emails.csv', index=False)

print("\nRendimiento del modelo XGBoost:")
print(f"  Precisión: {accuracy:.4f}")
print(f"  Exactitud: {precision:.4f}")
print(f"  Sensibilidad: {recall:.4f}")
print(f"  Puntuación F1: {f1:.4f}")
print(f"\nEl modelo detectó {int(phishing_count)} correos electrónicos como phishing en el conjunto de datos.")
