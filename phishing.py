import pandas as pd

# --- 1. Cargar el archivo CSV ---
# Si tu archivo usa ";" como separador, cambia sep=";".
df = pd.read_csv("BDcorreos.csv")


# --- 2. Indicadores más específicos de phishing ---
indicadores = [
    # URLs sospechosas
    "http://", "https://", "secure", "update", "reset", "login",
    "validacion", "validar-datos", "verify", "confirm", "secure-login",
    # Mensajes típicos de phishing
    "suspendida temporalmente", "actividad inusual", "bloqueo de cuenta",
    "verifique su identidad", "confirmar sus credenciales",
    "restablecer contraseña", "pago inmediato", "factura pendiente",
    "descargue el archivo", "problema en la entrega",
    "hemos detectado un problema", "evitar suspension",
    # Estilo sospechoso
    "estimado usuario", "cliente apreciado",
    "ha sido seleccionado", "ha sido elegido",
]

# --- 3. Indicadores que reducen falsos positivos ---
indicadores_legitimos = [
    "ticket", "solicitud", "incidencia",
    "requerimiento", "caso", "mesa de ayuda",
    "soporte interno", "número de ticket",
]

def es_phishing(fila):
    contenido = f"{fila['email']} {fila['subject']} {fila['descriptions']}".lower()

    # Si contiene palabras de legitimidad → probablemente NO es phishing
    if any(legit in contenido for legit in indicadores_legitimos):
        return False

    # Detectar indicadores específicos
    return any(ind in contenido for ind in indicadores)

# --- 4. Clasificar correos ---
df["phishing"] = df.apply(es_phishing, axis=1)

# --- 5. Guardar archivo final ---
df.to_csv("correos_clasificados.csv", index=False)

print("Clasificación completa → correos_clasificados.csv")