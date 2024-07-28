import streamlit as st

# Initial sample data
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

# Streamlit app
st.title("TORM Shipping Company - Ship Tracking")

# Function to add new ship
def add_ship(name, imo, mmsi, type_, speed, route, crew):
    ships_data[name] = {
        "IMO": imo,
        "MMSI": mmsi,
        "Type": type_,
        "Speed": speed,
        "Route": route,
        "Crew": crew
    }

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

# Form to add new ship
with st.form("Add New Ship"):
    st.header("Add New Ship Details")
    new_ship_name = st.text_input("Ship Name")
    new_ship_imo = st.text_input("IMO Number")
    new_ship_mmsi = st.text_input("MMSI Number")
    new_ship_type = st.text_input("Type of Cargo Carrying")
    new_ship_speed = st.text_input("Speed of Ship")
    new_ship_route = st.text_input("Route")
    new_ship_crew = st.number_input("Number of Crew Members", min_value=1, step=1)
    submit_button = st.form_submit_button(label="Add Ship")
    
    if submit_button:
        if new_ship_name and new_ship_imo and new_ship_mmsi and new_ship_type and new_ship_speed and new_ship_route and new_ship_crew:
            add_ship(new_ship_name, new_ship_imo, new_ship_mmsi, new_ship_type, new_ship_speed, new_ship_route, new_ship_crew)
            st.success(f"New ship '{new_ship_name}' added successfully!")
        else:
            st.error("Please fill in all the details to add a new ship.")

# Update the sidebar with the new ship data
ship_name = st.sidebar.selectbox("Select Ship", list(ships_data.keys()), key="ship_selector_updated")

# Display the updated ship details
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
