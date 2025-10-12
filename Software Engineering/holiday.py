# Step 1: Define fixed costs
def plane_cost(city_flight):
    if city_flight.lower() == "johannesburg":
        return 1000
    elif city_flight.lower() == "london":
        return 1700
    elif city_flight.lower() == "mumbai":
        return 1300
    elif city_flight.lower() == "new york":
        return 1600
    else:
        return 0

def hotel_cost(num_nights):
    return num_nights * 1000

def car_rental_cost(rental_days):
    return rental_days * 350

# Step 2: Get user input
city_flight = input("Enter the city you are flying to (Paris, London, Dubai, New York): ")
num_nights = int(input("Enter the number of nights you will stay in a hotel: "))
rental_days = int(input("Enter the number of days you will rent a car: "))

# Step 3: Calculate total cost
total_cost = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental_cost(rental_days)

# Step 4: Display results
print("\n--- Holiday Summary ---")
print(f"Flight to {city_flight.title()}: R{plane_cost(city_flight)}")
print(f"Hotel for {num_nights} nights: R{hotel_cost(num_nights)}")
print(f"Car rental for {rental_days} days: R{car_rental_cost(rental_days)}")
print(f"Total holiday cost: R{total_cost}")
