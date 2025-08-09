import os
import time
import random
import sys

# ANSI color codes
G = '\033[92m'  # Green
Y = '\033[93m'  # Yellow
R = '\033[91m'  # Red
C = '\033[96m'  # Cyan
W = '\033[0m'   # Reset color

def slow_print(text, delay=0.02):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def ip_to_int(ip):
    parts = list(map(int, ip.split('.')))
    return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

def int_to_ip(n):
    return f"{(n >> 24) & 0xFF}.{(n >> 16) & 0xFF}.{(n >> 8) & 0xFF}.{n & 0xFF}"

def generate_ip_files(prefix, max_size_mb=8):
    start_ip = f"{prefix}.0.0.1"
    end_ip = f"{prefix}.255.255.255"

    start_int = ip_to_int(start_ip)
    end_int = ip_to_int(end_ip)

    output_dir = f"ip_chunks_{prefix}"
    os.makedirs(output_dir, exist_ok=True)

    max_size = max_size_mb * 1024 * 1024  # 8 MB
    file_index = 1
    current_file_path = os.path.join(output_dir, f"ips_{file_index}.txt")
    current_file = open(current_file_path, "w")
    current_size = 0

    total = end_int - start_int + 1
    printed = 0

    for ip_int in range(start_int, end_int + 1):
        ip_str = int_to_ip(ip_int)
        formatted_ip = f"http://{ip_str}:80\n"
        encoded = formatted_ip.encode("utf-8")
        line_size = len(encoded)

        if current_size + line_size > max_size:
            current_file.close()
            file_index += 1
            current_file_path = os.path.join(output_dir, f"ips_{file_index}.txt")
            current_file = open(current_file_path, "w")
            current_size = 0

        current_file.write(formatted_ip)
        current_size += line_size

        if printed % 100000 == 0:
            print(f"{G}[+] Injecting → {formatted_ip.strip()}{W}")
        printed += 1

    current_file.close()
    slow_print(f"{Y}[✓] IPs generated and saved to folder: {output_dir}{W}", 0.01)

if __name__ == "__main__":
    slow_print(f"{C}┌─[IP Generator v1.0]─[{time.strftime('%H:%M:%S')}]─[By ZainPew]{W}", 0.01)
    time.sleep(0.5)
    slow_print(f"{Y}Initializing target network range...{W}", 0.02)
    time.sleep(1)

    while True:
        try:
            prefix = int(input(f"{R}Enter IP prefix (1–223): {W}"))
            if 1 <= prefix <= 223:
                break
            else:
                slow_print(f"{R}Invalid range. Must be between 1 and 223.{W}")
        except ValueError:
            slow_print(f"{R}Input must be a number.{W}")

    slow_print(f"{G}[*] Targeting range: {prefix}.0.0.1 to {prefix}.255.255.255{W}")
    time.sleep(1)
    slow_print(f"{G}[*] Preparing payload files (max 8MB each)...{W}")
    time.sleep(1)

    generate_ip_files(prefix)
    slow_print(f"{C}Exiting... mission complete.{W}", 0.01)
