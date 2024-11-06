# Lexical Analyzer for Simple C-Like Language

This project implements a lexical analyzer (tokenizer) for a subset of the C programming language. The analyzer processes an input string, identifies tokens like keywords, identifiers, numbers, operators, and special characters, and outputs their types and values. This project is ideal for understanding compiler design fundamentals, especially the lexical analysis phase.

## Features

- **Tokenizes Input:** Identifies keywords, identifiers, numbers, operators, and special characters.
- **C Keywords Support:** Recognizes keywords like `int`, `float`, `if`, `else`, and more.
- **Simple Operator Handling:** Supports operators such as `+`, `-`, `*`, `/`, `=`, `==`, `!=`, and others.

## Project Structure

- **Token Class:** Represents a single token with `type` and `value` attributes.
- **LexicalAnalyzer Class:** Processes the input string and generates tokens based on C-like language rules.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name


Here's a README.md template for your project that you can use on GitHub:

markdown
Copy code
# Lexical Analyzer for Simple C-Like Language

This project implements a lexical analyzer (tokenizer) for a subset of the C programming language. The analyzer processes an input string, identifies tokens like keywords, identifiers, numbers, operators, and special characters, and outputs their types and values. This project is ideal for understanding compiler design fundamentals, especially the lexical analysis phase.

## Features

- **Tokenizes Input:** Identifies keywords, identifiers, numbers, operators, and special characters.
- **C Keywords Support:** Recognizes keywords like `int`, `float`, `if`, `else`, and more.
- **Simple Operator Handling:** Supports operators such as `+`, `-`, `*`, `/`, `=`, `==`, `!=`, and others.

## Project Structure

- **Token Class:** Represents a single token with `type` and `value` attributes.
- **LexicalAnalyzer Class:** Processes the input string and generates tokens based on C-like language rules.

## Installation

*Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
```

*Ensure you have Python 3.x installed. No additional packages are required.
*Usage
*To run the lexical analyzer:

 #python Compiler_project1.py


*Enter a C-like statement when prompted:
 Please enter the statement
 #for (int i = 0; i <= 3; i++) { }

*The program will output each token identified in the input:

<Token Type: KEYWORD, Value: for>
<Token Type: SPECIAL_CHAR, Value: (>
<Token Type: KEYWORD, Value: int>
...



License
This project is licensed under the MIT License. See the LICENSE file for details.

Replace `https://github.com/your-username/your-repo-name.git` with your actual GitHub repository URL. This `README.md` provides a clear overview of the project, installation instructions, usage details, example output, and contribution guidelines.
