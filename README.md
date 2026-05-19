# 🛡️ CyberVault Pro: Tamper-Proof Evidence Archival Engine

A secure, forensic-grade digital archiving tool built during the hackathon to protect victims of cyberbullying and online harassment. CyberVault Pro transforms volatile screenshots into legally credible, tamper-proof evidence packets.

---

## 🎯 The Problem We Solve
Standard digital screenshots are frequently rejected by legal entities or police departments because they can be easily manipulated or doctored using editing software. CyberVault Pro solves this by instantly creating an immutable, cryptographically sealed record of the crime scene the exact millisecond it is reported.

---

## ✨ Key Features
*   **Cryptographic Hashing:** Instantly computes a unique **SHA-256 digital fingerprint** of the evidence screenshot to prevent any post-upload alteration.
*   **Immutable Timeline:** Hardcodes an exact system **Time Log** and references the source URL location to establish a valid chain of custody.
*   **Automated Court-Ready Reports:** Generates a professional, downloadable **Legal Incident Report (PDF)** compiling the evidence image, forensic telemetry, and metadata.
*   **Elegant Zero-Code UI:** Utilizes a highly intuitive, responsive two-column interface powered entirely by Python scripts.

---

## 🛠️ Tech Stack
*   **Frontend & Backend Interface:** [Gradio](https://github.com)
*   **Programming Language:** Python 3
*   **Cryptographic Verification:** Native Python `hashlib` (SHA-256)
*   **Document Generation:** `ReportLab` engine

---

## 🚀 How to Run Locally

### 1. Prerequisites
Ensure you have Python installed on your computer. Open your terminal inside VS Code and clone or set up your directory.

### 2. Install Dependencies
Run the following command to install the required library ecosystem:
```bash
pip install gradio reportlab python-dotenv
```

### 3. Execution
Launch the local development server by running:
```bash
python app.py
```
Open your browser and navigate to the local network port address displayed in your terminal (typically `http://127.0.0.1:8501`).

---

## 🔮 Future Roadmap
1. **Direct Cyber Cell Pipeline:** Direct automated API submission pipelines to official national cyber reporting portals.
2. **Blockchain Verification:** Archiving SHA-256 signatures onto a decentralized ledger to create absolute public proof of existence.
3. **AI Threat Mapping:** Automated extraction of textual evidence mapping directly to specific Indian Penal Statutes (BNS / IT Act).
