import streamlit as st

# Sample data
ships_data = {
    "TORM A": {
        "IMO": "1234567",
        "MMSI": "234567890",
        "Type": "Crude Oil Tanker",
        "Speed": "12 knots",
        "Route": "Port A to Port B",
        "Crew": 20
    },
    "TORM B": {
        "IMO": "7654321",
        "MMSI": "098765432",
        "Type": "Product Tanker",
        "Speed": "15 knots",
        "Route": "Port C to Port D",
        "Crew": 25
    }
}

st.title("TORM Shipping Company - Ship Tracking")

# Sidebar for ship selection
ship_name = st.sidebar.selectbox("Select Ship", list(ships_data.keys()))

# Display ship details
if ship_name:
    ship_info = ships_data[ship_name]
    
    st.header(f"Ship: {ship_name}")
    st.write(f"**IMO Number:** {ship_info['IMO']}")
    st.write(f"**MMSI Number:** {ship_info['MMSI']}")
    st.write(f"**Type of Cargo Carrying:** {ship_info['Type']}")
    st.write(f"**Speed of Ship:** {ship_info['Speed']}")
    st.write(f"**Route:** {ship_info['Route']}")
    st.write(f"**Number of Crew Members:** {ship_info['Crew']}")

# Add more details or functionalities as needed
