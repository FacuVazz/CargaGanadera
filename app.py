import streamlit as st
from calculos import (
    calcular_ms_por_hectarea_dia,
    requerimiento_diario_animal,
    oferta_total_ms,
    requerimiento_total_animales,
    capacidad_maxima_animales,
    animales_por_hectarea,
    calcular_ug_por_animal,
    carga_ug_ha,
    carga_maxima_ug_ha
)
from datos_pasturas import pasturas

# Configuración de la página
st.set_page_config(page_title="Calculadora de Carga Ganadera", page_icon="🐄")

# Estilos CSS: fondo + recuadro + inputs transparentes
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1501794747964-082a0829c977?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        .main .block-container {
            background-color: rgba(0, 0, 0, 0.85);
            padding: 2rem;
            border-radius: 12px;
            color: white;
        }

        input, .stTextInput > div > div > input,
        .stNumberInput input,
        .stSelectbox div[data-baseweb="select"] {
            background-color: transparent !important;
            color: white !important;
            border: 1px solid white !important;
        }

        label, .stSelectbox label, .stNumberInput label {
            color: white !important;
        }

        .stButton > button {
            background-color: #222 !important;
            color: white !important;
            border-radius: 5px;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("🐄 Calculadora de Carga Ganadera")
st.markdown("Estimá cuántos animales puede sostener tu campo según el tipo de pastura y los recursos disponibles.")

# FORMULARIO

st.subheader("📥 Ingresá los datos de tu establecimiento")

# Opciones de pasturas legibles
pastura_display = {
    "Alfalfa": "alfalfa",
    "Pasto Llorón": "pasto_lloron",
    "Rye Grass": "rye_grass",
    "Maíz Ensilado": "maiz_ensilado",
    "Campo Natural": "campo_natural",
    "Sorgo": "sorgo"
}
opciones_display = ["Elige el tipo de pastura.."] + list(pastura_display.keys())
tipo_pastura_display = st.selectbox("Tipo de pastura", opciones_display)
tipo_pastura = pastura_display.get(tipo_pastura_display, None)

# Inputs (sólo peso con decimales)
peso_vivo = st.number_input("Peso promedio del animal (kg)", min_value=0.0, value=0.0, step=0.01)
cantidad_animales = st.number_input("Cantidad actual de animales", min_value=0, value=0, step=1)
superficie_ha = st.number_input("Superficie disponible (hectáreas)", min_value=0, value=0, step=1)
dias = st.number_input("Días de permanencia en el campo", min_value=0, value=0, step=1)

# Validación antes de permitir cálculo
if tipo_pastura and peso_vivo > 0 and cantidad_animales > 0 and superficie_ha > 0 and dias > 0:

    if st.button("Calcular capacidad ganadera"):
        # CÁLCULOS
        produccion_ms_ha_dia = calcular_ms_por_hectarea_dia(tipo_pastura, pasturas)
        requerimiento_diario = requerimiento_diario_animal(peso_vivo)
        oferta_total = oferta_total_ms(superficie_ha, produccion_ms_ha_dia, dias)
        requerimiento_total = requerimiento_total_animales(cantidad_animales, requerimiento_diario, dias)
        capacidad_maxima = capacidad_maxima_animales(oferta_total, requerimiento_diario, dias)

        # Carga ganadera
        animales_ha_dia = animales_por_hectarea(produccion_ms_ha_dia, requerimiento_diario)
        animales_ha_totales = animales_ha_dia / dias
        ug_por_animal = calcular_ug_por_animal(peso_vivo)
        carga_actual_ug_ha = carga_ug_ha(cantidad_animales, ug_por_animal, superficie_ha)
        carga_maxima_ug_ha_valor = carga_maxima_ug_ha(capacidad_maxima, ug_por_animal, superficie_ha)

        # RESULTADOS
        st.subheader("📊 Resultados del cálculo")
        st.write(f"**Producción diaria de materia seca por hectárea:** {produccion_ms_ha_dia:.2f} kg")
        st.write(f"**Requerimiento diario de cada animal:** {requerimiento_diario:.2f} kg de materia seca")
        st.write(f"**Oferta total de forraje disponible:** {oferta_total:,.2f} kg")
        st.write(f"**Requerimiento total de los animales actuales:** {requerimiento_total:,.2f} kg")
        st.write(f"**Capacidad máxima del campo:** {int(capacidad_maxima)} animales durante {dias} días")

        st.subheader("📐 Indicadores de carga ganadera")
        st.write(f"**Cantidad estimada de animales que se pueden mantener por hectárea:** {animales_ha_totales:.2f}")
        st.write(f"**Equivalencia de cada animal en unidades ganaderas (UG):** {ug_por_animal:.2f}")
        st.write(f"**Carga ganadera actual:** {carga_actual_ug_ha:.2f} UG/ha")
        st.write(f"**Carga ganadera máxima recomendada:** {carga_maxima_ug_ha_valor:.2f} UG/ha")

        st.markdown("---")
        st.success(f"✅ Podés mantener hasta **{int(capacidad_maxima)} animales** durante {dias} días sin sobrepastorear.")

else:
    st.warning("⚠️ Completá todos los campos antes de realizar el cálculo.")

# Botón para limpiar el formulario
if st.button("Limpiar formulario"):
    st.rerun()
