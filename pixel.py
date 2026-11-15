#!/usr/bin/env python3
"""Neurotech pixel banner for Awesome Craft Neuro. Original scene, no brand marks."""
import random
from pathlib import Path

random.seed(23)
P = 8
W = 100
H = 34  # 800x272
out = []


def r(x, y, w, h, c, cls=None, extra=""):
    a = f' class="{cls}"' if cls else ""
    out.append(
        f'<rect x="{x*P}" y="{y*P}" width="{w*P}" height="{h*P}" fill="{c}"{a}{extra}/>'
    )


# 3x5 pixel font
F = {
    "A": ["010", "101", "111", "101", "101"],
    "C": ["011", "100", "100", "100", "011"],
    "E": ["111", "100", "110", "100", "111"],
    "F": ["111", "100", "110", "100", "100"],
    "N": ["101", "111", "111", "101", "101"],
    "O": ["010", "101", "101", "101", "010"],
    "R": ["110", "101", "110", "101", "101"],
    "T": ["111", "010", "010", "010", "010"],
    "U": ["101", "101", "101", "101", "010"],
    " ": ["000", "000", "000", "000", "000"],
}

style = """
<style>
.tw{animation:tw 2.4s steps(2) infinite}
.tw2{animation:tw 3.1s steps(2) infinite .8s}
.tw3{animation:tw 1.9s steps(2) infinite 1.4s}
@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}
.glow{animation:glow 1.4s steps(3) infinite}
.glow2{animation:glow 1.8s steps(3) infinite .5s}
.glow3{animation:glow 2.2s steps(3) infinite 1s}
@keyframes glow{0%,100%{opacity:.35}50%{opacity:1}}
.blink{animation:tw 1s steps(1) infinite}
.led{animation:led 1.2s steps(2) infinite}
.led2{animation:led 1.6s steps(2) infinite .4s}
.led3{animation:led .9s steps(2) infinite .2s}
@keyframes led{0%,100%{opacity:1}50%{opacity:.2}}
.wave{animation:wave 1.6s steps(8) infinite}
.wave2{animation:wave 1.8s steps(8) infinite .2s}
.wave3{animation:wave 1.4s steps(8) infinite .4s}
@keyframes wave{0%,100%{opacity:.25}50%{opacity:1}}
.pulse{animation:pulse 1.6s ease-in-out infinite}
.pulse2{animation:pulse 1.8s ease-in-out infinite .4s}
.pulse3{animation:pulse 2s ease-in-out infinite .8s}
@keyframes pulse{0%,100%{opacity:.3}50%{opacity:1}}
.scan{animation:scan 3.2s linear infinite}
@keyframes scan{0%{opacity:0;transform:translateY(0)}15%{opacity:1}85%{opacity:1}100%{opacity:0;transform:translateY(56px)}}
</style>
"""

# Deep lab night sky
sky = ["#070714", "#0b0b1f", "#10102c", "#141438", "#181844", "#1c1c50", "#20205c"]
for i, c in enumerate(sky):
    r(0, i * 4, W, 4, c)

# Sparse stars, keep the title band clear
for i in range(24):
    while True:
        x = random.randrange(W)
        y = random.randrange(10)
        if not (26 <= x <= 74 and y <= 8):
            break
    r(x, y, 1, 1, random.choice(["#a5b4fc", "#fce7f3", "#c4b5fd", "#e0e7ff"]), random.choice(["tw", "tw2", "tw3"]))

# Title: CRAFT NEURO
t = "CRAFT NEURO"
tx = (W - len(t) * 4) // 2
ty = 2
for k, ch in enumerate(t):
    for yy, row in enumerate(F[ch]):
        for xx, b in enumerate(row):
            if b == "1":
                r(tx + k * 4 + xx + 0.25, ty + yy + 0.25, 1, 1, "#000", None, ' opacity=".55"')
                r(tx + k * 4 + xx, ty + yy, 1, 1, "#c4b5fd")

# --- Left: generic head with EEG electrodes (not a product copy) ---
# neck / shoulders
r(8, 24, 14, 2, "#1e1b4b")
r(10, 23, 10, 1, "#312e81")
# head profile (simple oval)
for hx, hy, hw, hh, col in [
    (11, 14, 8, 9, "#f1c27d"),
    (12, 13, 6, 1, "#f1c27d"),
    (12, 23, 6, 1, "#e0a868"),
    (10, 16, 1, 5, "#f1c27d"),
    (19, 16, 1, 5, "#e0a868"),
]:
    r(hx, hy, hw, hh, col)
# hair / cap band
r(11, 14, 8, 2, "#312e81")
r(12, 13, 6, 1, "#1e1b4b")
r(11, 16, 8, 1, "#4338ca")
# eye
r(17, 18, 1, 1, "#0f172a")
# electrode dots on the cap (blinking)
electrodes = [(12, 14, "led"), (14, 13, "led2"), (16, 13, "led3"), (18, 14, "led"), (13, 16, "led2"), (17, 16, "led3")]
for x, y, cls in electrodes:
    r(x, y, 1, 1, "#22d3ee", cls)
# cable down to the amp
for y in range(17, 26):
    r(10, y, 1, 1, "#64748b" if y % 2 == 0 else "#475569")

# Generic amplifier / acquisition box under the head
r(4, 26, 12, 4, "#1e293b")
r(4, 26, 12, 1, "#334155")
r(5, 27, 2, 1, "#22c55e", "led")
r(8, 27, 2, 1, "#38bdf8", "led2")
r(11, 27, 2, 1, "#a78bfa", "led3")
r(6, 29, 8, 1, "#0f172a")

# --- Center: monitor with animated EEG traces ---
# desk
r(32, 25, 28, 1, "#334155")
r(33, 26, 26, 1, "#1e293b")
# bezel
r(34, 11, 24, 14, "#0f172a")
r(34, 11, 24, 1, "#475569")
r(34, 11, 1, 14, "#334155")
r(57, 11, 1, 14, "#020617")
r(34, 24, 24, 1, "#1e293b")
# stand
r(44, 25, 4, 1, "#475569")
r(45, 25, 2, 2, "#334155")
# screen
r(36, 13, 20, 10, "#042f2e")
r(36, 13, 20, 1, "#134e4a")
r(37, 13, 3, 1, "#2dd4bf", "glow")
# scan line
out.append(
    f'<rect x="{36*P}" y="{14*P}" width="{20*P}" height="{P}" fill="#5eead4" opacity=".35" class="scan"/>'
)

# Three EEG traces as pixel polylines with wave animation
traces = [
    # (points as (x, y) on screen), class, color
    (
        [(37, 16), (39, 15), (41, 17), (43, 15), (45, 16), (47, 14), (49, 17), (51, 15), (53, 16), (55, 15)],
        "wave",
        "#5eead4",
    ),
    (
        [(37, 19), (39, 19), (41, 18), (43, 20), (45, 17), (47, 19), (49, 18), (51, 20), (53, 19), (55, 18)],
        "wave2",
        "#a5b4fc",
    ),
    (
        [(37, 22), (39, 21), (41, 22), (43, 21), (45, 22), (47, 20), (49, 22), (51, 21), (53, 22), (55, 21)],
        "wave3",
        "#f9a8d4",
    ),
]
for points, cls, col in traces:
    for i, (x, y) in enumerate(points):
        if i:
            px, py = points[i - 1]
            y1, y2 = sorted((py, y))
            for yy in range(y1, y2 + 1):
                r(x if yy == y else px, yy, 1, 1, col, cls)
        r(x, y, 1, 1, "#ecfeff" if i == len(points) - 1 else col, cls if i < len(points) - 1 else "glow")

# Small operator to the right of the stand
r(60, 20, 2, 2, "#f1c27d")
r(61, 21, 1, 1, "#0f172a")
r(60, 22, 2, 3, "#4c1d95")
r(60, 25, 1, 1, "#111827")
r(61, 25, 1, 1, "#111827")

# --- Right: connected neurons with pulsing synapses ---
# soma 1
r(76, 14, 3, 3, "#ddd6fe", "pulse")
r(77, 15, 1, 1, "#f5f3ff", "glow")
# soma 2
r(88, 16, 3, 3, "#c4b5fd", "pulse2")
r(89, 17, 1, 1, "#f5f3ff", "glow2")
# soma 3
r(80, 21, 3, 3, "#a78bfa", "pulse3")
r(81, 22, 1, 1, "#f5f3ff", "glow3")
# dendrites / axons as stepped pixels
for x, y, c, cls in [
    (75, 15, "#818cf8", "pulse"),
    (74, 16, "#818cf8", "pulse"),
    (79, 15, "#818cf8", "pulse"),
    (80, 16, "#818cf8", "glow"),
    (81, 16, "#a5b4fc", "glow"),
    (82, 16, "#a5b4fc", "pulse2"),
    (83, 16, "#c4b5fd", "pulse2"),
    (84, 16, "#c4b5fd", "glow2"),
    (85, 16, "#ddd6fe", "glow2"),
    (86, 17, "#ddd6fe", "pulse2"),
    (87, 17, "#c4b5fd", "pulse2"),
    (77, 17, "#818cf8", "pulse"),
    (78, 18, "#818cf8", "glow3"),
    (79, 19, "#a78bfa", "glow3"),
    (80, 20, "#a78bfa", "pulse3"),
    (83, 22, "#a78bfa", "pulse3"),
    (84, 21, "#c4b5fd", "glow"),
    (85, 20, "#c4b5fd", "pulse2"),
    (86, 19, "#ddd6fe", "pulse2"),
    (87, 19, "#ddd6fe", "glow2"),
    (89, 19, "#c4b5fd", "pulse2"),
    (90, 20, "#a78bfa", "pulse3"),
    (91, 15, "#c4b5fd", "pulse2"),
    (92, 14, "#ddd6fe", "glow2"),
    (75, 13, "#a5b4fc", "pulse"),
    (76, 12, "#c4b5fd", "glow"),
]:
    r(x, y, 1, 1, c, cls)

# Floor / lab grate
for x in range(W):
    r(x, 30, 1, 1, "#312e81" if x % 4 == 0 else "#1e1b4b")
    r(x, 31, 1, 1, "#0f172a" if x % 2 else "#1e1b4b")
    for y in range(32, H - 2):
        r(x, y, 1, 1, "#0b1220" if (x + y) % 4 else "#1e1b4b")

# Status bar
out.append(
    f'<text x="{8}" y="{H*P-8}" font-family="monospace" font-size="12" fill="#c4b5fd">'
    f"&gt; reading open-source neural signals"
    f'<tspan class="blink">_</tspan></text>'
)

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W*P} {H*P}" '
    f'width="{W*P}" height="{H*P}" shape-rendering="crispEdges">'
    + style
    + "".join(out)
    + "</svg>"
)

dest = Path(__file__).resolve().parent / "assets" / "craft-neuro.svg"
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(svg)
print(f"wrote {dest} ({dest.stat().st_size} bytes)")
