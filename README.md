# Movie CLI - Công cụ xem danh sách phim từ TMDB

🔥 Đây là công cụ CLI đơn giản giúp bạn xem danh sách phim đang hot, phổ biến, sắp ra mắt từ API The Movie Database (TMDB).  
Sử dụng thư viện [rich](https://github.com/Textualize/rich) để hiển thị bảng màu sắc đẹp mắt trong terminal.

---

## Tính năng

- Hiển thị bảng phim với thông tin: STT, tên phim, ngày ra mắt, điểm đánh giá và lượt vote.
- Cho phép xem tóm tắt (overview) phim qua tương tác nhập số.
- Hỗ trợ nhiều loại danh sách phim: đang chiếu, phổ biến, top rated, sắp ra mắt.
- Hiển thị ngày tháng theo định dạng dễ đọc (dd/mm/yyyy).
- Tô màu điểm đánh giá theo mức độ (xanh, vàng, đỏ).

---

## Cài đặt

1. Clone repo:

```bash
git clone https://github.com/username/movie-cli.git
cd movie-cli
```
2. Tạo và kích hoạt môi trường ảo:
```
python -m venv .venv
```
# Linux/macOS:
```
source .venv/bin/activate
```
# Windows:
```
.venv\Scripts\activate
```
3. Cài thư viện cần thiết:
```
pip install -r requirements.txt
```
5. cập nhật API_KEY trong config.py
## Sử dụng
Chạy file chính với tham số --type:
```
python main.py --type popular
```
Các type có thể dùng:
    playing : Phim đang chiếu
    popular : Phim phổ biến
    top : Phim được đánh giá cao
    upcoming : Phim sắp ra mắt

[https://roadmap.sh/projects/tmdb-cli](https://github.com/GiaHy29/tmdbtool/)
