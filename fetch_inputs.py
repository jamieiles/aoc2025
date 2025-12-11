# /// script
# dependencies = [
#   "aocd",
# ]
# ///
#!/usr/bin/env python3
from aocd import get_data
from datetime import datetime
from pathlib import Path
import os

os.makedirs('data', exist_ok=True)

for day in range(1, 13):
    try:
        with open(Path('data') / f'day{day}.txt', 'w') as f:
            f.write(get_data(day=day, year=2025))
    except Exception as e:
        break
