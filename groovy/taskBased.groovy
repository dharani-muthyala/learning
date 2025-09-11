// Library Book Tracker -----|task-1   (Day-1)
boolean isBookAvailable(String title) {
    def books = [
        [title:"The Alchemist", available:true],
        [title:"Groovy in Action", available:false]
    ]
    for (book in books) {
        if (book.title == title) {
            return book.available
        }
    }
    return false  
}

println isBookAvailable("The Alchemist")
println isBookAvailable("Groovy in Action")

println "================================================================="
// Employee salary bonus calculator -------|task-2
def updateSalaries = { employeesList ->
    employeesList.collect { emp ->
        if (emp.dept == "Sales") {
            // return updated salary employee
            return [
                name  : emp.name,
                dept  : emp.dept,
                salary: (emp.salary * 1.10).toInteger()
            ]
        } else {
            return emp
        }
    }
}
def employees = [
    [name: "Alice", dept: "Tech", salary: 50000],
    [name: "Bob", dept: "Sales", salary: 60000]
]

def updated = updateSalaries(employees)
updated.each { println it }

println "================================================================"
// online Order Price Calculator --------| task-3
def calcultePrices = { customersList ->
    def laptop = customersList.find { it.item == "Laptop" }
    if (laptop) {
        return  (laptop.price + 1600).toInteger()
    } else {
        return "Laptop not found"
    }
}

def customers = [
    [item: "Laptop", price: 60000, qty:1],
    [item: "Mouse", price: 800, qty: 2]
]

def res = calcultePrices(customers)
println res

println "================================================================="
// Movie Ratings Filter --------| task-4
def movies = [
    [title: "Interstellar", rating:4.6],
    [title: "Tenet", rating:3.9],
    [title: "Inception", rating:4.8]
]

def filteredTitles = movies.findAll { it.rating > 4.0 }*.title
println filteredTitles.collect { "\"$it\"" }

println "================================================================="
// Student Grade Summary ---------| task-5
def students = [
    [name: "Ravi", marks:78],
    [name: "Neha", marks:33]
]

students.each { student ->
    def status = student.marks >= 40 ? "pass" : "fail"
    println "${student.name}-${student.marks}-${status}"
}

println "================================================================="
// (Day-2)
// To-Do List Manager ---------|task-1
def tasks = [
    [title: "Laundry", priyority: "Low", done: false],
    [title: "Finish Groovy Practice", priyority: "High", done: false],
    [title: "Buy groceries", priyority: "Medium", done: true]
]

def getIncompleteTasks = { taskList ->
    def priyorityOrder = ["High": 1, "Medium": 2, "Low": 3]
    return taskList
        .findAll { !it.done }
        .sort { priyorityOrder[it.priyority] }  
        .collect { "\"${it.title}\"" }
}

println getIncompleteTasks(tasks)

println "================================================================="
// Bank Transactions Tracker -------|task-2
def transactions = [
   [type: "deposit", amount: 1000],
   [type: "withdrawal", amount: 300],
   [type: "deposit", amount: 500]
]

def initialBalance = 2000

def calculateFinalBalance(initialBalance, transactions) {
    def finalBalance = initialBalance
    transactions.each { tx ->
        if (tx.type == "deposit") {
            finalBalance += tx.amount
        } else if (tx.type == "withdrawal") {
            finalBalance -= tx.amount
        }
    }
    return finalBalance
}

println calculateFinalBalance(initialBalance, transactions)

println "======================================================"
// Simple Voting System ------|task-3
def votes = ["Apple", "Banana", "Apple", "Mango", "Banana", "Apple"]

def mostVotedFruit = { list ->
    
    def count = [:]  // empty map for storing voted Keys

    list.each { fruit ->
        if (count[fruit] == null) {
            count[fruit] = 1
        } else {
            count[fruit] += 1
        }
    }

    def mostVoted = count.max { it.value }?.key
    return "\"${mostVoted}\""
}

println mostVotedFruit(votes)

println "============================================================="
// Bus Seat Reservation System ---------|task-4
def bookedSeats = [3, 5, 9, 12, 30]

def availableSeats = (1..40).findAll { seat ->
    !bookedSeats.contains(seat)
}

println "A list from 1 to 40 excluding those booked ones."

println "==============================================================" 
// Mini Shopping Discount System ---------|task-5
def cart = [
    [item: "Shoes", price: 1500],
    [item: "T-shirt", price: 700],
    [item: "Jacket", price: 2500]
]
def updatedCart = cart.collect { product ->
    if (product.price > 1000) {
        def discountedPrice = product.price * 0.8
        [item: product.item, price: (int)discountedPrice]
    } else {
        product
    }
}

println "["
updatedCart.eachWithIndex { item, i ->
    def comma = (i < updatedCart.size() - 1) ? "," : ""
    println "  [item: \"${item.item}\", price: ${item.price}]${comma}"
}
println "]"