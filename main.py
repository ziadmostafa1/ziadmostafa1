from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=120)

tree = Tree("🤓 [link=https://ziadai.me]Ziad Mostafa", guide_style="bold cyan")

data_science_tree = tree.add("👨🏻‍🔬 Data Scientist")
data_science_tree.add("[link=https://github.com/ziadmostafa1]GitHub Repositories")
data_science_tree.add("[link=https://huggingface.co/ziadmostafa]Hugging Face 🤗")


github_tree = tree.add("👨🏻‍💻 Open Source Contributor")
github_tree.add("[link=https://ziadai.me/FaceAgingGAN]Facial Age Transformation with CycleGAN")
github_tree.add("[link=https://ziadai.me/Fake_News_Detection_with_RNN_and_LSTM]Fake News Detection with RNN & LSTM")
github_tree.add("[link=https://ziadai.me/Hands_Sign]Real-time Sign Language Recognition")
github_tree.add("[link=https://ziadai.me/Fire_and_Smoke_Detection_with_YOLOv8]Fire and Smoke Detection with YOLOv8")
github_tree.add("[link=https://ziadai.me/Egyptian_Hieroglyphs]Egyptian Hieroglyph Classification")
github_tree.add("[link=https://ziadai.me/Movie_Recommendation_System]Movie Recommendation System")

blog_tree = tree.add("📚 Blog Writer")
blog_tree.add("📜 [link=https://ziadai.me/post/how-to-create-a-blog-in-2025]How to Create a Blog in 2025")

about = """\
I'm a Data Scientist specializing in NLP and Computer Vision, living in [link=https://www.google.com/maps/place/Banha,+Qism+Banha,+Banha,+Al-Qalyubia+Governorate/@30.4589172,31.1884216,14z]Benha[/], Egypt. Passionate about building intelligent systems that make a difference. I love working on open-source projects, contributing to AI research, and sharing knowledge through writing and mentoring.

Follow me on [bold link=https://x.com/ZiadMostaf_a]Twitter[/] and [bold link=https://www.linkedin.com/in/ziadmostafa]LinkedIn[/]. 

Feel free to ask me anything!"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi 👋 I'm Ziad", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)