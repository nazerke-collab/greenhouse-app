import streamlit as st
import pandas as pd
import joblib

# Загружаем обученную модель
model = joblib.load('greenhouse_model.pkl')

st.title("🌱 Управление школьной теплицей")
st.write("Учебный кейс: определение необходимости полива на основе данных датчиков[cite: 1].")

# Панель управления с ползунками датчиков
st.sidebar.header("Параметры датчиков теплицы")
temp = st.sidebar.slider("Температура (°C)", 10.0, 40.0, 25.0)
air_hum = st.sidebar.slider("Влажность воздуха (%)", 10.0, 100.0, 50.0)
soil_hum = st.sidebar.slider("Влажность почвы (%)", 0.0, 100.0, 30.0)

# Кнопка для получения прогноза
if st.button("Сделать прогноз"):
    # Передаем данные в модель в том же формате, что и при обучении
    input_data = pd.DataFrame([[temp, air_hum, soil_hum]], 
                              columns=['temperature_c', 'air_humidity_pct', 'soil_moisture_pct'])
    
    prediction = model.predict(input_data)[0]
    
    st.subheader("Результат:")
    if prediction == 1:
        st.error("⚠️ **Суару қажет / Требуется полив!** Влажность почвы низкая.")
    else:
        st.success("✅ **Суару қажет емес / Полив не требуется.** Условия в норме.")

st.markdown("---")
st.caption("Проект выполнен в рамках STEM-образования магистрантов[cite: 1].")