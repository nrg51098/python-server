EMPLOYEES = [
    {
        "id": 1,
        "name": "Employee1",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Employee2",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Employee3",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee