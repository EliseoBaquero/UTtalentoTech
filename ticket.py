import pandas as pd

# Load the dataset
df_churn = pd.read_csv('BDanonimo_final.csv')

# Display the first few rows of the DataFrame to verify
#display(df_churn.head())

keywords_correctivo = [
    'problema', 'fallo', 'error', 'bug', 'no funciona', 'lento', 'pantalla', 'disco duro',
    'no enciende', 'congela', 'impresora no detectada', 'seguridad', 'malware', 'batería',
    'sobrecalentamiento', 'audio', 'cámara', 'micrófono', 'puerto usb', 'archivos corruptos',
    'reinicia', 'se apaga', 'inaceptable', 'frustrado', 'ayuda urgente', 'preocupado', 'solución rápida',
    'harto', 'impotente', 'garantía', 'diagnóstico remoto', 'virus', 'no arranca', 'pantallazos azules',
    'no se conecta a internet', 'drivers', 'actualización de seguridad', 'antivirus', 'no puedo instalar',
    'red local inaccesible', 'pérdida de datos', 'pantalla negro', 'reconocimiento de huella', 'bios/uefi',
    'teclas pegajosas', 'ruidos extraños', 'lentitud', 'gráficos', 'parpadea', 'se cierra solo', 'errores frecuentes'
]

keywords_evolutivo = [
    'solicitud', 'nueva característica', 'mejora', 'desarrollo', 'nueva aplicación',
    'propuesta', 'optimización', 'interfaz de usuario', 'nueva herramienta', 'automatización'
]

# Function to classify descriptions
def classify_maintenance_type(description):
    description_lower = description.lower()

    is_evolutivo = any(keyword in description_lower for keyword in keywords_evolutivo)
    is_correctivo = any(keyword in description_lower for keyword in keywords_correctivo)

    # Prioritize 'Mantenimiento Evolutivo' if it's clearly an evolutive request and not a corrective one.
    if is_evolutivo and not is_correctivo:
        return 'Mantenimiento Evolutivo'
    # Otherwise, classify as 'Mantenimiento Correctivo'. This covers cases that are purely corrective,
    # or a mix of both (defaulting to corrective unless purely evolutive), or neither (previously 'Otro').
    else:
        return 'Mantenimiento Correctivo'

# Apply the classification function to the 'subject' column
df_churn['tipo_mantenimiento'] = df_churn['subject'].apply(classify_maintenance_type)

#print("Classification of 'subject' completed. 'Otro' category has been reclassified as 'Mantenimiento Correctivo'.")
#display(df_churn.head())

# Display the counts for each maintenance type
print("\nCounts of each maintenance type:")
print(df_churn['tipo_mantenimiento'].value_counts())

# Save the DataFrame with the new classification to a CSV file
df_churn.to_csv('clasificacion.csv', index=False)