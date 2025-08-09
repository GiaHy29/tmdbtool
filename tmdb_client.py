import requests
from display import print_movies_table, print_error, show_movie_overview
from config import API_KEY, BASE_URL, DEFAULT_LANGUAGE

class TMDBClient:
    def __init__(self, api_key=API_KEY, base_url=BASE_URL, language=DEFAULT_LANGUAGE):
        self.api_key = api_key
        self.base_url = base_url
        self.language = language

    def fetch_movies(self, movie_type, page=1):
        """
        Gọi API lấy phim theo loại (now_playing, popular, top_rated, upcoming)
        """
        url = f"{self.base_url}/{movie_type}"
        params = {
            'api_key': self.api_key,
            'language': self.language,
            'page': page
        }
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi gọi API: {e}")
            return None

    def print_movies(self, data, limit=4):
        if not data or 'results' not in data:
            print_error("Không có dữ liệu phim.")
            return
        movies = data['results'][:limit]
        print_movies_table(movies)
        show_movie_overview(movies)

    # Các method cho mỗi type
    def get_now_playing(self, page=1):
        return self.fetch_movies("now_playing", page)

    def get_popular(self, page=1):
        return self.fetch_movies("popular", page)

    def get_top_rated(self, page=1):
        return self.fetch_movies("top_rated", page)

    def get_upcoming(self, page=1):
        return self.fetch_movies("upcoming", page)


