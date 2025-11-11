import streamlit as st
import pandas as pd
from setup import Setup
from setup_manager import SetupManager

# ---------- CONFIGURATION PAGE ----------
st.set_page_config(
    page_title="Setup Manager Formula Student",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- STYLE APPLE ----------
st.markdown("""
<style>
.big-title {
    font-size: 36px;
    font-weight: 600;
    color: #1c1c1e;
    text-align: center;
    font-family: -apple-system, BlinkMacSystemFont, "San Francisco", "Helvetica Neue", sans-serif;
    margin-top: -40px;
}
.subtitle {
    color: #86868b;
    text-align: center;
    margin-bottom: 40px;
}
.card {
    background-color: #f9f9fb;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
    margin-bottom: 30px;
}
button:focus, select:focus, input:focus {
    outline: none !important;
    box-shadow: none !important;
}
html, body, [class*="block-container"] {
    scroll-behavior: smooth;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🏎️ Setup Manager Formula Student</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Gérez vos réglages châssis avec élégance</p>', unsafe_allow_html=True)

# ---------- INITIALISATION ----------
manager = SetupManager()
try:
    manager.lecture_fichier("setups.csv")
except FileNotFoundError:
    pass

# ---------- FORMULAIRE AJOUT ----------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("➕ Ajouter un nouveau setup")

    with st.form("Ajouter Setup"):
        col1, col2 = st.columns(2)

        # Colonnes principales
        with col1:
            nom = st.text_input("Nom du setup")
            hauteur = st.number_input("Hauteur caisse (mm)", value=120.0)
            camber = st.number_input("Camber (°)", value=-2.0)
            caster = st.number_input("Caster (°)", value=5.0)
            pression = st.number_input("Pression pneus (bar)", value=1.8)

        with col2:
            aero = st.number_input("Aéro (N)", value=200.0)
            poids = st.number_input("Poids (kg)", value=250.0)
            epreuve = st.text_input("Épreuve")
            terrain = st.selectbox("Type de terrain", ["Lisse", "Accidenté", "Mixte"])
            tarmac = st.selectbox("Type de tarmac", ["Asphalte", "Béton"])
            meteo = st.selectbox("Météo", ["Sec", "Pluie", "Humide"])

        # Expander pour réglages avancés
        with st.expander("⚙️ Réglages avancés"):
            col3, col4 = st.columns(2)
            with col3:
                barre_av = st.number_input("Barre anti-roulis AV", value=30.0)
                bv_comp = st.number_input("BV compression", value=5.0)
                bv_det = st.number_input("BV détente", value=7.0)
                ressort_av = st.number_input("Ressort AV (N/mm)", value=400.0)
            with col4:
                barre_ar = st.number_input("Barre anti-roulis AR", value=25.0)
                hv_comp = st.number_input("HV compression", value=6.0)
                hv_det = st.number_input("HV détente", value=8.0)
                ressort_ar = st.number_input("Ressort AR (N/mm)", value=350.0)
                ackerman = st.number_input("Ackerman (%)", value=50.0)

        submitted = st.form_submit_button("✅ Ajouter le setup")
        if submitted:
            s = Setup(
                nom, hauteur, camber, caster, pression, aero, poids,
                barre_av, barre_ar, ackerman,
                bv_comp, bv_det, hv_comp, hv_det,
                ressort_av, ressort_ar,
                epreuve, terrain, tarmac, meteo
            )
            manager.ajouter_setup(s)
            manager.sauvegarde_fichier("setups.csv")
            st.success(f"Setup '{nom}' ajouté avec succès ✅")
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- LISTE DES SETUPS ----------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 Liste des setups enregistrés")

    if manager.setups:
        data = [vars(s) for s in manager.setups]
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

        noms_setups = [elt.nom for elt in manager.setups]

        # Suppression
        choix_suppr = st.selectbox("🗑️ Sélectionner un setup à supprimer :", noms_setups)
        if st.button("Supprimer le setup sélectionné"):
            for elt in manager.setups:
                if elt.nom == choix_suppr:
                    manager.supprimer_setup(choix_suppr)
                    manager.sauvegarde_fichier("setups.csv")
                    st.success(f"Setup '{choix_suppr}' supprimé ✅")
                    st.rerun()

    # Modification
    choix_modif = st.selectbox("✏️ Sélectionner un setup à modifier :", noms_setups)
    setup_a_modif = next((s for s in manager.setups if s.nom == choix_modif), None)

    if setup_a_modif:
        with st.expander(f"Modifier le setup '{choix_modif}'"):
            with st.form(f"modifier_{choix_modif}"):
                col1, col2 = st.columns(2)

                # Colonnes principales
                with col1:
                    nom = st.text_input("Nom du setup", value=setup_a_modif.nom)
                    hauteur = st.number_input("Hauteur caisse (mm)", value=float(getattr(setup_a_modif, "hauteur_caisse", 120.0)))
                    camber = st.number_input("Camber (°)", value=float(getattr(setup_a_modif, "camber", -2.0)))
                    caster = st.number_input("Caster (°)", value=float(getattr(setup_a_modif, "caster", 5.0)))
                    pression = st.number_input("Pression pneus (bar)", value=float(getattr(setup_a_modif, "pression_pneus", 1.8)))

                with col2:
                    aero = st.number_input("Aéro (N)", value=float(getattr(setup_a_modif, "aero", 200.0)))
                    poids = st.number_input("Poids (kg)", value=float(getattr(setup_a_modif, "poids", 250.0)))
                    epreuve = st.text_input("Épreuve", value=getattr(setup_a_modif, "epreuve", ""))
                    terrain = st.selectbox(
                        "Type de terrain", ["Lisse", "Accidenté", "Mixte"],
                        index=["Lisse", "Accidenté", "Mixte"].index(getattr(setup_a_modif, "terrain", "Lisse"))
                    )
                    tarmac = st.selectbox(
                        "Type de tarmac", ["Asphalte", "Béton"],
                        index=["Asphalte", "Béton"].index(getattr(setup_a_modif, "tarmac", "Asphalte"))
                    )
                    meteo = st.selectbox(
                        "Météo", ["Sec", "Pluie", "Humide"],
                        index=["Sec", "Pluie", "Humide"].index(getattr(setup_a_modif, "meteo", "Sec"))
                    )

                # Réglages avancés
                with st.expander("⚙️ Réglages avancés"):
                    col3, col4 = st.columns(2)
                    with col3:
                        barre_av = st.number_input("Barre anti-roulis AV", value=float(getattr(setup_a_modif, "barre_antiroulis_av", 30.0)))
                        bv_comp = st.number_input("BV compression", value=float(getattr(setup_a_modif, "bv_compression_av", 5.0)))
                        bv_det = st.number_input("BV détente", value=float(getattr(setup_a_modif, "bv_detente_av", 7.0)))
                        ressort_av = st.number_input("Ressort AV (N/mm)", value=float(getattr(setup_a_modif, "ressort_av", 400.0)))
                    with col4:
                        barre_ar = st.number_input("Barre anti-roulis AR", value=float(getattr(setup_a_modif, "barre_antiroulis_ar", 25.0)))
                        hv_comp = st.number_input("HV compression", value=float(getattr(setup_a_modif, "hv_compression_av", 6.0)))
                        hv_det = st.number_input("HV détente", value=float(getattr(setup_a_modif, "hv_detente_av", 8.0)))
                        ressort_ar = st.number_input("Ressort AR (N/mm)", value=float(getattr(setup_a_modif, "ressort_ar", 350.0)))
                        ackerman = st.number_input("Ackerman (%)", value=float(getattr(setup_a_modif, "ackerman", 50.0)))

                submitted_modif = st.form_submit_button("💾 Enregistrer les modifications")
                if submitted_modif:
                    dico_modif = {
                        "nom": nom,
                        "hauteur_caisse": hauteur,
                        "camber": camber,
                        "caster": caster,
                        "pression_pneus": pression,
                        "aero": aero,
                        "poids": poids,
                        "barre_antiroulis_av": barre_av,
                        "barre_antiroulis_ar": barre_ar,
                        "ackerman": ackerman,
                        "bv_compression_av": bv_comp,
                        "bv_detente_av": bv_det,
                        "hv_compression_av": hv_comp,
                        "hv_detente_av": hv_det,
                        "ressort_av": ressort_av,
                        "ressort_ar": ressort_ar,
                        "epreuve": epreuve,
                        "terrain": terrain,
                        "tarmac": tarmac,
                        "meteo": meteo
                    }
                    manager.modifier_setup(choix_modif, dico_modif)
                    manager.sauvegarde_fichier("setups.csv")
                    st.success(f"Setup '{choix_modif}' modifié avec succès ✅")
                    st.rerun()
    else:
        st.info("Aucun setup disponible.")

    st.markdown('</div>', unsafe_allow_html=True)