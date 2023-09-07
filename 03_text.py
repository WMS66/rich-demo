from rich.console import Console
from rich.text import Text
console = Console()

console.print("This is some text.", style="bold underline green")
console.print("[bold]This [cyan]is[/] some text.[/]")

text = Text("Hello, World!")
text.stylize("bold magenta", 0, 6)

console.print(text)
