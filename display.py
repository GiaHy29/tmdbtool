from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from datetime import datetime

console = Console()

def print_movies_table(movies):
    table = Table(
        title="[bold underline yellow]🔥 DANH SÁCH PHIM NỔI BẬT 🔥[/bold underline yellow]",
        title_justify="center",
        border_style="bright_magenta",
        show_lines=True,
        pad_edge=True,
    )

    table.add_column("STT", style="bold cyan", justify="right", no_wrap=True)
    table.add_column("Tên phim", style="bold magenta")
    table.add_column("Ngày ra mắt", style="bold green", justify="center", no_wrap=True)
    table.add_column("Điểm đánh giá", style="yellow", justify="center", no_wrap=True)
    table.add_column("lượt vote", style="yellow", justify="center", no_wrap=True)

    for idx, movie in enumerate(movies, 1):
        title = Text(movie.get('title', 'N/A'), style="italic bright_white")
        release_date = format_date(movie.get('release_date', 'N/A'))
        vote = str(movie.get('vote_average', 'N/A'))
        vote_count = str(movie.get('vote_count', 'N/A'))
        style = get_vote_style(vote)
        table.add_row(
            str(idx),
            title,
            release_date,
            Text(vote, style=style, justify="center"),
            Text(vote_count, style="yellow", justify="center")
        )

    console.print(table)

def print_error(message):
    console.print(f"[bold red]{message}[/bold red]")

def format_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%d/%m/%Y")
    except Exception:
        return date_str or "N/A"

def get_vote_style(vote):
    try:
        vote = float(vote)
        if vote >= 8:
            return "bold green"
        elif vote >= 5:
            return "bold yellow"
        else:
            return "bold red"
    except:
        return ""

def show_movie_overview(movies):
    while True:
        choice = console.input("\nNhập số phim để xem tóm tắt (0 để thoát): ")
        if not choice.isdigit():
            console.print("[red]Vui lòng nhập số hợp lệ![/red]")
            continue
        choice = int(choice)
        if choice == 0:
            break
        if 1 <= choice <= len(movies):
            movie = movies[choice-1]
            overview = movie.get('overview', 'Không có tóm tắt.')
            panel = Panel.fit(overview, title=movie.get('title', 'Phim'), border_style="green")
            console.print(panel)
        else:
            console.print(f"[red]Số nhập ngoài phạm vi 1-{len(movies)}[/red]")
