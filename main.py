import streamlit as st

from fakes import weather_df, mon_df, mal_df

import datetime

st.set_page_config(
    "PillowPulse"
)

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

st.write('# Welcome to PillowPulse! ')

st.write(
    'Want to go for an adventure now 🤠 !'
    ' Use _`PillowPulse`_ and go through our exciting tour packages in reasonable cost 🤩 !'
)

st.divider()

MD_LAST = """

Dear **Guest**,

Thank you for choosing PillowPulse for your upcoming stay! We are absolutely delighted to have you as our guest, and we're committed to making your time with us truly exceptional. 🌟

## Your Experience Awaits

At PillowPulse, we've curated an atmosphere of comfort and luxury to ensure your stay is unforgettable. From cozy rooms to top-notch amenities, your satisfaction is our priority.

## Personalized Service

Our dedicated team, including Arjun, Utham, and Adarsh, is here to cater to your every need. If there's anything you require or any special arrangements you'd like, please don't hesitate to let us know.

## Contact Information

- **Email:** [pillowpulsehotels@gmail.com](mailto:pillowpulsehotels@gmail.com)
- **Phone:** +91 89000 00089

## Safe Travels

As you prepare for your journey, we wish you safe travels! We eagerly anticipate your arrival and can't wait to welcome you personally.

Looking forward to creating beautiful moments for you at PillowPulse!

Warm regards,

**Arjun, Utham, Adarsh**

"""
def Form():
    where = st.selectbox(
    "Destination ",
    ("Monaco", "Maldives"),
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

            st.write("📍 Monte carlo resorts, HOTEL DE PARIS")

            rooms = st.radio(
                "rooms",
                ("Villa @ 699$", "Penthouse @ 435$")
            )

            if rooms in [
                "Villa @ 699$"
            ]:
                st.info(
                    "- High-speed internet and Wi-Fi\n"
                    "- Spa facilities, including a sauna and steam room\n"
                    "- Private garden\n"
                    "- Fully equipped kitchen\n"
                    "- 24/7 concierge services\n"
                    "- Private beach access\n"
                )
            if rooms in [
                "Penthouse @ 435$"
            ]:
                st.info(
                    "- High-speed internet and Wi-Fi \n"
                    "- Access to concierge service \n"
                    "- 24/7 security personnel \n"
                    "- Private elevator access \n"
                    "- Balcony with panoramic views \n"
                    "- Integrated smart home system \n"
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

            st.write("📍 Turtle gateway, Reef valley resorts ")

            rooms = st.radio(
                "rooms",
                ("Villa @ 699$", "Penthouse @ 435$")
            )
            if rooms in [
                "Villa @ 699$"
            ]:
                st.info(
                    "- High-speed internet and Wi-Fi\n"
                    "- Spa facilities, including a sauna and steam room\n"
                    "- Private garden\n"
                    "- Fully equipped kitchen\n"
                    "- 24/7 concierge services\n"
                    "- Private beach access\n"
                )
            if rooms in [
                "Penthouse @ 435$"
            ]:
                st.info(
                    "- High-speed internet and Wi-Fi \n"
                    "- Access to concierge service \n"
                    "- 24/7 security personnel \n"
                    "- Private elevator access \n"
                    "- Balcony with panoramic views \n"
                    "- Integrated smart home system \n"
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

if lets_go:

    # TODO : save them

    st.success(
        MD_LAST
    )

else:

    Form()
    
