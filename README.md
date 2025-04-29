📄 Project Description:
This project demonstrates a secure and production-friendly approach to handling database passwords in Python applications.

It includes:
● 🔐 Password encryption using Fernet (symmetric encryption)
● 🛡 Safe decryption at runtime with protection against accidental leaks (print/log masking)
● ⚙️ Actual MySQL database connection using the decrypted password
● 📁 Clean modular code organization for real-world project structure

🧱 Tech Stack:
● Language: Python 3
● Database: MySQL

● Libraries:
○ cryptography – for encryption and decryption
○ mysql-connector-python – to connect to MySQL from Python

Feature Description
Encryption-Password is encrypted using a randomly generated 32-byte Fernet key
Key Management-The key is generated once and stored in a local file secret.key
Secure Decryption-Password is decrypted only at runtime using the key
Print-Safe Strings-Decrypted password uses a custom FakeStr class to prevent print/log leaks
MySQL Integration-Connects to a MySQL database using the decrypted password

Real-World Use Case:
This setup mimics what developers and data engineers should follow when building
internal tools, automation scripts, or backend jobs that involve sensitive credentials like:
● MySQL / PostgreSQL DBs
● Cloud storage credentials
● Secure API keys
By avoiding plaintext passwords, the project improves security and follows DevSecOps
best practices.

