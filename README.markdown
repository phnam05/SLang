# 🔥 SLang: The Stylish Programming Language

SLang is a modern, expressive programming language with slang-inspired syntax, built using ANTLR and Python. This language combines familiar programming constructs with street-style keywords and expressions to create a fun, yet powerful coding experience.

## 💯 Language Philosophy

SLang was created to make programming more approachable and expressive. It draws inspiration from:
- Street/urban slang for keywords and expressions
- Traditional programming language constructs for familiarity
- Modern error handling with personalized "OOPsies" messages

Our language aims to be both educational and entertaining, showing how programming languages can have personality while maintaining functionality.

## 🚀 Key Features

- **Typed Variable Declarations** using `int`, `float`, `boolean`, `string`, and `array`/`gang`
- **Alternative Keywords** like `holla`/`spit`/`yap` (print), `fr`/`legit` (true), `nah` (false)
- **Unique Control Flow** syntax with familiar patterns
- **Modern Array Support** with literal expressions, indexing, and iteration
- **Personalized Error Handling** via the "OOPsies" system for friendly debugging
- **Comprehensive Type Checking** to catch errors before they happen
- **Multi-keyword Support** for most operations (e.g., multiple ways to say "true" or "print")

## 📝 Syntax Overview

### Variable Declaration & Assignment

SLang supports traditional variable declarations with type annotations:

```slang
// Basic variable declarations with type annotation
int x = 10;
float pi = 3.14;
string name = "SLang";
boolean isAwesome = true;  // or "fr" or "legit"

// Arrays
array numbers = [1, 2, 3, 4, 5];  // you can also use "gang" instead of "array"
```

### Data Types

SLang supports five primary data types:

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integer values | `int count = 42;` |
| `float` | Floating-point numbers | `float temp = 98.6;` |
| `boolean` | Boolean values (true/false) | `boolean active = true;` |
| `string` | Text strings | `string greeting = "Hey!";` |
| `array`/`gang` | Collections of values | `array scores = [85, 90, 78];` |

### Output & Printing

Multiple ways to output information:

```slang
// Different ways to print
print "Standard output";
holla "Same thing, different style!";
spit "Getting the message out there";
yap "Just saying...";

// Printing variables and expressions
int score = 95;
print "Your score:", score;
holla "Calculation result:", score * 2;
```

### Conditionals

SLang supports standard if/else logic with some stylish alternatives:

```slang
// Standard if/else
if (score > 90) {
    holla "Excellent work!";
} else {
    holla "Keep trying!";
}

// Alternative syntax
when (user_count > 100) {
    spit "We're going viral!";
} else {
    spit "Still growing...";
}
```

### Loops

#### While Loops

```slang
// Standard while loop
int count = 5;
while (count > 0) {
    print count;
    count = count - 1;
}

// Breaking out of loops
int i = 0;
while (i < 10) {
    if (i == 5) {
        break;  // or use "bruh" instead of "break"
    }
    i = i + 1;
}
```

#### For Loops

```slang
// Iterating over arrays
array names = ["Alex", "Taylor", "Jordan"];
for name in names {
    holla "Hello,", name;
}

// Alternative syntax
gang numbers = [1, 2, 3, 4, 5];
those num in numbers {
    print num * 2;
}
```

### Operators

SLang supports a rich set of operators:

#### Arithmetic Operators
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Modulo: `%`

#### Logical Operators
- AND: `&&` or `and`
- OR: `||` or `or`
- NOT: `!` or `not`

#### Relational Operators
- Less than: `<`
- Less than or equal: `<=`
- Greater than: `>`
- Greater than or equal: `>=`

#### Equality Operators
- Equal to: `==` or `is`
- Not equal to: `!=` or `aint`

#### Assignment Operators
- Assign: `=` or `be`

### Arrays and Indexing

SLang provides comprehensive array support:

```slang
// Creating arrays
array fibonacci = [1, 1, 2, 3, 5, 8, 13];
gang favorites = ["pizza", "tacos", "ice cream"];

// Accessing elements
print fibonacci[0];  // Prints 1 (first element)
holla favorites[2];  // Prints "ice cream" (third element)

// Modifying elements
fibonacci[3] = 4;    // Change value at index 3
```

## 🐞 Error Handling - The OOPsies System

SLang features a friendly error handling system that reports errors as "OOPsies" instead of the usual intimidating error messages. When something goes wrong, SLang tells you what happened with a personalized message:

| Error Type | Description | Example Output |
|------------|-------------|----------------|
| `SyntaxOOPsie` | Invalid syntax or parsing issues | `SyntaxOOPsie: Unexpected token at line 12, column 5: '+'` |
| `NameOOPsie` | Undefined or redeclared variables | `NameOOPsie: Variable 'counter' not declared at line 7, column 10: 'counter'` |
| `TypeOOPsie` | Type mismatches in operations or assignments | `TypeOOPsie: Expected int for 'x', got string at line 3, column 7: 'x'` |
| `ValueOOPsie` | Runtime value errors like division by zero | `ValueOOPsie: Division by zero at line 10, column 9: '/'` |
| `IndexOOPsie` | Array access issues and out of bounds errors | `IndexOOPsie: Array index out of bounds at line 15, column 11: '10'` |
| `BreakOOPsie` | Break statements outside of loops | `BreakOOPsie: 'break' outside loop at line 20, column 3: 'break'` |

The OOPsie system is designed to make debugging more approachable, especially for beginners, by providing clear information about what went wrong and where in your code the issue occurred.

## 📦 Complete Examples

These complete program examples demonstrate how to use SLang to solve actual problems. They show how different language features work together and provide templates you can modify for your own programs. Each example increases in complexity and showcases different aspects of the language.

### Temperature Converter
This example shows basic variable declarations, arithmetic operations, and printing output:

```slang
// Temperature converter program
print "Temperature Converter";
print "---------------------";

float celsius = 25.0;
float fahrenheit = (celsius * 9/5) + 32;

holla celsius, "°C equals", fahrenheit, "°F";

// Convert back
float newCelsius = (fahrenheit - 32) * 5/9;
holla fahrenheit, "°F equals", newCelsius, "°C";
```

Expected output:
```
Temperature Converter
---------------------
25.0 °C equals 77.0 °F
77.0 °F equals 25.0 °C
```

### Array Processing
This example demonstrates working with arrays, loops, and conditional statements:

```slang
// Working with arrays
array scores = [85, 92, 78, 90, 88];
print "Student scores:", scores;

// Calculate average
int sum = 0;
int i = 0;
while (i < 5) {
    sum = sum + scores[i];
    i = i + 1;
}
float average = sum / 5;
holla "Average score:", average;

// Find max score
int max = scores[0];
for score in scores {
    if (score > max) {
        max = score;
    }
}
holla "Highest score:", max;
```

Expected output:
```
Student scores: [85, 92, 78, 90, 88]
Average score: 86.6
Highest score: 92
```

### Fibonacci Generator
This more complex example shows advanced array manipulation, initialization, and algorithm implementation:

```slang
// Fibonacci sequence generator
int n = 10;  // Generate first 10 Fibonacci numbers
array fib = [0, 1];

print "Generating Fibonacci sequence...";

int i = 2;
while (i < n) {
    int next = fib[i-1] + fib[i-2];
    fib[i] = next;
    i = i + 1;
}

print "Fibonacci sequence:", fib;
```

Expected output:
```
Generating Fibonacci sequence...
Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 💻 Setup & Installation

### Prerequisites
- **Python 3.8+**: Ensure Python is installed (`python3 --version`)
- **ANTLR 4.13.2**: Required to generate the lexer and parser from the grammar
- **Java**: Needed to run the ANTLR tool
- **Git**: For cloning the repository

### Step-by-Step Installation

1. **Set Up Project Directory**:
   ```bash
   # Create a project directory
   mkdir slang-project
   cd slang-project
   
   # Download or copy the required files into this directory:
   # - SLang.g4 (grammar file)
   # - run_interpreter.py
   # - Errors.py
   # - test.slang (sample program)
   ```

2. **Install ANTLR Python Runtime**:
   ```bash
   pip install antlr4-python3-runtime==4.13.2
   ```

3. **Download ANTLR**:
   ```bash
   # Using wget:
   wget https://www.antlr.org/download/antlr-4.13.2-complete.jar

   # Or download manually from antlr.org
   ```

4. **Generate Lexer and Parser**:
   ```bash
   # Using the JAR file to generate Python code
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor SLang.g4
   ```

5. **Verify Installation**:
   ```bash
   # Run a simple test script
   python run_interpreter.py test.slang
   ```

### Running SLang Programs

To run a SLang program, use the interpreter:

```bash
python run_interpreter.py your_program.slang
```

## 🔧 Development and Extension

SLang is designed to be easily extended. Here are some areas you might want to explore:

- **New Keywords**: Add more slang-inspired alternatives to existing keywords
- **Custom Functions**: Implement support for user-defined functions
- **Extended Library**: Add built-in functions for common operations
- **Enhanced Error Messages**: Expand the OOPsies system with more detailed diagnostics

## 🤝 Contributing

Contributions are welcome! Please submit pull requests to the `dev` branch with clear descriptions. For significant changes like language features or refactoring, use feature branches like `feature/your-feature-name`.

### Contribution Guidelines

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 Project Status

This project was developed as part of a programming languages course assignment. SLang demonstrates fundamental concepts in language design including lexical analysis, parsing, and interpretation. The interpreter continues to be improved with new features and optimizations.

## 🙏 Acknowledgements

- The ANTLR team for their excellent parser generator
- Programming language design resources and communities
- All contributors who have helped shape SLang
