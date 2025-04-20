
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
   pip install antlr4-python3-runtime==4.9.2
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

