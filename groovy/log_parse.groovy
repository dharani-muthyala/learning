// task-3 -------| Log Parser
// File paths
def logFile = new File("server.log")
def errorFile = new File("errors.txt")

// Counters
int infoCount = 0
int errorCount = 0
int warnCount = 0

// Clear previous error file content if any
errorFile.text = ""

// Process each line of the log
logFile.eachLine { line ->
    if (line.startsWith("[INFO]")) {
        infoCount++
    } else if (line.startsWith("[ERROR]")) {
        errorCount++
        errorFile << line + "\n"  // Append error line to errors.txt
    } else if (line.startsWith("[WARN]")) {
        warnCount++
    }
}

// Print results
println "INFO messages: $infoCount"
println "ERROR messages: $errorCount"
println "WARN messages: $warnCount"
