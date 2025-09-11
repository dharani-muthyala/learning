// printing hello world
println "Hello! World...."

println "-------------------------------------------------------------------------"
// defining variables
def name = "John"          // Groovy is case sensitive and dynamically typed 
println "My Name is"+name // (or) println "My Name is ${name}"

def (x,y,z) = [20,30,40]
println x
println y
println z

println"-------------------------------------------------------------------------"
// Groovy datatypes : byte,short,int,long,float,double,char,string
byte b = 10
println b
println Byte.MIN_VALUE
println Byte.MAX_VALUE
//char
char c = "*"   // char only considers a single character(like,A,@,*) but not a a string(abcd)
println c
//boolean
boolean flag = "true"
println flag
//string
String str = "Groovy"
println str

println "------------------------------------------------------------"
// Groovy operators :
// Arithmetic operators
assert 1 + 2 == 3
println(1 + 2 == 3)
assert 4 - 3 == 1
assert 3 * 5 == 15
assert 3 / 2 == 1.5
assert 10 % 3 == 1
assert 2 ** 3 == 8
assert 9.intdiv(5) == 1
// incrementing ++ and decrement -- operators
def d = 2 
def e = d++ * 3
assert d == 3 && e == 6
println(d == 3 && e == 6)

def f = 3
def g = f-- * 2
assert f == 2 && g == 6
// Asiignment arithmetic operators
def h = 4
h += 3 //h = h + 3
assert h == 7
 def i = 5
i -= 3 // i = -3
assert i == 2
// Relation operators
assert 1 + 2 == 3
assert 3 != 4

assert -2 < 3
assert 2 <= 2

assert 5 > 1
assert 5 >= -2
// Logical operators
assert !false        // NOT
assert true && true  // AND
assert true || false // OR

println "-----------------------------------------------------------"
// Groovy conditional statements:
// checking the num is +ve or -ve (if-else)
def num = 11
if (num > 0)
    println "num is +ve"
else 
    println "num is -nv" 
// Nested if
def n = 12
if (n > 0)
    println "n is +ve"
else if (n == 0)
    println "n is zero"
else 
    println "n is +ve"
// Switch case
def j = 10
def result = ""
 
switch(j) {
    case 0:
        result = "j is zero"
        break
    case {j>0}:
        result = "j is +ve"
        break
    case {j<0}:
        result = "j is -ve" 
        break 
    default:
        result = "Invalid number"      
}  
println result

println "-----------------------------------------------------------------"
// Groovy Loops: (keywords in loops: upto,times,step)
// for loop        // using keywords:
for (a in 1..5){   // 1.upto(5) { println "$it" }
    println a      // 5.times { println "$it" }
}                  // 1.step(10, 2) { println "$it" }
// iterate over a map
def map = ["name": "Groovy", "subject": "Automation"]
for (m in map) {
     print m.key+":"
     println m.value
}
// while loop 
int p = 1
while(p<=10) {
    println  p 
    p=p+1
}

 