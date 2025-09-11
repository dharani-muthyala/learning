// Import tools to work with dates and JSON
import java.text.SimpleDateFormat
import groovy.json.JsonOutput

// List of current bookings
def bookings = [
    [room: 101, checkIn: '2025-04-10', checkOut: '2025-04-15'],
    [room: 102, checkIn: '2025-04-12', checkOut: '2025-04-18'],
    [room: 103, checkIn: '2025-04-20', checkOut: '2025-04-25']
]

// All rooms in the hotel
def allRooms = [101, 102, 103, 104]

// Format to read and compare date strings
def dateFormat = new SimpleDateFormat("yyyy-MM-dd")

// Requested booking dates (new guest wants a room)
def startDate = dateFormat.parse("2025-04-15")
def endDate = dateFormat.parse("2025-04-20")

// Function to check if two bookings overlap
boolean isOverlap(Date start1, Date end1, Date start2, Date end2) {
    return !(end1 <= start2 || end2 <= start1)
}

// Check which rooms are available
def availableRooms = allRooms.findAll { roomNum ->
    // Get all bookings for this room
    def roomBookings = bookings.findAll { it.room == roomNum }

    // Room is available if all its bookings do NOT overlap
    roomBookings.every { booking ->
        def bStart = dateFormat.parse(booking.checkIn)
        def bEnd = dateFormat.parse(booking.checkOut)
        !isOverlap(startDate, endDate, bStart, bEnd)
    }
}

// Show the result
println "Available rooms from 2025-04-15 to 2025-04-20: $availableRooms"

// BONUS: Book one of the available rooms and save to file
if (availableRooms) {
    def roomToBook = availableRooms[0] // Take the first available room
    bookings << [room: roomToBook, checkIn: "2025-04-15", checkOut: "2025-04-20"]

    // Save all bookings to a file in JSON format
    def json = JsonOutput.prettyPrint(JsonOutput.toJson(bookings))
    new File("bookings.json").write(json)

    println "Room $roomToBook booked successfully!"
    println "Bookings saved to 'bookings.json'"
} else {
    println "Sorry, no rooms available for your selected dates."
}
