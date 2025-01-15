from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

# Initialize Console
console = Console(record=True, width=110)

# Expertise Tree
tree = Tree("🤓 [link=https://talhaouy.me]Mhammed Talhaouy", guide_style="bold cyan")
expertise_tree = tree.add("💻 Software Engineer | Web3 Enthusiast", guide_style="bold green")
expertise_tree.add("🐘 PHP | Rust | Python | Js | Solidity")
expertise_tree.add("🚀 Laravel | Node.js | Vue.js")
expertise_tree.add("🧠 LangChain | PyTorch | Pandas | NumPy")
expertise_tree.add("☁️ AWS | CI/CD Pipelines | Nginx")
expertise_tree.add("📦 MySQL | Docker | Redis")
tree.add("🧹 Clean Coder | 🕵️ Auditor")

# About Panel
about_content = """
I enjoy creating tools that break things to make systems stronger, but never break what helps build — that's just unfair.
🌟 [green]Follow me on Twitter: [bold link=https://twitter.com/tal7aouy]@tal7aouy[/]
"""

about_panel = Panel.fit(
    about_content,
    box=box.DOUBLE,
    border_style="blue",
    title="[b]👋 Welcome",
    width=60,
)

# Display Content
console.print(Columns([about_panel, tree]))

# Save Output as HTML
CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
