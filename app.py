import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Управление школьной теплицей", page_icon="🌱")

st.title("🌱 Управление школьной теплицей")
st.write("Учебный кейс: определение необходимости полива с учетом типа растения и данных датчиков (200 измерений).")

# Загрузка обученной модели
@st.cache_resource
def load_model():
    with open("greenhouse_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Боковая панель для ввода параметров
st.sidebar.header("Параметры датчиков теплицы")

plant_type = st.sidebar.selectbox(
    "Вид растения",
    ["Томаты", "Огурцы", "Зелень"]
)

temperature = st.sidebar.slider("Температура (°C)", 10.0, 40.0, 25.0)
air_humidity = st.sidebar.slider("Влажность воздуха (%)", 20.0, 100.0, 50.0)
soil_moisture = st.sidebar.slider("Влажность почвы (%)", 10.0, 90.0, 30.0)

# Подготовка данных для модели
plant_Зелень = 1 if plant_type == "Зелень" else 0
plant_Огурцы = 1 if plant_type == "Огурцы" else 0
plant_Томаты = 1 if plant_type == "Томаты" else 0

input_data = pd.DataFrame([{
    'temperature_c': temperature,
    'air_humidity_pct': air_humidity,
    'soil_moisture_pct': soil_moisture,
    'plant_type_Зелень': plant_Зелень,
    'plant_type_Огурцы': plant_Огурцы,
    'plant_type_Томаты': plant_Томаты
}])

if st.button("Сделать прогноз"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error(f"⚠️ **Требуется полив!** (Для культуры '{plant_type}' текущие условия требуют увлажнения почвы)")
    else:
        st.success(f"✅ **Полив не требуется.** (Для культуры '{plant_type}' показатели в норме)")

st.caption("Проект выполнен в рамках STEM-образования магистрантов.")
