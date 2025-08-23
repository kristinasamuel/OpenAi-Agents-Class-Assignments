#  instruction/dynamic_instruction.py
from agents import RunContextWrapper
def dynamic_instruction(ctx: RunContextWrapper, agent):
    # All hotel details
    HOTELS = {
        "Hotel Sannata": {
            "owner": "Ms.Samyira",
            "total_rooms": 100,
            "reserved_rooms": 20,
            "available_rooms": 80,
            "location": "Karachi",
   
        },
        "Hotel Pearl": {
            "owner": "Ms.Jessica",
            "total_rooms": 150,
            "reserved_rooms": 30,
            "available_rooms": 120,
            "location": "Lahore",
        },
        "Hotel Skyline": {
            "owner": "Mr.Andrew Shahzad",
            "total_rooms": 75,
            "reserved_rooms": 25,
            "available_rooms": 50,
            "location": "Islamabad",
        }
    }

    # Get user query from context
    user_query = ctx.context.get("user_query", "").lower()

    # Detect hotel name in user query
    hotel_name = None
    for h_name in HOTELS.keys():
        if h_name.lower() in user_query:
            hotel_name = h_name
            break

    if not hotel_name:
        return "Hi! I am your Hotel Assistant. Please include a valid hotel name in your query (Hotel Sannata, Hotel Pearl, Hotel Skyline)."

    hotel = HOTELS[hotel_name]

    # Return all hotel details dynamically
    return (
        f"Hi! I am your Hotel Assistant. Here is the information for {hotel_name}:\n"
        f"- Owner: {hotel['owner']}\n"
        f"- Location: {hotel['location']}\n"
        f"- Total Rooms: {hotel['total_rooms']}\n"
        f"- Reserved Rooms: {hotel['reserved_rooms']}\n"
        f"- Available Rooms: {hotel['available_rooms']}\n"
    )
