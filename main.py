import argparse
from tmdb_client import TMDBClient

TYPE_MAP = {
    'playing': ('now_playing', 'get_now_playing'),
    'popular': ('popular', 'get_popular'),
    'top': ('top_rated', 'get_top_rated'),
    'upcoming': ('upcoming', 'get_upcoming'),
}

def main():
    parser = argparse.ArgumentParser(description="TMDB CLI tool")
    parser.add_argument('--type', choices=TYPE_MAP.keys(), required=True, help="Loại phim")
    parser.add_argument('--limit', type=int, default=4, help="Số phim hiển thị")
    parser.add_argument('--page', type=int, default=1, help="Trang dữ liệu")
    args = parser.parse_args()

    client = TMDBClient()

    movie_type_api, method_name = TYPE_MAP[args.type]

    # Lấy data bằng gọi method tương ứng
    fetch_method = getattr(client, method_name)
    data = fetch_method(page=args.page)

    client.print_movies(data, limit=args.limit)


if __name__ == "__main__":
    main()
