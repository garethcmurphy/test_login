# Login System Debugging Tool 🐛🔐  

This repository provides a tool to **identify and debug login failures** in a system where logins fail intermittently. It automates repeated login attempts, logs error messages, and tests different approaches to determine if issues are caused by an offline LDAP server.

---

## Features ✨  

- **Automated Login Testing**: Repeated login attempts to reproduce failures.  
- **Error Logging**: Captures detailed error messages for analysis.  
- **Root Cause Analysis**: Tests whether issues are due to LDAP server availability.  

---

## Prerequisites 🛠️  

- Python 3.8+  
- Required libraries:
  - `requests` (for login requests)  
  - `logging` (for error logging)  

Install dependencies:  
pip install requests  

---

## Installation  

1. Clone the repository:  
   git clone https://github.com/your-username/login-debug-tool.git  
   cd login-debug-tool  

2. Install dependencies:  
   pip install -r requirements.txt  

---

## Usage 🔧  

1. Update the `config.json` file with:  
   - Login URL  
   - Credentials for testing  
   - LDAP server addresses  

2. Run the debugging tool:  
   python login_debugger.py  

3. Review the logs in the `logs/` directory for error messages and server statuses.  

---

## File Structure 📂  

- `login_debugger.py`: Main script to perform login tests and log errors.  
- `config.json`: Configuration file for login and LDAP server details.  
- `logs/`: Directory for storing error logs.  
- `README.md`: Documentation for the repository.  

---

## Example Commands  

- Run the debugger:  
  python login_debugger.py  

- View logs:  
  cat logs/debug.log  

---

## Contributing 🤝  

1. Fork the repository.  
2. Create a new branch:  
   git checkout -b feature/your-feature  

3. Commit your changes:  
   git commit -m "Add your feature"  

4. Push the branch:  
   git push origin feature/your-feature  

5. Open a pull request.  

---

## License 📝  

This project is licensed under the MIT License. See the LICENSE file for details.  

---

**Identify and resolve login issues with this debugging tool!** 🐛🔐  
