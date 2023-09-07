import time
from rich.console import Console
console = Console()

for i in range(10):
    console.log(f"Doing important stuff... {i}")
    time.sleep(0.2)
