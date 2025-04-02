 
import numpy as np
import streamlit as st

# Constantes physiques
k = 1.380649e-23  # Constante de Boltzmann (J/K)
q = 1.602176634e-19  # Charge de l'électron (C)
T = 300.0  # Température (K)

st.title("Calcul des Paramètres du Modèle Électrique Équivalent de la Cellule Solaire")

# Entrée des données par l'utilisateur
Isc = st.number_input("Courant de court-circuit (Isc) [A]", value=1.0)
Voc = st.number_input("Tension à vide (Voc) [V]", value=0.6)
Vm = st.number_input("Tension au point de puissance maximale (Vm) [V]", value=0.5)
Im = st.number_input("Courant au point de puissance maximale (Im) [A]", value=0.8)
V1_Rs0 = st.number_input("Tension V1 pour Rs [V]", value=0.1)
I1_Rs0 = st.number_input("Courant I1 pour Rs [A]", value=0.9)
V2_Rs0 = st.number_input("Tension V2 pour Rs [V]", value=0.2)
I2_Rs0 = st.number_input("Courant I2 pour Rs [A]", value=0.85)
V1_Rsh0 = st.number_input("Tension V1 pour Rsh [V]", value=0.2)
I1_Rsh0 = st.number_input("Courant I1 pour Rsh [A]", value=0.01)
V2_Rsh0 = st.number_input("Tension V2 pour Rsh [V]", value=0.3)
I2_Rsh0 = st.number_input("Courant I2 pour Rsh [A]", value=0.015)

# Calcul des résistances
Rs0 = -(V2_Rs0 - V1_Rs0) / (I2_Rs0 - I1_Rs0)
Rsh0 = -(V2_Rsh0 - V1_Rsh0) / (I2_Rsh0 - I1_Rsh0)

# Calcul du facteur d'idéalité A
A = (Vm + (Im * Rs0) - Voc) / (
    np.log(Isc - (Vm / Rsh0) - Im) - np.log(Isc - (Voc / Rsh0)) + (Im / (Isc - (Voc / Rsh0)))
)

# Calcul du courant de saturation inverse I0
I0 = (Isc - (Voc / Rsh0)) * np.exp(-Voc / A)

# Calcul de la résistance série Rs
Rs = Rs0 - ((A / I0) * np.exp(-Voc / A))

# Calcul de la résistance shunt Rsh
Rsh = Rsh0

# Calcul du courant photogénéré Iph
Iph = Isc * (1.0 + (Rs / Rsh)) + I0 * (np.exp((Isc * Rs) / A) - 1.0)

# Affichage des résultats
st.write("### Résultats")
st.write(f"Courant photogénéré (Iph) : {Iph:.6f} A")
st.write(f"Courant de saturation (I0) : {I0:.6e} A")
st.write(f"Facteur d'idéalité (A) : {A:.6f}")
st.write(f"Résistance série (Rs) : {Rs:.6f} Ω")
st.write(f"Résistance shunt (Rsh) : {Rsh:.6f} Ω")
