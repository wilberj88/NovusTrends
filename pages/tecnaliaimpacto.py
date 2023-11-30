import streamlit as st
from streamlit_extras.let_it_rain import rain 
from streamlit_echarts import st_echarts
import plotly.graph_objects as go
import folium
import time
from datetime import datetime
import pandas as pd
import plotly.express as px
import numpy as np
from PIL import Image
from streamlit_extras.colored_header import colored_header
from streamlit_extras.grid import grid
import requests
import urllib, json

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Tecnalia&NovusDemo", page_icon="🧠")

with st.sidebar:
    st.write('Prototipo Monitor de Impacto')
st.header("Mando de Impacto en Tiempo Real")
a = st.selectbox("Choose a Module", ("Económico", "Social", "Ambiental", "Beneficiarios"), index=None, placeholder="Choose an option")

if a == "Económico":
    st.title('Impactos Económicos 💰')

    current_time = time.ctime()
    st.write("A día de hoy a las: ", current_time)
    
    colored_header(
        label="Desempeño Histórico Pymes de la Región",
        description="Promedio últimos 25 años",
        color_name="violet-70",
    )
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Supervivencia", "75%", "20%")
    col2.metric("Empleos Directos", "80%", "-8%")
    col3.metric("Empleos Indirectos", "125%", "25%")
    col4.metric("Tributación", "15%", "3%")
    
    meta_zona_1 = 10290
    meta_zona_2 = 11986
    meta_zona_3 = 11368
    meta_zona_4 = 14018
    meta_zona_5 = 14036
    meta_zona_6 = 5241
    meta_zona_7 = 3112
    meta_zona_8 = 110
    meta_zona_9 = 7338
    
    col5, col6, col7 = st.columns(3)
    with col5:
        
        meta = 35000
        st.subheader("Supervivencia Vs Promedio")
        option = {
        "xAxis": {
            "type": "category",
            "data": ["Hora_1", "Hora_2", "Hora_3", "Hora_4", "Hora_5", "Hora_6", "Hora_7"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": [meta*0.1, meta*0.2, meta*0.35, meta*0.5, meta*0.75, meta*0.9, meta], "type": "line"},
            {"data": [meta*0.15, meta*0.25, meta*0.4, meta*0.55, meta*0.75, meta*0.9, meta], "type": "line"},
        ],
        }
        st_echarts(
            options=option, height="625px",
        )
    with col6:
        
        st.subheader("Empleos")
        acelerometro2 = {
            "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
            "series": [
                {
                    "name": "Pressure",
                    "type": "gauge",
                    "axisLine": {
                        "lineStyle": {
                            "width": 10,
                        },
                    },
                    "progress": {"show": "true", "width": 10},
                    "detail": {"valueAnimation": "true", "formatter": "{value}"},
                    "data": [{"value": 50, "name": "Directos"}],
                }
            ],
        }
        st_echarts(options=acelerometro2)
        acelerometro1 = {
            "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
            "series": [
                {
                    "name": "Pressure",
                    "type": "gauge",
                    "axisLine": {
                        "lineStyle": {
                            "width": 10,
                        },
                    },
                    "progress": {"show": "true", "width": 10},
                    "detail": {"valueAnimation": "true", "formatter": "{value}"},
                    "data": [{"value": 30, "name": "Indirectos"}],
                }
            ],
        }
    
        st_echarts(options=acelerometro1)
         
    with col7:
        st.subheader("Tributación Sectorial")
        options = {
                "title": {"text": "🧱"},
                "tooltip": {
                    "trigger": "axis",
                    "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
                },
                "legend": {"data": ["Agro", "Manufacturas", "Industrial", "Servicios", "Tech"]},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "xAxis": [
                    {
                        "type": "category",
                        "boundaryGap": False,
                        "data": ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "23:59"],
                    }
                ],
                "yAxis": [{"type": "value"}],
                "series": [
                    {
                        "name": "Agro",
                        "type": "line",
                        "stack": "总量",
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
                        "data": [meta_zona_5*0.1, meta_zona_5*0.2, meta_zona_5*0.35, meta_zona_5*0.45, meta_zona_5*0.5, meta_zona_5*0.75, meta_zona_5],
                    },
                      {
                        "name": "Manufacturas",
                        "type": "line",
                        "stack": "总量",
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
                        "data": [meta_zona_4*0.1, meta_zona_4*0.2, meta_zona_4*0.35, meta_zona_4*0.45, meta_zona_4*0.5, meta_zona_4*0.75, meta_zona_4],
                    },
                      {
                        "name": "Industrial",
                        "type": "line",
                        "stack": "总量",
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
                        "data": [meta_zona_3*0.1, meta_zona_3*0.2, meta_zona_3*0.35, meta_zona_3*0.45, meta_zona_3*0.5, meta_zona_3*0.75, meta_zona_3],
                    },
                      {
                        "name": "Servicios",
                        "type": "line",
                        "stack": "总量",
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
                        "data": [meta_zona_2*0.1, meta_zona_2*0.2, meta_zona_2*0.35, meta_zona_2*0.45, meta_zona_2*0.5, meta_zona_2*0.75, meta_zona_2],
                    },
                      {
                        "name": "Tech",
                        "type": "line",
                        "stack": "总量",
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
                        "data": [meta_zona_1*0.1, meta_zona_1*0.2, meta_zona_1*0.35, meta_zona_1*0.45, meta_zona_1*0.5, meta_zona_1*0.75, meta_zona_1],
                    },
                ],
            }
        st_echarts(options=options, height="600px")

    
if a == "Social":
    st.title('Impactos Sociales 👨‍👨‍👦‍')
    current_time = time.ctime()
    st.write("A día de hoy a las: ", current_time)
    col4, col5 = st.columns(2)
    with col4:
        fig1 = go.Figure(data=[go.Sankey(
          node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = ["Indicador 1", "Indicador 2", "Indicador 3", "Categoría 1", "Categoría 2", "Puntaje Iris+"],
            color = "blue"
          ),
          link = dict(
            source = [0, 1, 2, 3, 4], # indices correspond to labels, eg A1, A2, A1, B1, ...
            target = [3, 4, 3, 5, 5],
            value = [8, 4, 5, 13, 4]
        ))])
      
        fig1.update_layout(title_text="Históricos Metodología IRIS+", font_size=10)
        st.plotly_chart(fig1, theme="streamlit")
    
    with col5:
        fig1 = go.Figure(data=[go.Sankey(
          node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = ["16 ODS", "Sociales", "Ambientales", "Económicos", "Vivienda", "Estudio", "Alimentación", "Transporte", "Entretenimiento", "Viajes", "Acciones", "Activos", "Criptomonedas", "Bonos"],
            color = "red"
          ),
          link = dict(
            source = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
            target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            value = [44, 44, 44, 10, 20, 10, 22, 22, 10, 14, 10, 10, 10]
        ))])
      
        fig1.update_layout(title_text="Por Objetivos de Desarrollo Sostenible (ODS)", font_size=10)
        st.plotly_chart(fig1, theme="streamlit")
    
    col6, col7 = st.columns(2)
    with col6:
        option = {
            "title": {"text": "Eficacia", "subtext": "Porcentaje Conversión(%)"},
            "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c}%"},
            "toolbox": {
                "feature": {
                    "dataView": {"readOnly": False},
                    "restore": {},
                    "saveAsImage": {},
                }
            },
            "legend": {"data": ["Contactados", "Interesados", "Persuadidos", "Comprometidos", "Beneficiarios"]},
            "series": [
                {
                    "name": "Contactados",
                    "type": "funnel",
                    "left": "10%",
                    "width": "80%",
                    "label": {"formatter": "{b}%"},
                    "labelLine": {"show": False},
                    "itemStyle": {"opacity": 0.7},
                    "emphasis": {
                        "label": {"position": "inside", "formatter": "{b}预期: {c}%"}
                    },
                    "data": [
                        {"value": 60, "name": "Persuadidos"},
                        {"value": 40, "name": "Comprometidos"},
                        {"value": 20, "name": "Beneficiarios"},
                        {"value": 80, "name": "Interesados"},
                        {"value": 100, "name": "Contactados"},
                    ],
                },
                {
                    "name": "Margen",
                    "type": "funnel",
                    "left": "10%",
                    "width": "80%",
                    "maxSize": "80%",
                    "label": {"position": "inside", "formatter": "{c}%", "color": "#fff"},
                    "itemStyle": {"opacity": 0.5, "borderColor": "#fff", "borderWidth": 2},
                    "emphasis": {
                        "label": {"position": "inside", "formatter": "{b}实际: {c}%"}
                    },
                    "data": [
                        {"value": 30, "name": "Persuadidos"},
                        {"value": 10, "name": "Comprometidos"},
                        {"value": 5, "name": "Beneficiarios"},
                        {"value": 50, "name": "Interesados"},
                        {"value": 80, "name": "Contactados"},
                    ],
                    "z": 100,
                },
            ],
        }
        st_echarts(option, height="500px")    
    
    with col7:
        option = {
            "legend": {},
            "tooltip": {"trigger": "axis", "showContent": False},
            "dataset": {
                "source": [
                    ["product", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
                    ["Sociales", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                    ["Ambientales", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                    ["Económicos", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                    ["Institucionales", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "25%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@2012} ({d}%)"},
                    "encode": {"itemName": "product", "value": "Junio", "tooltip": "Junio"},
                },
            ],
        }
        st_echarts(option, height="500px", key="echarts")
    
    
    






if a == "Ambiental":
    st.title('Impactos Ambientales 🌳')
    current_time = time.ctime()
    st.write("A día de hoy a las: ", current_time)
    st.subheader('Impacto en Emisiones ☣️')
    colx, coly = st.columns(2)
    with colx:
        def render_basic_radar():
            option = {
                    "title": {"text": "Transición energética"},
                    "legend": {"data": ["Histórico", "Beneficiarios"]},
                    "radar": {
                        "indicator": [
                            {"name": "Carbón", "max": 6500},
                            {"name": "Agua", "max": 16000},
                            {"name": "Viento", "max": 30000},
                            {"name": "Sol", "max": 38000},
                            {"name": "Petróleo", "max": 52000},
                            {"name": "Gas", "max": 25000},
                        ]
                    },
                    "series": [
                        {
                            "name": "Histórico Vs Beneficiarios",
                            "type": "radar",
                            "data": [
                                {
                                    "value": [6000, 10000, 20000, 3500, 15000, 11800],
                                    "name": "Histórico",
                                },
                                {
                                    "value": [3500, 15000, 25000, 10800, 22000, 20000],
                                    "name": "Beneficiarios",
                                },
                            ],
                        }
                    ],
                }
            st_echarts(option, height="500px")
        render_basic_radar()
    with coly:
        df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Plotly_Graphs/Radar-chart/ExistingHotels_CustomerVisitsdata-1554810038262.csv")
        df = df[df['Hotelid'].isin(['hotel_101','hotel_102','hotel_103'])]
        print(df.iloc[:20, :8])
    
        df = df.groupby('Hotelid')[['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                        'Rooms_rating','Checkin_rating',
                                        'Businessservice_rating']].mean().reset_index()
        print(df)
    
    # Convert from wide data to long data to plot radar chart
        df = pd.melt(df, id_vars=['Hotelid'], var_name='category', value_name='rating',
                         value_vars=['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                     'Rooms_rating','Checkin_rating','Businessservice_rating'],
            )
        print(df)
    
    # radar chart Plotly examples - https://plotly.com/python/radar-chart/
    # radar chart Plotly docs = https://plotly.com/python-api-reference/generated/plotly.express.line_polar.html#plotly.express.line_polar
        fig = px.line_polar(df, r='rating', theta='category', color='Hotelid', line_close=True,
                                        line_shape='linear',  # or spline
                                hover_name='Hotelid',
                                hover_data={'Hotelid':False},
                                markers=True,
                                # labels={'rating':'stars'},
                                # text='Hotelid',
                                # range_r=[0,10],
                                direction='clockwise',  # or counterclockwise
                                start_angle=45
                                )
            # fig.update_traces(fill='toself')
        fig.show()
        
    
       
        url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
    
        # override gray link colors with 'source' colors
        opacity = 0.4
        # change 'magenta' to its 'rgba' value to add opacity
        data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
        data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                            for src in data['data'][0]['link']['source']]
    
        fig = go.Figure(data=[go.Sankey(
            valueformat = ".0f",
            valuesuffix = "TWh",
            # Define nodes
            node = dict(
              pad = 15,
              thickness = 15,
              line = dict(color = "black", width = 0.5),
              label =  data['data'][0]['node']['label'],
              color =  data['data'][0]['node']['color']
            ),
            # Add links
            link = dict(
              source =  data['data'][0]['link']['source'],
              target =  data['data'][0]['link']['target'],
              value =  data['data'][0]['link']['value'],
              label =  data['data'][0]['link']['label'],
              color =  data['data'][0]['link']['color']
        ))])
    
        fig.update_layout(title_text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
                          font_size=10)
    
        st.plotly_chart(fig, theme="streamlit")
    st.subheader('Oportunidades Climáticas 🌤️')
    def obtener_datos_ciudad(ciudad):
        URL = BASE_URL + f"q={ciudad}&appid={API_KEY}"
        response = requests.get(URL)
    
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather'][0]['description']
            return temperature, humidity, pressure, report
        else:
            return None

    def mostrar_informacion_ciudad(region, ciudades):
        col = st.columns(len(ciudades))
    
        for i, ciudad in enumerate(ciudades):
            with col[i]:
                st.write(f"🌧 {region} ☀️")
                st.write(f"{ciudad:-^30}")
                datos_ciudad = obtener_datos_ciudad(ciudad)
                
                if datos_ciudad:
                    temperature, humidity, pressure, report = datos_ciudad
                    st.write(f"Temperature (Kelvins): {temperature}")
                    st.write(f"Humidity: {humidity}")
                    st.write(f"Pressure: {pressure}")
                    st.write(f"Weather Report: {report}")
                else:
                    st.write(f"Error obteniendo datos para {ciudad}")
    
    # Constantes
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "146090ad17fa8843bc9eca97c53926b4"
    
    # Ciudades por región
    ciudades_usa = ["New York", "Bogota"]
    ciudades_europa = ["Toledo", "London"]
    ciudades_asia = ["Pekin", "Bombai"]
    
    # Mostrar información para cada región
    mostrar_informacion_ciudad("USA", ciudades_usa)
    mostrar_informacion_ciudad("Europe", ciudades_europa)
    mostrar_informacion_ciudad("Asia", ciudades_asia)



if a == "Beneficiarios":
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

    clubes = df_data["Club"].value_counts().index
    club = st.sidebar.selectbox("Club", clubes)
    
    df_players = df_data[df_data["Club"] == club]
    players = df_players["Name"].value_counts().index
    player = st.sidebar.selectbox("Jugador", players)
    
    player_stats = df_data[df_data["Name"] == player].iloc[0]
    
    st.image(player_stats["Photo"])
    st.title(f"{player_stats['Name']}")
    
    st.markdown(f"**Equipo:** {player_stats['Club']}")
    st.markdown(f"**Rol:** {player_stats['Position']}")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown(f"**Edad:** {player_stats['Age']}")
    col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}")
    col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
    
    st.divider()
    st.subheader(f"Overal {player_stats['Overall']}")
    st.progress(int(player_stats['Overall']))
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
    col2.metric(label="Salario mensual", value=f"£ {player_stats['Wage(£)']:,}")
    col3.metric(label="Cláusula de recisión", value=f"£ {player_stats['Release Clause(£)']:,}")
    
