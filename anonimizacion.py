import pandas as pd
import re

def main():
    df_correos_original = pd.read_csv('classified_emails.csv')

    unique_emails_df = df_correos_original['email'].drop_duplicates().reset_index(drop=True)
    df_usuarios = pd.DataFrame(unique_emails_df)

    df_usuarios['ID Usuario'] = range(10000, 10000 + len(df_usuarios))
    df_usuarios['ID Usuario'] = df_usuarios['ID Usuario'].apply(lambda x: str(x).zfill(7))
    df_usuarios = df_usuarios[['ID Usuario', 'email']]
    df_usuarios.to_csv('BDUsuarios.csv', index=False)
    print("BDUsuarios.csv created successfully.")

    df_correos_original['descriptions_anonymized'] = df_correos_original['descriptions'].str.lower()

    first_names = [
        'ana', 'maria', 'carmen', 'laura', 'sofia', 'isabel', 'lucia', 'elena', 'paula', 'marta',
        'alba', 'clara', 'andrea', 'julia', 'irene', 'daniela', 'valeria', 'sara', 'rocio', 'patricia',
        'alejandro', 'daniel', 'pablo', 'david', 'javier', 'sergio', 'carlos', 'manuel', 'adrian', 'alvaro',
        'marco', 'iker', 'gonzalo', 'diego', 'hugo', 'mateo', 'nicolas', 'martin', 'lucas', 'leo',
        'antonio', 'jose', 'francisco', 'juan', 'pedro', 'miguel', 'rafael', 'luis', 'fernando', 'jorge',
        'lina', 'pedro', 'maria', 'ana', 'elena', 'gustavo', 'angie', 'wendy', 'diego', 'jaime',
        'roberto', 'sandra', 'natalia', 'gabriel', 'valeria', 'sofia', 'camila', 'juan', 'andres', 'lorena',
        'santiago', 'valentina', 'sebastian', 'mariana', 'juliana', 'david', 'esteban', 'carolina', 'pablo', 'ximena',
        'alexandra', 'ricardo', 'adriana', 'mauricio', 'paola', 'fabian', 'vanessa', 'jessica', 'oscar', 'adriana',
        'felipe', 'veronica', 'daniela', 'camilo', 'alejandra', 'sara', 'andrea', 'diana', 'monica', 'victor', 'gina',
        'maría', 'josé', 'jesús', 'ángel', 'álvaro', 'méndez', 'sánchez'
    ]
    last_names = [
        'garcia', 'fernandez', 'gonzalez', 'rodriguez', 'lopez', 'martinez', 'sanchez', 'perez', 'gomez', 'martin',
        'jimenez', 'hernandez', 'diaz', 'moreno', 'muñoz', 'alvarez', 'romero', 'alonso', 'gutierrez', 'navarro',
        'torres', 'dominguez', 'vazquez', 'ramos', 'ruiz', 'serrano', 'mendez', 'castro', 'ortega', 'rubio',
        'morales', 'sanz', 'cruz', 'ortiz', 'gallego', 'delgado', 'ramirez', 'castillo', 'nuñez', 'herrera',
        'flores', 'blanco', 'prieto', 'mendoza', 'vega', 'aguilar', 'rey', 'cabrera', 'pascual', 'montes',
        'suarez', 'diez', 'vidal', 'iglesias', 'ruiz', 'garcia', 'martinez', 'garcia', 'lopez', 'diaz', 'gonzález',
        'rodriguez', 'serrano', 'aguilar', 'lopez', 'diaz', 'barrientos', 'parra', 'garcia', 'fernandez', 'gomez',
        'perez', 'sanchez', 'romero', 'moreno', 'jimenez', 'ruiz', 'gutierrez', 'alonso', 'mendez', 'castro',
        'ortega', 'rubio', 'morales', 'sanz', 'cruz', 'ortiz', 'gallego', 'delgado', 'ramirez', 'castillo',
        'nuñez', 'herrera', 'flores', 'blanco', 'prieto', 'mendoza', 'vega', 'salas', 'soto', 'moya',
        'martínez', 'garcía', 'pérez', 'lópez', 'gómez', 'díaz', 'sánchez', 'muñoz', 'hernández', 'jiménez', 'fernández', 'rodríguez'
    ]
    full_names = [f'{first} {last}' for first in first_names for last in last_names]
    company_names_extended = [
        'alpha tech', 'tech solutions', 'beta systems', 'innovate corp', 'global dynamics',
        'cyber security inc', 'data stream corp', 'network solutions', 'cloud computing ltd', 'smart systems ag',
        'digital innovations', 'web services llc', 'tech giants', 'software inc', 'it solutions group',
        'delta systems', 'precision tech', 'future soft', 'dynamic corp', 'prime solutions'
    ]
    terms_to_anonymize_extended = list(set(
        first_names + last_names + full_names + company_names_extended
    ))
    terms_to_anonymize_extended_sorted = sorted(terms_to_anonymize_extended, key=len, reverse=True)

    for term in terms_to_anonymize_extended_sorted:
        df_correos_original['descriptions_anonymized'] = df_correos_original['descriptions_anonymized'].str.replace(
            r'\b' + re.escape(term) + r'\b', 'XY', flags=re.IGNORECASE, regex=True
        )

    df_anonimo_merged = pd.merge(df_correos_original, df_usuarios, on='email', how='left')
    df_anonimo_final = df_anonimo_merged[['ID Usuario', 'subject', 'fecha_recepcion_requerimiento', 'descriptions_anonymized']]
    df_anonimo_final.to_csv('BDanonimo_final.csv', index=False)
    print("Anonymized data saved to 'BDanonimo_final.csv'")

    print("\nFirst 5 rows of BDanonimo_final.csv:")
    print(df_anonimo_final.head())

if __name__ == "__main__":
    main()
