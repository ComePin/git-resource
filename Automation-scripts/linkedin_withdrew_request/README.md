# 💼 LinkedIn Invitation Cleanup Script

A robust, Selenium-based automation script to withdraw all pending LinkedIn invitations. Designed with explicit waits, modular structure, and comprehensive error handling to ensure stability and reliability across Chrome and Edge browsers.

---

## ⚙️ Features

- ✅ Automates withdrawal of sent LinkedIn invitations
- ✅ Explicit wait handling to avoid flakiness
- ✅ Cross-browser compatibility (Chrome & Edge)
- ✅ Modular functions for easy maintenance
- ✅ Graceful error handling with clear logs

---

## 🧰 Requirements

- Python 3.7+
- Google Chrome or Microsoft Edge
- ChromeDriver / EdgeDriver installed and added to PATH

### Python Dependencies
Install via pip:

```bash
pip install -r requirements.txt

🛡️ Best Practices
- 💡 Use explicit waits WebDriverWait instead of hard sleeps for robustness.
- 🚫 Avoid hardcoded XPaths; use stable selectors when possible.
- 🧪 Test regularly as LinkedIn’s DOM may change.
- 🔄 Modularize helpers to reuse and scale your automation.

🤝 Contributing
PRs are welcome! Please follow standard formatting conventions and include docstrings. For major changes, open an issue first to discuss what you’d like to change.

📄 License
This project is licensed under the MIT License. See LICENSE for details.

---
