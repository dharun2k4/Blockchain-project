

📄 Blockchain-based Document Verification System

🔗 Overview

This project is a Blockchain-based Document Verification System built with Python.
It ensures that important documents like certificates, contracts, and ID proofs are tamper-proof and verifiable.

Each document is converted into a SHA-256 hash and stored inside the blockchain.
Later, when verifying, the document is re-hashed and compared with blockchain records.
If even a single character changes, the verification fails.


---

⚡ Features

✅ Store document hashes securely on a blockchain

✅ Verify authenticity of documents

✅ Detect tampering instantly

✅ Simple Python implementation

✅ Extendable into a web app with Flask/Django



---

🏗 Workflow

1. 📥 Upload Document → System generates SHA-256 hash


2. 🔗 Store on Blockchain → Save the hash in a block


3. 🔍 Verify Document → Re-hash uploaded file and compare


4. ❌ Tamper Detection → If changed, verification fails






🖥 Tech Stack

Language: Python 3

Libraries: hashlib, time, os

Concepts: Blockchain, Cryptographic Hashing (SHA-256)





⚙ Installation & Usage

# Clone this repository
git clone https://github.com/your-username/document-verification-blockchain.git

# Navigate to project folder
cd document-verification-blockchain

# Run the program
python blockchain_verification.py


---

▶ Example Output

Document1 valid? True
Tampered Document valid? False




📊 Future Enhancements

🌐 Flask/Django web app with file upload

📱 QR code for instant document verification

☁ Store blockchain on distributed servers (IPFS/Cloud)

🔑 User authentication for issuing authorities




🤝 Contributors
Ahmed Sirajudeen - 220071601021
Dharun Suvadhagan- 220071601053




