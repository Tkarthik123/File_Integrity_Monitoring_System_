📁 File Integrity Monitoring System

📌 Overview

The File Integrity Monitoring System (FIMS) is a Python-based tool that continuously monitors specified directories for changes such as file creations, modifications, and deletions. It maintains a log of all detected changes in an SQLite database and can optionally send email notifications to administrators.

🚀 Features

✅ Real-time Monitoring – Detects file changes (create, modify, delete) in a directory.✅ Hash Verification – Uses SHA-256 to track file integrity.✅ Logging & Database Storage – Stores all changes in an SQLite database.✅ Email Alerts – Sends notifications when unauthorized changes are detected.✅ Cross-Platform – Works on Windows, Linux, and macOS.

⚙️ Installation

1️⃣ Prerequisites

Ensure you have Python 3.12+ installed.

2️⃣ Clone the Repository

git clone https://github.com/your-username/File-Integrity-Monitoring-System.git
cd File-Integrity-Monitoring-System

3️⃣ Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4️⃣ Install Dependencies

pip install -r requirements.txt

🛠️ Usage

1️⃣ Run the Monitor Script

python monitor.py

This will start monitoring the configured directory.

Any file changes will be logged and stored in the database.

2️⃣ View Logged Events

python log_viewer.py

This script will display all recorded file events from the database.

3️⃣ Test the System

Run the test suite to ensure everything is working correctly:

python -m unittest test_monitor.py

🖥️ Project Structure

📂 File-Integrity-Monitoring-System
│── monitor.py           # Main script for monitoring files
│── log_viewer.py        # Displays logs from the SQLite database
│── test_monitor.py      # Unit tests for integrity checks
│── requirements.txt     # Dependencies list
│── README.md            # Documentation
│── file_logs.db         # SQLite database storing file events
🔹 monitored_folder/    # Folder being monitored for changes

📩 Email Notifications (Optional)

To enable email alerts for unauthorized file changes:1️⃣ Open monitor.py and configure SMTP settings.2️⃣ Replace "your-email@gmail.com" and "your-password" with valid credentials.3️⃣ Ensure less secure apps access is enabled in your email provider.

🛡️ Security Considerations

Ensure monitored files have proper access control.

Use secure email credentials (consider using OAuth instead of plain-text passwords).

Regularly review logs to detect anomalies.

🌆 Future Enhancements

🔹 Web dashboard for visualizing logs.🔹 Multi-folder monitoring.🔹 Integration with cloud storage for backup.

🤝 Contributing

Pull requests are welcome! Feel free to contribute improvements or report issues.

📄 License

This project is open-source and available under the MIT License.

📥 Contact

📧 Email: tavatarikarthik034@example.com
