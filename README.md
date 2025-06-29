Password Strength Analyzer

Project Overview

The Password Strength Analyzer is a Python based tool developed for a Security Automation course. Its purpose is to help users test the strength of their passwords using automated logic. The program evaluates passwords based on length, character diversity (uppercase, lowercase, digits, special characters), and similarity to known weak and common passwords.

This project shows how automation can be used to improve password security and prevent weak credentials. It runs as a commandline tool and gives real time feedback with improvement suggestions.

---

Features

- Checks password strength based on
  - Length
  - Use of uppercase and lowercase letters
  - Use of numbers and special characters
  - Detection of known weak passwords from a static list
- Scores password strength on a scale
- Gives user friendly suggestions for improving weak passwords
- Lightweight with no external libraries needed

---

Dependencies

This project uses only built in Python libraries, so no installation of packages are needed.

Python 3.7 or higher

A text file named common_passwords.txt with a list of weak/common passwords

---

How to Set Up and Run

### 1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/password-strength-analyzer.git
cd password-strength-analyzer

python main.py

