import streamlit as st
import numpy as np

# Constantes physiques
k = 1.380649e-23  # Constante de Boltzmann (J/K)
q = 1.602176634e-19  # Charge de l'électron (C)
T = 300.0  # Température (K)

# Titre de l'application
st.title("Calcul des paramètres du modèle équivalent d'une cellule solaire")
# Affichage d'une image explicative
st.image("figure_ok.png", caption="Caractéristiques I-V d'une cellule solaire", use_column_width=True)

# Entrée des paramètres par l'utilisateur
Isc = st.number_input("Courant de court-circuit (Isc) [A]", min_value=0.0)
Voc = st.number_input("Tension à vide (Voc) [V]", min_value=0.0)
Vm = st.number_input("Tension au point de puissance max (Vm) [V]", min_value=0.0)
Im = st.number_input("Courant au point de puissance max (Im) [A]", min_value=0.0)


V1_Rs0 = st.number_input("V1 pour Rs [V]", min_value=0.0)
I1_Rs0 = st.number_input("I1 pour Rs [A]", min_value=0.0)
V2_Rs0 = st.number_input("V2 pour Rs [V]", min_value=0.0)
I2_Rs0 = st.number_input("I2 pour Rs [A]", min_value=0.0)

V1_Rsh0 = st.number_input("V1 pour Rsh [V]", min_value=0.0)
I1_Rsh0 = st.number_input("I1 pour Rsh [A]", min_value=0.0)
V2_Rsh0 = st.number_input("V2 pour Rsh [V]", min_value=0.0)
I2_Rsh0 = st.number_input("I2 pour Rsh [A]", min_value=0.0)

# Bouton pour exécuter le calcul
if st.button("Calculer"):
    Rs0 = -(V2_Rs0 - V1_Rs0) / (I2_Rs0 - I1_Rs0)
    Rsh0 = -(V2_Rsh0 - V1_Rsh0) / (I2_Rsh0 - I1_Rsh0)

    A = (Vm + (Im * Rs0) - Voc) / (
        np.log(Isc - (Vm / Rsh0) - Im) - np.log(Isc - (Voc / Rsh0)) + (Im / (Isc - (Voc / Rsh0)))
    )

    I0 = (Isc - (Voc / Rsh0)) * np.exp(-Voc / A)
    Rs = Rs0 - ((A / I0) * np.exp(-Voc / A))
    Rsh = Rsh0
    Iph = Isc * (1.0 + (Rs / Rsh)) + I0 * (np.exp((Isc * Rs) / A) - 1.0)

    # Affichage des résultats
    st.write(f"**Courant photogénéré (Iph) :** {Iph:.6f} A")
    st.write(f"**Courant de saturation inverse (I0) :** {I0:.6e} A")
    st.write(f"**Facteur d'idéalité (A) :** {A:.4f}")
    st.write(f"**Résistance série (Rs) :** {Rs:.4f} Ω")
    st.write(f"**Résistance shunt (Rsh) :** {Rsh:.4f} Ω")
