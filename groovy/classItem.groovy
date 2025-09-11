// task-2 ---------| Grocery Billing System with Tax + Discount Rules
// Item class to hold name, price, and category
class Item {
    String name
    double price
    String category

    // Get tax rate based on category
    double getTaxRate() {
        if (category.toLowerCase() == 'essential') {
            return 0.05
        } else if (category.toLowerCase() == 'luxury') {
            return 0.18
        } else {
            return 0.0
        }
    }

    // Calculate tax amount
    double getTaxAmount() {
        return price * getTaxRate()
    }

    // Price including tax
    double getTotalWithTax() {
        return price + getTaxAmount()
    }
}

// Function to generate bill
def generateBill(List<Item> items) {
    double totalTax = 0
    double grossTotal = 0
    Map<String, Double> itemTaxes = [:]

    // Calculate total and tax for each item
    items.each { item ->
        double tax = item.getTaxAmount()
        totalTax += tax
        grossTotal += item.getTotalWithTax()
        itemTaxes[item.name] = tax.round(2)
    }

    // Apply discount if applicable
    double discount = (grossTotal > 5000) ? 500 : 0
    double finalTotal = grossTotal - discount

    // Save to file (bonus)
    def file = new File("final_bill.txt")
    file.withWriter('UTF-8') { writer ->
        writer.writeLine("Final Total: ${finalTotal.round(2)}")
        writer.writeLine("Total Discount: ${discount}")
        itemTaxes.each { name, tax ->
            writer.writeLine("${name} Tax: ${tax}")
        }
    }

    // Return result
    return [
        finalTotal   : finalTotal.round(2),
        totalDiscount: discount,
        itemTaxes    : itemTaxes
    ]
}

// Sample items
def items = [
    new Item(name: "Rice", price: 2000, category: "essential"),
    new Item(name: "Perfume", price: 3000, category: "luxury"),
    new Item(name: "Soap", price: 200, category: "essential")
]

// Run billing function
def result = generateBill(items)

// Final simple output
println "Final Total: ${result.finalTotal}"
println "Total Discount: ${result.totalDiscount}"
result.itemTaxes.each { name, tax ->
    println "${name} Tax: ${tax}"
}
