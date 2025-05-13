# SLang Interpreter

A simple interpreter for the SLang programming language, built using ANTLR and Python. SLang supports variable declarations, assignments, arithmetic operations, conditionals, loops, arrays, and print statements.

## Project Status
This is a work-in-progress. The interpreter currently supports:
- **Variable declarations and assignments** (including re-assignment)
- **Arithmetic operations** (addition, subtraction, multiplication, division)
- **Conditionals** (`if`, `else`)
- **For-loops** (fixed bug)
- **Arrays** (basic support)
- **Print statements** (`print`)
- **Custom Error Handling** (via `SLangBaseError` and subclasses for Syntax, Name, Type, Value, etc., now renamed to `OOPsies` for more personalized debugging messages 🎉)

> **Note**: The `OOPsies` error renaming has been implemented, replacing standard error messages with more user-friendly `OOPsies` messages. However, the interpreter is still a work-in-progress. It currently does not handle unrecognized operators, resulting in errors from Python's parser files instead of being managed by the interpreter's custom `OOPsies` system.

There are no longer known issues with variable re-assignment or for-loops. Please refer to the [Issues](#known-issues) section for any future concerns.

## Key Features

- **Variable Declarations** using keywords like `var`, `yo`, `ayo`, or `let`.
- **Multiple Data Types**: `int`, `float`, `boolean`, `string`, and `array` (`gang`).
- **Control Flow**: Supports `if`/`else`, `while`, and `for-in` loops.
- **Array Support**: Array literals, indexing, and iteration over arrays.
- **Expressions**: Includes arithmetic, logical, relational, and conditional expressions.
- **Flexible Boolean and Assignment operators**, like `is`, `aint`, and `be`.


## Syntax Overview

## 1. Variable Declaration

```slang
var int x = 10;
ayo string name = "SLang";
```
You can use any of the following for declaration: `var`, `yo`, `ayo`, `let` or don't use it at all, and the language will infer the data type. 

## 2. Data Types
`int`: intergers
`float`: floats
`boolean`: booleans
`string`: strings
`array` / `gang`: arrays

## 3. Printing Output
```slang
spit "Sup";
ayo string name = "SLang";
holla name;
```

## 4. Conditionals
```
if (100 > 90) {
    holla "Great!";
} else {
    yap "Try again!";
}
```

## 5. Loops
While Loops
```
while (x < 5) {
    holla x;
    x = x + 1;
}
```

For Loops
```
for item in nums {
    print item;
}
```

## 6. Operations
- Arithmatic: `+`, `-`-, `*`, `/`, `%`
- Logical: `&&` / `and`, `||` / `or`, `!` / `not`
- Relational: `<`, `<=`, `>`, `>=` 
- Equality: `==` / `is`, `!=` / `aint`

## 7. Arrays
SLang supports both arrays and arrays indexing

```
arr = [1, 2, 3];
print arr[0];
```

## Setup

### Prerequisites
- **Python 3.8+**: Ensure Python is installed (`python3 --version`).
- **ANTLR 4.13.2**: Required to generate the lexer and parser from the grammar.
- **Java**: Needed to run the ANTLR tool.
- **Git**: For cloning the repository.

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/slang-interpreter.git
   cd slang-interpreter
   ```

2. **Install ANTLR Python Runtime**:
   ```bash
   pip install antlr4-python3-runtime==4.13.2
   ```

3. **Download ANTLR**:
   Download the ANTLR 4.13.2 JAR file:
   ```bash
   wget https://www.antlr.org/download/antlr-4.13.2-complete.jar
   ```
   Or download manually from [antlr.org](https://www.antlr.org/download.html).

4. **Generate Lexer and Parser**:
   Run the ANTLR tool to generate Python lexer and parser files from `SLang.g4`:
   ```bash
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor SLang.g4
   ```

## Contributing

Please submit pull requests to the `dev` branch with clear descriptions. For significant changes like language features or refactoring (e.g., error handling), use feature branches like `feature/your-feature-name`.