#!/usr/bin/env python3
# ╔══════════════════════════════════════════╗
# ║   𓆩᪳Ξ𝐑𝐀𝐇𝐌𝐀𝐍 𝐇𝐀𝐂𝐊𝐄𝐑𓆪 ː͢» PREMIUM TOOL   ║
# ╚══════════════════════════════════════════╝

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
    print(C + "║" + W + "      COOKIE SEPARATOR TOOL (PREMIUM)   " + C + "║")
    print(C + "║" + G + "   Dev: 𓆩᪳Ξ𝐑𝐀𝐇𝐌𝐀𝐍 𝐇𝐀𝐂𝐄𝐊𝐄𝐑𓆪 ː͢»       " + C + "║")
    print(C + "╚" + "═"*52 + "╝")
    print(Y + f"[•] Date: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")
    print(C + "━"*54)

    print(Y + "[+] Output Files:")
    print(W + "    /sdcard/1000_ids.txt")
    print(W + "    /sdcard/615_ids.txt")
    print(W + "    /sdcard/other_ids.txt")
    print(C + "━"*54)

# ===== MAIN FUNCTION =====
def sep_cookies():
    banner()

    f = input(W + '[>] Enter File Path: ')

    if not os.path.exists(f): 
        print(R + f"[!] Error: '{f}' not found!")
        return

    print(C + "\n[•] Processing... Please wait\n")

    a, b, c = [], [], []

    for l in open(f, encoding='utf-8'):
        l = l.strip()
        if not l:
            continue

        i = l.split('|')[0]

        if i.startswith('1000'):
            a.append(l)
        elif i.startswith('615'):
            b.append(l)
        else:
            c.append(l)

    if a:
        open('/sdcard/1000_ids.txt', 'w', encoding='utf-8').write('\n'.join(a))
    if b:
        open('/sdcard/615_ids.txt', 'w', encoding='utf-8').write('\n'.join(b))
    if c:
        open('/sdcard/other_ids.txt', 'w', encoding='utf-8').write('\n'.join(c))

    print(G + "━"*54)
    print(G + "[√] Task Completed Successfully!")
    print(G + f"[√] 1000 IDs: {len(a)}")
    print(G + f"[√] 615 IDs : {len(b)}")
    print(G + f"[√] Others  : {len(c)}")
    print(G + "━"*54)

    footer()

# ===== FOOTER =====
def footer():
    print(P + "\n" + "═"*54)
    print(W + "   Developer: 𓆩᪳Ξ𝐑𝐀𝐇𝐌𝐀𝐍 𝐇𝐀𝐂𝐊𝐄𝐑𓆪 ː͢»")
    print(C + "   Premium Python Tool | 2026")
    print(P + "═"*54)

# ===== RUN =====
if __name__ == "__main__":
    sep_cookies()