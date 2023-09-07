from rich.console import Console
from rich.traceback import install
install()


def add(x, y):
    console.log("Adding two numbers.", log_locals=True)
    return x + y


console = Console(record=True)


try:
    add(1, 2)
    add(1, 3)
    add(1, "a")
except TypeError:
    console.print_exception()

console.save_html("demo.html")
