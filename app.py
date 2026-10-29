from flask import Flask, render_template, request

app = Flask(__name__)

# Estimated daily cost per person for each destination
DESTINATIONS = {
    "Manali": 2500,
    "Shimla": 2200,
    "Goa": 3000,
    "Jaipur": 2000,
    "Delhi": 1800,
    "Agra": 1700
}


@app.route("/")
def home():
    return render_template(
        "index.html",
        destinations=DESTINATIONS.keys(),
        result=None
    )


@app.route("/plan", methods=["POST"])
def plan_trip():
    destination = request.form.get("destination", "")

    try:
        days = int(request.form.get("days", 0))
        people = int(request.form.get("people", 0))
    except (ValueError, TypeError):
        return "Please enter valid trip details.", 400

    if destination not in DESTINATIONS:
        return "Please select a valid destination.", 400

    if not 1 <= days <= 30 or not 1 <= people <= 20:
        return "Days must be 1-30 and travellers must be 1-20.", 400

    # Get the estimated daily cost per person
    daily_cost = DESTINATIONS[destination]

    # Divide the daily cost into expense categories
    accommodation = daily_cost * 40 // 100
    food = daily_cost * 30 // 100
    transport = daily_cost * 20 // 100
    other_expenses = daily_cost - accommodation - food - transport

    # Calculate total expenses for all travellers and days
    accommodation_total = accommodation * days * people
    food_total = food * days * people
    transport_total = transport * days * people
    other_total = other_expenses * days * people

    total_cost = daily_cost * days * people

    # Send the result to the webpage
    result = {
        "destination": destination,
        "days": days,
        "people": people,
        "accommodation": accommodation_total,
        "food": food_total,
        "transport": transport_total,
        "other": other_total,
        "total_cost": total_cost
    }

    return render_template(
        "index.html",
        destinations=DESTINATIONS.keys(),
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)