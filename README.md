Introduction
This project is a Tiny Language Interpreter implemented in Python. The interpreter processes and evaluates programs written in the Tiny language using recursive-descent parsing. It reads input from a file, checks for syntax errors, and evaluates arithmetic expressions and conditionals.

Features
Parses Tiny language code based on its defined grammar.
Reads .tiny files and processes statements.
Identifies syntax errors and provides error handling.
Supports arithmetic operations and conditional expressions.
Prerequisites
Python 3.x
No additional libraries required
Usage
To run the Tiny Language Interpreter, use the following command:

bash
Copy
Edit
python parser_2897958.py sample.tiny
Replace sample.tiny with your actual Tiny language source file.

Example Input and Expected Output
Input Program	Expected Output
let x : int = 5 ; in int ( x + x * x ) end ;	30
let r : real = 10.0 ; pi : real = 3.1416 ; in real ( pi * r * r ) end ;	314.16
let a : int = 3 ; b : real = 0.5 ; in real ( if a > 5 then b + 1.1 else c ) end ;	0.25
Error Handling
Displays an error message if the input file is not found.
Detects syntax errors in Tiny language programs.
Handles exceptions during parsing and evaluation.
File Structure
parser_2897958.py - The main interpreter script.
sample.tiny - Example Tiny language program (replace with actual input files).
Conclusion
The parser_2897958.py script provides an effective way to interpret Tiny language programs, ensuring syntax correctness and evaluating expressions according to the defined grammar.

