// task-4 -------| Flight Ticket Pricing Engine
// Function to calculate final flight ticket fare
double calculatePrice(double baseFare, String travelClass, String day) {
    double finalPrice = baseFare

    // Apply class multiplier
    switch (travelClass.toLowerCase()) {
        case "business":
            finalPrice *= 1.5
            break
        case "first":
            finalPrice *= 2.0
            break
        case "economy":
            // No change
            break
        default:
            throw new IllegalArgumentException("Invalid travel class: $travelClass")
    }

    // Check if the day is weekend
    if (day.toLowerCase() in ["saturday", "sunday"]) {
        finalPrice *= 1.1
    }

    return finalPrice
}

// Example usage
def price = calculatePrice(5000, "Business", "Sunday")
println "₹${price as int}"




