import streamlit as st
import pandas as pd
import joblib  # Charger les objets nécessaires

# Charger le modèle et le scaler
rf_model = joblib.load(r".\rf_model.pkl")
scaler = joblib.load(r".\scaler.pkl")

# Détails des clusters
cluster_to_details = {
    0: {'marque': 'Renault', 'nom': '120i', 'puissance': 164.38, 'longueur': 'longue', 'couleur': 'blanc', 'categorie': 'Familiale', 'description': '👨‍👩‍👧‍👦 Voitures spacieuses, conçues pour les familles. Idéales pour les trajets quotidiens et les vacances en famille.'},
    1: {'marque': 'BMW', 'nom': 'M5', 'puissance': 507.0, 'longueur': 'très longue', 'couleur': 'blanc', 'categorie': 'Sportive', 'description': '🏎️ Véhicules haute performance, parfaits pour ceux qui recherchent des sensations fortes et un design dynamique.'},
    2: {'marque': 'Volkswagen', 'nom': '1007 1.4', 'puissance': 95.13, 'longueur': 'courte', 'couleur': 'blanc', 'categorie': 'Routière', 'description': '🛣️ Voitures confortables et stables, adaptées pour les longs trajets. Offrent une conduite douce et un bon espace pour les passagers.'},
    3: {'marque': 'Mercedes', 'nom': 'S500', 'puissance': 282.25, 'longueur': 'très longue', 'couleur': 'blanc', 'categorie': 'Voiture de luxe', 'description': '💎 Véhicules haut de gamme, offrant des équipements sophistiqués et un confort exceptionnel pour ceux qui recherchent le raffinement.'}
}

# Configuration de la page
st.set_page_config(page_title="Recommandation de Véhicules", page_icon="🚗", layout="wide")

st.sidebar.image("sidebar_image.jpg", caption="Recommandation automobile", use_column_width=True)
# Barre latérale
st.sidebar.title("À propos de l'application")
st.sidebar.write("""
                 <div style="text-align: justify;">
                    Cette application vous aide à choisir le véhicule le plus adapté à vos besoins.
                  Basée sur des techniques avancées de machine learning, elle analyse vos informations
                  personnelles et recommande un véhicule en fonction de vos préférences et de vos besoins.
                   </div>
""", unsafe_allow_html=True)


st.sidebar.markdown("---")  # Ligne de séparation

st.sidebar.title("Réalisateur :")
st.sidebar.markdown("**Nohayla Anoada**")
st.sidebar.markdown("""
                    <div style="text-align: justify;">
Etudiante en Master en Intelligence Artificielle 🤖 et Analyse de Données 📊 à la Faculté des Sciences de Meknès. 
                    Passionnée par la création de solutions innovantes qui combinent le développement web 🌐 avec des techniques 
                    avancées d'apprentissage automatique 🧠 et d'apprentissage profond 🔍.
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")  # Ligne de séparation

st.sidebar.title("Encadrant :")
st.sidebar.markdown("**Professeur El Moukhtar Zemmouri**")
st.sidebar.markdown("""
                    <div style="text-align: justify;">
                    Professeur Assistant 👨‍🏫 à l’Ecole Nationale Supérieure d’Arts et Métiers-Meknès 🇲🇦. Il a obtenu son doctorat 🎓 en Génie Informatique 
                    💻 en 2013 de l’ENSAM-Meknès, et son diplôme d’ingénieur d’état 📜 en Informatique et Télécommunications 📡 en 2003 de l’INPT-Rabat.
                    </div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")  # Ligne de séparation

st.markdown("""
    <style>
        .st-emotion-cache-nok2kl a {
            color: inherit !important; /* Hérite de la couleur par défaut de l'élément parent */
            text-decoration: none !important; /* Supprime la décoration si nécessaire */
        }
    </style>
""", unsafe_allow_html=True)


# Ajouter les liens Font Awesome pour les icônes
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)

# Liens sociaux avec icônes
st.sidebar.markdown("""
    ### 🔗 Connectez-vous avec moi :
    <a href="https://www.linkedin.com/in/nohayla-anoada-45ab671b8/" target="_blank">
        <i class="fa fa-linkedin" style="font-size:30px; color:#0077b5; margin-right: 10px;"></i>
    </a>
    <a href="https://github.com/NohaylaA" target="_blank">
        <i class="fa fa-github" style="font-size:30px; color:#333; margin-right: 10px;"></i>
    </a>
    <a href="mailto:anoada.nohayla01@gmail.com" target="_blank">
        <i class="fa fa-envelope" style="font-size:30px; color:#D14836;"></i>
    </a>
""", unsafe_allow_html=True)





st.image("accueil_image.png", use_column_width=True)  # Ajouter une image de présentation
st.markdown("<h1 style='text-align: center;'>Application de Recommandation de Véhicules</h1>", unsafe_allow_html=True)
st.write("""
                 <div style="text-align: justify;">
        Imaginez un système qui vous propose le véhicule idéal en quelques clics, parfaitement adapté à vos besoins ! 
         Dans un marché où la personnalisation des offres joue un rôle de plus en plus important dans les ventes de véhicules, 
         l'intelligence artificielle se révèle être un outil essentiel. Ce projet a pour objectif de créer une solution capable 
         de recommander un véhicule en fonction des caractéristiques personnelles de chaque client, telles que l'âge, le sexe,
          la capacité d'endettement et la situation familiale, afin de faciliter la prise de décision.
                   </div>
""", unsafe_allow_html=True)



# Onglets principaux
tabs = st.tabs(["Accueil", "Recommandation"])

# Accueil
with tabs[0]:
    st.markdown("<h1 style='text-align: center;'>Bienvenue sur l'application de Recommandation de Véhicules</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.write("""### 🌟 Pourquoi utiliser cette application ?""")
        st.write("""
                 <div style="text-align: justify;">
            Trouver un véhicule adapté peut être complexe. Cette application simplifie le processus en utilisant des modèles avancés de machine learning pour analyser vos préférences et fournir des recommandations précises.
        </div>
        """, unsafe_allow_html=True)

        st.write("""### 🔍 Comment fonctionne-t-elle ?""")
        st.write("""
            - 🖋️ **Saisie des informations** : Entrez votre âge, situation familiale, capacité d'endettement, etc.
            - 🧠 **Analyse des données** : Le modèle compare vos données à celles de notre base.
            - ✅ **Recommandation personnalisée** : Vous recevez les détails du véhicule qui correspond le mieux à vos besoins.
        """)

        st.write("""### 💡 Avantages de l'application :""")
        st.write("""
            - 🎯 **Personnalisation** : Chaque recommandation est adaptée à votre profil unique.
            - 🖥️ **Facilité d'utilisation** : Une interface claire et simple pour une navigation agréable.
            - 📊 **Précision** : S'appuie sur des algorithmes performants pour garantir des résultats fiables.
        """)

        st.write("""### 📚 En savoir plus :""")
        st.write("""
                 <div style="text-align: justify;">
            Explorez les fonctionnalités et découvrez comment cette application peut vous aider à faire un choix éclairé. Notre mission est de proposer des solutions innovantes et basées sur les données pour répondre à vos attentes.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("sidebar_texte.jpg", use_column_width=True) 
    
# Recommandation
with tabs[1]:
    st.markdown("<h1 style='text-align: center;'>Recommandation de Véhicule</h1>", unsafe_allow_html=True)
    st.write("""
                 <div style="text-align: justify;">
        Entrez vos informations personnelles pour découvrir le véhicule qui répond le mieux à vos besoins.
    </div>
        """, unsafe_allow_html=True)

    # Entrées utilisateur
    age = st.slider("🔢 Âge", 18, 80, 30)
    sexe = st.selectbox("👤 Sexe", options=["Homme", "Femme"])
    taux = st.number_input("💶 Capacité d'endettement (en euros)", min_value=500, max_value=100000, step=500)
    situationFamiliale = st.selectbox("👨‍👩‍👧‍👦 Situation Familiale", options=["célibataire", "en couple", "divorcé(e)", "seul(e)"])
    nbEnfantsAcharge = st.slider("👶 Nombre d'enfants à charge", 0, 4, 0)
    deuxieme_voiture = st.selectbox("🚘 Possédez-vous déjà une voiture ?", options=["non", "oui"])

    # Encodage des entrées
    sexe_encoded = 1 if sexe == "m" else 0
    situation_encoded = {"célibataire": 0, "en couple": 1, "divorcé(e)": 2, "seul(e)": 3}[situationFamiliale]
    deuxieme_voiture_encoded = 1 if deuxieme_voiture == "oui" else 0

    # Préparation des données
    user_data = pd.DataFrame({
        'age': [age],
        'sexe': [sexe_encoded],
        'taux': [taux],
        'situationFamiliale': [situation_encoded],
        'nbEnfantsAcharge': [nbEnfantsAcharge],
        '2eme voiture': [deuxieme_voiture_encoded]
    })
    
    # Standardisation
    user_data_scaled = scaler.transform(user_data)

    # Prédiction
    predicted_cluster = rf_model.predict(user_data_scaled)[0]
    predicted_details = cluster_to_details[predicted_cluster]

    # Résultats avec message personnalisé
    st.subheader("🎯 Votre Recommandation")

    # Catégorie recommandée avec une section dédiée
    st.markdown(f"""
        ## 🏷️ **Catégorie Recommandée** : <span style="color:#ff4b4b;">{predicted_details['categorie']}</span> 🚘
        _Cette catégorie est idéale pour vous car elle répond à vos besoins en matière de confort, performance et utilisation quotidienne._
    """, unsafe_allow_html=True)

    # Description de la catégorie
    st.write(f"### 📄 **Description de la catégorie** :")
    st.markdown(f"""
        - **Voiture {predicted_details['categorie']}** : {predicted_details['description']}
    """)

    # Informations détaillées du véhicule
    st.markdown(f"### 🚗 **Détails du véhicule recommandé** :")
    st.markdown(f"""
        - **Marque** : {predicted_details['marque']} 🚙
        - **Modèle** : {predicted_details['nom']} 🏎️
        - **Puissance** : {predicted_details['puissance']} chevaux 💪
        - **Longueur** : {predicted_details['longueur']} cm 📏
        - **Couleur** : {predicted_details['couleur']} 🎨
    """)

    # Affichage de l'image du véhicule
    st.image(f"{predicted_details['marque'].lower()}_image.png", caption=f"Modèle : {predicted_details['nom']} 🖼️", use_column_width=True)

    # Message de clôture avec invitation à poser des questions ou ajuster les préférences
    st.write(f"🔧 **Ajustez vos préférences** si nécessaire pour explorer d'autres options qui pourraient mieux correspondre à vos besoins.")

