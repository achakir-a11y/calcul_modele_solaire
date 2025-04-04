import streamlit as st
import numpy as np
from fpdf import FPDF

# Configuration de la page
st.set_page_config(page_title="Modèle Solaire", page_icon="☀️", layout="wide")

# Barre latérale
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["Accueil", "Méthode à 5 points", "Bibliographie", "Contact"])


# Fonction pour générer un PDF
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Rapport du Modèle Solaire", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, "Résultats calculés ici...", ln=True)
    pdf.output("rapport_modele_solaire.pdf")
    return "rapport_modele_solaire.pdf"


# Affichage du contenu selon la page sélectionnée
if page == "Accueil":
    st.title("Modèle Solaire - Simulation et Calculs")
    st.image("figure.PNG", caption="Caractéristiques I-V d'une cellule solaire", use_container_width=True)
    # Ajout d'un bouton de téléchargement
    if st.button("Télécharger le rapport en PDF"):
        pdf_file = generate_pdf()
        with open(pdf_file, "rb") as f:
            st.download_button("Télécharger", f, file_name="rapport_modele_solaire.pdf")

elif page == "Méthode à 5 points":
    st.title("Méthode à 5 Points")
    st.write("""
    La méthode à 5 points est une technique utilisée pour...
    (Explication détaillée ici)
    """)

elif page == "Bibliographie":
    st.title("Bibliographie de Dr. Ahmed Kotbi")
    st.write("""
    Dr. Ahmed Kotbi est un chercheur expérimenté dans le domaine des capteurs de gaz,
    des matériaux semi-conducteurs bidimensionnels et de la fabrication du graphène.
    Il a mené plusieurs projets en collaboration avec des institutions académiques en France et au Maroc...
    """)

elif page == "Contact":
    st.title("Contact")
    st.write("""
    **Email** : ahmed.kotbi@example.com  
    **LinkedIn** : [linkedin.com/in/ahmedkotbi](https://www.linkedin.com/in/ahmedkotbi)  
    """)

# Constantes physiques
k = 1.380649e-23  # Constante de Boltzmann (J/K)
q = 1.602176634e-19  # Charge de l'électron (C)
T = 300.0  # Température (K)

# Titre de l'application
st.title("Calcul des paramètres du modèle équivalent d'une cellule solaire - Modèle à 5 points")
st.markdown("""
Ce site permet de calculer les paramètres du modèle électrique équivalent d’une cellule solaire 
en utilisant la méthode à cinq points. Il est destiné aux chercheurs, ingénieurs et étudiants 
travaillant dans le domaine du photovoltaïque.
""")

# Affichage d'une image explicative
st.write("""
## Méthode des 5 points pour le calcul des paramètres du modèle électrique équivalent d'une cellule solaire

Cette méthode permet d'extraire les principaux paramètres d'une cellule solaire en se basant sur cinq points caractéristiques de la courbe I-V :
- **(Isc, 0)** : Le courant de court-circuit
- **(Voc, 0)** : La tension à vide
- **(Vm, Im)** : Le point de puissance maximale
- Deux points supplémentaires pour l'estimation des résistances série et shunt.

À partir de ces points, on peut calculer :
- La **résistance série** (Rs) en analysant deux points à faible courant.
- La **résistance shunt** (Rsh) en analysant deux points à faible tension.
- Le **facteur d’idéalité** (A) en utilisant la relation logarithmique entre les courants et les tensions.
- Le **courant de saturation inverse** (I0) et le **courant photogénéré** (Iph).

Cette méthode est souvent utilisée en recherche pour caractériser les cellules photovoltaïques de manière rapide et efficace.
""")

st.write("### Réalisé par : **Dr. Ahmed Kotbi**")
st.write("### Post-doc à l'Université de Picardie Jules verne")
# Ajout de la section "À propos de l'auteur"

st.sidebar.title("📖 Biographie")

st.sidebar.info("""
### **Dr. Ahmed Kotbi**
**Chercheur spécialisé** en matériaux semi-conducteurs et capteurs de gaz.

### **🎓 Formation et Expérience**
- Expert en **PECVD, CVD, PVD, Sol-Gel (Spin Coating, Dip Coating, Spray Pyrolysis)**.
- Collaborations : **MAScIR (Maroc), Université de Technologie de Compiègne (France)**.
- Développement de **capteurs de gaz HF** et **filtres optiques pour applications biologiques**.

### **🔬 Contributions Scientifiques**
- **Brevet sur la fabrication du Graphène** par PECVD.
- **Optimisation de la croissance du Graphène** via la **méthode Taguchi**.
- Encadrement de **doctorants et étudiants** en **énergétique et optoélectronique**.

### **📞 Contact**
📧 Email : [ahmed.kotbi@u-picardie.fr](mailto:ahmed.kotbi@u-picardie.fr)  
🔗 LinkedIn : [linkedin.com/in/votreprofil](https://www.linkedin.com/in/ahmed-kotbi-1398bab9/)  
""")




# Ajout de la section "📬 Contact"
st.sidebar.header("📬 Contact")
st.sidebar.info(
    """
    📧 **Email :** [kotbi.ahmed7@gmail.com](mailto:kotbi.ahmed7@gmail.com)  
    🔗 **LinkedIn :** [linkedin.com/in/ahmedkotbi](https://www.linkedin.com/in/ahmed-kotbi-1398bab9/)  
    🏫 **Institution :** Université de Picardie Jules Verne / Centre de recherche: Laboratoire de physique de la matière condensée / Amiens / France  
    """
)


st.image("figure_ok.PNG", caption="Caractéristiques I-V d'une cellule solaire", use_container_width=True)




# Entrée des paramètres par l'utilisateur
Isc = st.number_input("Courant de court-circuit (Isc) [A]", format="%.6f")
Voc = st.number_input("Tension à vide (Voc) [V]", format="%.6f")
Vm = st.number_input("Tension au point de puissance max (Vm) [V]", format="%.6f")
Im = st.number_input("Courant au point de puissance max (Im) [A]", format="%.6f")


V1_Rs0 = st.number_input("V1 pour Rs [V]", format="%.6f")
I1_Rs0 = st.number_input("I1 pour Rs [A]", format="%.6f")
V2_Rs0 = st.number_input("V2 pour Rs [V]", format="%.6f")
I2_Rs0 = st.number_input("I2 pour Rs [A]", format="%.6f")

V1_Rsh0 = st.number_input("V1 pour Rsh [V]", format="%.6f")
I1_Rsh0 = st.number_input("I1 pour Rsh [A]", format="%.6f")
V2_Rsh0 = st.number_input("V2 pour Rsh [V]", format="%.6f")
I2_Rsh0 = st.number_input("I2 pour Rsh [A]", format="%.6f")

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

# Pied de page
st.markdown("""---  
© 2025 Ahmed Kotbi – Tous droits réservés.
""")


