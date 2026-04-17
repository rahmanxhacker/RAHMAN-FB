#!/usr/bin/env python3
# ╔══════════════════════════════════════════╗
# ║   𓆩᪳Ξ𝐑𝐀𝐇𝐌𝐀𝐍 𝐇𝐀𝐂𝐊𝐄𝐑𓆪 ː͢» PREMIUM TOOL   ║
# ╚══════════════════════════════════════════╝

import openpyxl
import re
import os
from datetime import datetime

# ===== COLORS =====
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[1;97m"
P = "\033[1;35m"

# ===== BANNER =====
def banner():
    os.system("clear")
    print(C + "╔" + "═"*52 + "╗")
    print(C + "║" + W + "      XLSX NUMBER EXTRACTOR TOOL        " + C + "║")
    print(C + "║" + G + "   Dev: 𓆩᪳Ξ𝐑𝐀𝐇𝐌𝐀𝐍 𝐇𝐀𝐂𝐊𝐄𝐑𓆪 ː͢»       " + C + "║")
    print(C + "╚" + "═"*52 + "╝")
    print(Y + f"[•] Date: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")
    print(C + "━"*54)

    print(Y + "[+] Default Input  : /sdcard/file.xlsx")
    print(Y + "[+] Default Output : /sdcard/file.txt")
    print(C + "━"*54)

# ===== EXTRACT FUNCTION =====
def extract_nums(file_path):
    try:
        wb = openpyxl.load_workbook(file_path, data_only=True)
        data = (str(c) for r in wb.active.iter_rows(values_only=True) for c in r if c)

        nums = {re.sub(r'\D', '', s) for s in data}
        clean = [n for n in nums if 7 <= len(n) <= 15]

        return sorted(clean)

    except Exception as e:
        print(R + f"[!] Error: {e}")
        return []

# ===== MAIN =====
def main():
    banner()

    inp = input(W + "[>] Enter XLSX Path: ")
    out = input(W + "[>] Enter TXT Output Path: ")

    if not os.path.exists(inp):
        print(R + "[!] File not found!")
        return

    print(C + "\n[•] Processing... Please wait\n")

    numbers = extract_nums(inp)

    if numbers:
        with open(out, "w") as f:
            f.write("\n".join(numbers) + "\n")

        print(G + "━"*54)
        print(G + f"[√] Successfully Converted {len(numbers)} Numbers!")
        print(G + f"[√] Saved to: {out}")
        print(G + "━"*54)
    else:
        print(R + "[!] No numbers found or File Error!")

    footer()

# ===== FOOTER =====
def footer():
    print(P + "\n" + "═"*54)
    print(W + "   Developer: 𓆩᪳Ξ𝐑𝐀𝐇𝐌𝐀𝐍 𝐇𝐀𝐂𝐊𝐄𝐑𓆪 ː͢»")
    print(C + "   Premium Python Tool | 2026")
    print(P + "═"*54)

# ===== RUN =====
if __name__ == "__main__":
    main()