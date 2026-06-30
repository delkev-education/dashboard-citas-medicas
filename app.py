import streamlit as st
import pandas as pd
import plotly.express as px

# Leer datos
df = pd.read_csv("citas_medicas.csv")

st.title("Dashboard de Gestión de Citas Médicas")

# -------------------------
# Citas por Especialidad
# -------------------------
st.subheader("Citas por Especialidad")

especialidades = df["especialidad"].value_counts().reset_index()
especialidades.columns = ["Especialidad", "Cantidad"]

fig1 = px.bar(
    especialidades,
    x="Especialidad",
    y="Cantidad",
    color="Especialidad"
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------
# Estado de las citas
# -------------------------
st.subheader("Estado de las Citas")

fig2 = px.pie(
    df,
    names="estado"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Citas por mes
# -------------------------
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month

citas_mes = df.groupby("mes").size().reset_index(name="cantidad")

st.subheader("Citas por Mes")

fig3 = px.line(
    citas_mes,
    x="mes",
    y="cantidad",
    markers=True
)

st.plotly_chart(fig3, use_container_width=True)
