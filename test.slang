// Example of break statements in SLang

// Example 1: Simple break from a while loop
var int counter = 1
var int limit = 10

print "Example 1: Breaking out of a while loop"
while (true) {  // Infinite loop
    print counter
    counter = counter + 1
    
    if (counter > limit) {
        print "Reached limit, breaking out!"
        break
    }
}

// Example 2: Breaking from a for loop
var array numbers = [10, 20, 30, 40, 50, 60, 70]
var int target = 40
var boolean found = false

print "Example 2: Searching array with break"
for num in numbers {
    print "Checking number:"
    print num
    
    if (num == target) {
        print "Found target!"
        found = true
        break
    }
}

print "Search result:"
print found

// Example 3: Breaking from nested loops
var int i = 0
var int j = 0

print "Example 3: Breaking from nested loops"
while (i < 3) {
    i = i + 1
    print "i ="
    print i
    
    j = 0
    while (j < 5) {
        j = j + 1
        print "  j ="
        print j
        
        if (j == 3) {
            print "  Breaking from inner loop"
            break
        }
    }
}