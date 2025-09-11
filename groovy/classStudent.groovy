// task-1 --------|Student Performance Report with Class Object
class Student {
    String name
    Map<String, Integer> subjectScores

    Student(String name, Map<String, Integer> subjectScores) {
        this.name = name
        this.subjectScores = subjectScores
    }

    double getAverage() {
        if (subjectScores.isEmpty()) return 0
        return subjectScores.values().sum() / subjectScores.size()
    }

    String getGrade() {
        double avg = getAverage()
        if (avg >= 80) return "A"
        else if (avg >= 60) return "B"
        else if (avg >= 40) return "C"
        else return "F"
    }

    String toString() {
        return "${name}: Grade ${getGrade()} (Avg: ${getAverage().round(2)})"
    }
}

// Create students
def students = [
    new Student("Anjali", [Math: 85, English: 78, Science: 91]),
    new Student("Rahul", [Math: 66, English: 59, Science: 72]),
    new Student("Neha", [Math: 35, English: 40, Science: 39])
]

// Top performer
def topStudent = students.max { it.getAverage() }
println "Top Performer: ${topStudent.name} with Average: ${topStudent.getAverage().round(2)}"

// Print each student's grade
println "\n--- Student Performance Report ---"
students.each { println it }

// Save to file
def report = new File("student_report.txt")
report.withWriter { writer ->
    writer.writeLine("Top Performer: ${topStudent.name} with Average: ${topStudent.getAverage().round(2)}")
    writer.writeLine("\n--- Student Performance Report ---")
    students.each { writer.writeLine(it.toString()) }
}
println "\nReport saved to student_report.txt"
