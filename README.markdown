# SLang Interpreter

A simple interpreter for the SLang programming language, built using ANTLR and Python. SLang supports variable declarations, assignments, arithmetic operations, conditionals, loops, arrays, and print statements.

## Project Status
This is a work-in-progress. The interpreter currently supports:
- **Variable declarations and assignments** (including re-assignment)
- **Arithmetic operations** (addition, subtraction, multiplication, division)
- **Conditionals** (`if`, `else`)
- **While loops** (with `break` statement support)
- **For-loops** (fixed bug, also supports `break`)
- **Arrays** (basic support)
- **Print statements** (`print`)
- **Custom Error Handling** (via `SLangBaseError` and subclasses for Syntax, Name, Type, Value, etc., now renamed to `OOPsies` for more personalized debugging messages 🎉)

> **Note**: The `OOPsies` error renaming has been implemented, replacing standard error messages with more user-friendly `OOPsies` messages. However, the interpreter is still a work-in-progress. It currently does not handle unrecognized operators, resulting in errors from Python's parser files instead of being managed by the interpreter's custom `OOPsies` system.

There are no longer known issues with variable re-assignment or for-loops. Please refer to the [Issues](#known-issues) section for any future concerns.

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

## Running SLang Programs

The interpreter now supports running SLang programs from any file. Here's how to run your SLang code:

1. **Create a SLang program file** with a `.slang` extension (recommended) or any extension of your choice.

2. **Run the interpreter** by passing your program file as a command-line argument:
   ```bash
   python run_interpreter.py your_program.slang
   ```

3. **Example**: To run the included example program:
   ```bash
   python run_interpreter.py examples/factorial.slang
   ```

### Example SLang Program

Here's a simple example of a SLang program that demonstrates a while loop with a break statement:

```
// Example of break in a while loop
var int counter = 1
var int limit = 5

while (true) {  // Infinite loop
    print counter
    counter = counter + 1
    
    if (counter > limit) {
        print "Done counting!"
        break  // Exit the loop when limit is reached
    }
}
```

Save this to a file (e.g., `break_example.slang`) and run it with:
```bash
python run_interpreter.py break_example.slang
```

## Language Features

### Basic Syntax
- Variable declaration: `var [type] [name] = [value]`
- Assignment: `[name] = [value]`
- Print statements: `print [expression]`
- Comments: `// This is a comment`

### Types
- `int`: Integer values
- `float`: Floating-point values
- `boolean`: Boolean values (`true` or `false`)
- `string`: Text strings enclosed in double quotes
- `array`: Lists of values

### Control Flow
- If statements: `if (condition) { ... } else { ... }`
- While loops: `while (condition) { ... }`
- For loops: `for item in array { ... }`
- Break statement: `break` (exits the innermost loop)

### Operators
- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Comparison: `==`, `!=`, `<`, `<=`, `>`, `>=`
- Logical: `&&` (and), `||` (or), `!` (not)
- Ternary: `condition ? trueValue : falseValue`
