LOCATIONS = [
    {
        "id": 1,
        "name": "Customer1",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Customer2",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Customer3",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the locationS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location