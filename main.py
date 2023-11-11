import streamlit as st

from fakes import weather_df, mon_df, mal_df

import datetime

# TODO : add bg image

# remove footer and header
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.write('# PillowPulse')

st.write(
    'Want to go for an adventure now 🤠 !'
    ' Use _`PillowPulse`_ and go through our exciting tour packages in reasonable cost 🤩 !'
)

st.divider()

where = st.selectbox(
    "Destination ",
    help="Enter the name of the place you are headed .",
)

if where in ["Monaco"]:

    print(0)
    Gcol , Dcol = st.columns(2)

    with Gcol:

        st.metric(
            label = "🌡️ Temperature@Monaco",
            value=f"{weather_df.iloc[:, 0]['temperature']} °C",
            
        )
        st.metric(
            label= "🌧️ Humidity@Monaco",
            value=f"{weather_df.iloc[:, 0]['humidity']}"
        ) 
        st.metric(
            label = "💨 Wind Speed@Monaco",
            value=f"{weather_df.iloc[:, 0]['wind_speed']}",
            
        )
        st.metric(
            label = "☀️ UV Index@Monaco",
            value=f"{weather_df.iloc[:, 0]['UV_index']}",
            
        )

        st.write("### Booking Trends Over Time Comparison")

        st.area_chart(mon_df)
        
    with Dcol:
        st.write("## Accommodations")

        st.radio(
            "rooms",
            ("Villa @ 699$", "Penthouse @ 435$")
        )

        st.write("## Hightlights")

        st.write(
            '- Stay at a glamorous hotel overlooking the Monaco Grand Prix circuit \n',
            '- Exclusive access to a private yacht party \n',
            '- Explore the iconic Casino de Monte-Carlo \n',
            '- Gourmet dining experience at Michelin-starred restaurants \n',
            '- Helicopter tour of the French Riviera \n',
            "- Visit the Prince's Palace and Monaco Cathedral \n",
            '- Guided tour of the Oceanographic Museum \n'
        )

        st.write("## When")

        On = st.date_input('Deparature date ', datetime.date(2023, 12, 3))
        Time = st.time_input('Departure time', datetime.time(8, 45))

        
        
elif where in ["Maldives"]:
    print(1)

    Gcol , Dcol = st.columns(2)

    with Gcol:

        st.metric(
            label = "🌡️ Temperature@Maldives",
            value=f"{weather_df.iloc[:, 1]['temperature']} °C",
            
        )
        st.metric(
            label= "🌧️ Humidity@Maldives",
            value=f"{weather_df.iloc[:, 1]['humidity']}"
        ) 
        st.metric(
            label = "💨 Wind Speed@Maldives",
            value=f"{weather_df.iloc[:, 1]['wind_speed']}",
            
        )
        st.metric(
            label = "☀️ UV Index@Maldives",
            value=f"{weather_df.iloc[:, 1]['UV_index']}",
            
        )

        st.write("### Booking Trends Over Time Comparison")

        st.area_chart(mal_df)
        
    with Dcol:
        st.write("## Accommodations")

        st.radio(
            "rooms",
            ("Villa @ 699$", "Penthouse @ 435$")
        )

        st.write("## Hightlights")

        st.write(
            '- Stay at a luxurious overwater bungalow \n'
            '- Explore vibrant coral reefs with snorkeling and diving \n'
            '- Relax on pristine white-sand beaches \n'
            '- Dolphin watching excursion at sunset \n'
            '- Indulge in a romantic beachfront dinner \n'
            '- Guided tour of local islands and cultural experiences \n'
            '- Complimentary water sports activities \n'
        )

        st.write("## When")

        On = st.date_input('Deparature date ', datetime.date(2023, 12, 3))
        Time = st.time_input('Departure time', datetime.time(8, 45))

lets_go = st.button("Let's go 🚀 !",use_container_width=True)

