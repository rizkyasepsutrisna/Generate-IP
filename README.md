# IP Range Scanner

This project consists of two Python scripts:

1. **Generate_IP** – Generates a list of IP addresses in a given range and saves them to `.txt` files per batch (max 8 MB each).
2. **Scanning** – Scans each IP (HTTP) to check if the response has a **status code 200**.

## 📂 Project Structure

```
.
├── Generate_IP.py        # Script to generate IP addresses
├── Scanning.py           # Script to scan IP addresses
├── requirements.txt      # Dependency list
├── README.md             # Project documentation
└── ip_chunks_xx/         # Output folder from Generate_IP (xx = IP prefix)
```

---

## 📦 Installation

Make sure Python 3.8+ is installed, then install dependencies:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
aiohttp
colorama
```

---

## 🚀 Usage

### 1. Generate IP List
Run `Generate_IP.py` to create files containing IP addresses based on the prefix you provide.

```bash
python Generate_IP.py
```

**Example input:**
```
Enter IP prefix (1–223): 18
```

The result will be saved in a folder:
```
ip_chunks_18/
```
The files inside will contain lines like:
```
http://18.0.0.1:80
http://18.0.0.2:80
...
```

---

### 2. Scan IPs
After generating the IP list, run `Scanning.py` to check for HTTP status code 200.

```bash
python Scanning.py
```

**Example input:**
```
📂 Enter IP folder name (e.g., ip_chunks_18): ip_chunks_18
```

The script will:
- Show the status of each IP (`200 OK`, other codes, or errors)
- Save IPs with **status code 200** to `success.txt`

---

## ⚙️ Configuration
Key variables in `Scanning.py`:
- `BATCH_SIZE` → Number of IPs per batch (default 10,000)
- Request timeout: 5 seconds
- Only IPs with status **200 OK** are saved

---

## ⚠️ Disclaimer
This script is for **legal purposes only**, such as:
- Internal network testing
- Security auditing of systems you own or have permission to test

Scanning public networks without permission is **illegal** in many countries.

---

## ☕ Buy Me a Coffee
If you like this project and want to support me:

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://saweria.co/zainpewpewpew)

---

## 📜 License
MIT License © 2025
