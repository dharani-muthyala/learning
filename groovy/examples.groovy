// Groovy Exception Handling  (blocks: try-catch, try-catch-finally, try-finally)
// try-catch 
try {
int i = 1/0

}catch(Exception exp) {
    println "I am in the exception block"
    println exp.getCause()
    println exp.getMessage()
   // exp.printStackTrace()   ---> it shows whole exceptions
}finally {
    println "I am inside finally block"
}
println "Another set of code"   // --> here the main advantage is, if any exception occurs the flow of execution will can't stop 

println "--------------------------------------------------------------"
// Strings:
def name = "John"
println name
println "My name is " + name
println "My name is ".concat(name)
 
println "My name is $name"
println 'My name is $name'

def s1 = """ This is a groovy class 
and we are learning strings"""
println s1 
//
def s2 = "Rushma"
println s2.length()
println s2[2]
println s2[-2]
println s2.indexOf('s')

println s2[0..2]
println s2[5..2] 
println s2[0,3,5]

println s2.substring(2)
println s2.subSequence(1,4)
//
def s3 = "This is a groovy class"
println s3.split(" ")
println s3-("groovy")
println s3.replace("class", "session")
// lower-upper cases
println s3.toLowerCase()
println s3.toUpperCase()
println s3.toList()
println "Groovy " * 3
// slashy-doller slashy strings
def name1 = "Rushma"
def s4 = /a green tree/
def s5 = $/a blue sky/$
println s4
println s5

println "---------------------------------------------------------------------"
// Groovy Methods:
def printHello() {
    println "Hello....."
}
printHello()
def sum( int a=5, int b=10) {
    println "sum is "+(a+b)
}
sum()
// return type:
def sub(int a, int b) {
    def c = a-b
    return c
}
def result = sub(10,5)
println "result is "+result
// Instance method:
class Method1 {
    static void main(args) {
        Method1 myFunc = new Method1()
        myFunc.myMethod()
    }
}
def myMethod() {
    println ("I am inside the my method")
}