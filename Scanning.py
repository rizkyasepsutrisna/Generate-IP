import os
import asyncio
import aiohttp
from colorama import Fore, Style, init

init(autoreset=True)

BATCH_SIZE = 10000  # Number of IPs per batch

# Check a single IP
async def check_url(session, url):
    try:
        async with session.get(url, timeout=5, ssl=False) as resp:
            if resp.status == 200:
                print(Fore.GREEN + f"[200 OK] {url}")
                return url
            else:
                print(Fore.RED + f"[{resp.status}] {url}")
    except asyncio.TimeoutError:
        print(Fore.YELLOW + f"[TIMEOUT] {url}")
    except aiohttp.ClientError as e:
        print(Fore.YELLOW + f"[ERROR] {url} -> {e}")
    except Exception as e:
        print(Fore.YELLOW + f"[UNKNOWN ERROR] {url} -> {e}")
    return None

# Load all IPs from folder
def load_urls_from_folder(folder_path):
    urls = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), "r") as f:
                for line in f:
                    url = line.strip()  # Keep as HTTP
                    if url:
                        urls.append(url)
    return urls

# Save successful IPs to file
def save_success(urls, output_file="success.txt"):
    with open(output_file, "a") as f:
        for url in urls:
            f.write(url + "\n")
    print(Fore.CYAN + f"\n✅ Batch finished → {len(urls)} IPs saved to {output_file}")

# Process one batch of IPs
async def process_batch(session, urls):
    tasks = [check_url(session, url) for url in urls]
    success = []
    for future in asyncio.as_completed(tasks):
        result = await future
        if result:
            success.append(result)
    return success

# Main async executor
async def main_async(folder_path):
    print(Fore.YELLOW + f"\n🚀 Loading all IPs from folder: {folder_path}...")
    urls = load_urls_from_folder(folder_path)
    print(Fore.YELLOW + f"🔢 Total targets: {len(urls)} IPs\n")

    connector = aiohttp.TCPConnector(limit=500)

    async with aiohttp.ClientSession(connector=connector) as session:
        total = len(urls)
        for i in range(0, total, BATCH_SIZE):
            batch = urls[i:i + BATCH_SIZE]
            print(Fore.CYAN + f"\n🧪 Processing batch {i // BATCH_SIZE + 1} ({len(batch)} IPs)...")
            success = await process_batch(session, batch)
            save_success(success)

# Entry point
if __name__ == "__main__":
    os.system("clear")
    print(Fore.GREEN + Style.BRIGHT + r"""
███████╗ █████╗ ██╗███╗   ██╗     ██████╗ ███████╗██╗    ██╗
╚══███╔╝██╔══██╗██║████╗  ██║    ██╔══██╗██╔════╝██║    ██║
  ███╔╝ ███████║██║██╔██╗ ██║    ██████╔╝█████╗  ██║ █╗ ██║
 ███╔╝  ██╔══██║██║██║╚██╗██║    ██╔═══╝ ██╔══╝  ██║███╗██║
███████╗██║  ██║██║██║ ╚████║    ██║     ███████╗╚███╔███╔╝
╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚══════╝ ╚══╝╚══╝
""")
    folder = input(Fore.CYAN + "📂 Enter IP folder name (e.g., ip_chunks_18): ").strip()

    if not os.path.exists(folder):
        print(Fore.RED + "❌ Folder not found.")
    else:
        asyncio.run(main_async(folder))
