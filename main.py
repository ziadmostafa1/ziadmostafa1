from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=120)

tree = Tree("🚀 [link=https://ziadai.me]Ziad Mostafa", guide_style="bold cyan")

data_science_tree = tree.add("📊 Data Scientist")
data_science_tree.add("🔹 [link=https://github.com/ziadmostafa]GitHub Repositories ")
data_science_tree.add("🔹 [link=https://huggingface.co/ziadmostafa]Hugging Face 🤗")


github_tree = tree.add("🧑‍💻 Open Source Contributor")
github_tree.add("[bold]Facial Age Transformation with CycleGAN[/bold] [link=https://github.com/ziadmostafa1/FaceAgingGAN]")
github_tree.add("[bold]Fake News Detection with RNN & LSTM[/bold] [link=https://github.com/ziadmostafa1/Fake_News_Detection_with_RNN_and_LSTM]")
github_tree.add("[bold]Real-time Sign Language Recognition[/bold] [link=https://github.com/ziadmostafa1/CV-Sections-Tasks/tree/main/Task3/Hands%20Sign]")
github_tree.add("[bold]Fire and Smoke Detection with YOLOv8[/bold] [link=https://github.com/ziadmostafa1/CV-Sections-Tasks/tree/main/Task4]")
github_tree.add("[bold]Egyptian Hieroglyph Classification[/bold] [link=https://github.com/ziadmostafa1/CV-Sections-Tasks/tree/main/Task2/Egyptian%20Hieroglyphs]")
github_tree.add("[bold]Movie Recommendation System[/bold] [link=https://github.com/ziadmostafa1/Movie-Recommendation-System]")

blog_tree = tree.add("📚 Blog Writer")
blog_tree.add("📜 [link=https://ziadai.me/post/how-to-create-a-blog-in-2025]How to Create a Blog in 2025")

about = """\
I'm a Data Scientist specializing in NLP and Computer Vision, living in [link=https://maps.app.goo.gl/jX75Vtr6Qov5htL29]Benha, Egypt[/]. Passionate about building intelligent systems that make a difference. I love working on open-source projects, contributing to AI research, and sharing knowledge through writing and mentoring.

Visit my website [bold link=https://ziadai.me]ziadai.me[/] and follow me on [bold link=https://www.linkedin.com/in/ziadmostafa]LinkedIn[/].

Let's connect and talk AI!"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi 👋 I'm Ziad", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)