from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"success": "green", "error": "bold red"})

console = Console(theme=custom_theme)

console.print("Operation successful!", style="success")
console.print("Operation failed!", style="error")
console.print("Operation [error]failed![/error]")

# Emoji
console.print(":thumbs_up: File downloaded!")
console.print(":apple: :bug: ")
