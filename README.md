#  Phân tích hành vi người dùng Facebook

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Phân%20tích%20dữ%20liệu-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Trạng%20thái-Hoàn%20thành-success?style=for-the-badge">
</p>

---

## 📌 Tổng quan
Dự án này phân tích **hành vi người dùng Facebook** dựa trên bộ dữ liệu hơn **99.000 người dùng**, nhằm khám phá:
- Đặc điểm nhân khẩu học  
- Mức độ tương tác  
- Cách người dùng sử dụng nền tảng  

---

## 📊 Trực quan dữ liệu

###  Phân bố độ tuổi
![alt text](01_phan_bo_do_tuoi.png)

- Người dùng tập trung chủ yếu từ **13–25 tuổi**
- Giảm mạnh sau 35 tuổi

---

### 🎂 Phân bố ngày sinh
![alt text](02_phan_bo_ngay_sinh.png)

- Đỉnh cao tại **ngày 1**
- Có thể do người dùng nhập thông tin mặc định / ẩn thông tin

---

### 📅 Phân bố tháng sinh
![alt text](03_phan_bo_thang_sinh.png)

- Phân bố khá đồng đều  
- Tăng đột biến vào **tháng 1**

---

### 🚻 Phân bố giới tính
![alt text](04_phan_bo_gioi_tinh.png)

- Nam chiếm số lượng lớn hơn  
- Nữ có **mức độ tương tác cao hơn**

---

### ❤️ Lượt thích theo nhóm tuổi
![alt text](06_likes_theo_nhom_tuoi.png)

- Nhóm trẻ có mức tương tác cao nhất  
- Có thể tồn tại dữ liệu bất thường ở nhóm tuổi cao

---

### ⏱️ Thời gian sử dụng & số bạn bè
![alt text](07_tenure_theo_nhom_ban_be.png)

- Số bạn bè càng nhiều → thời gian sử dụng càng cao

---

### 🔗 Ma trận tương quan
![alt text](08_ma_tran_tuong_quan.png)

- Tương quan mạnh giữa **like mobile & tổng like**
- Mobile là nền tảng chính

---

## 📂 Dữ liệu & Nguồn tài Liệu Tham Khảo
- Nguồn: Kaggle  
- Quy mô: ~99.000 người dùng  
- Đã được làm sạch trước khi phân tích  
- Facebook data : https//www.kaggle.com/datasets/sheenabatra/facebook-data
- Facebook DataAnalysis : https://www.kaggle.com/code/ahmedmagdyahmed/facebook-data-analysis

---

## ▶️ Cách chạy dự án

```bash
git clone https://github.com/your-username/facebook-analysis.git
cd facebook-analysis
pip install -r requirements.txt
```

---

## 📁 Cấu trúc project

facebook-analysis/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt

---

## 🚀 Kết luận chính
- Người dùng trẻ chiếm đa số  
- Nữ có xu hướng tương tác nhiều hơn  
- Mobile là nền tảng chính của người dùng  

---

## 👥 Nhóm thực hiện
- Lê Đức Trung  
- Vũ Tú Nam  
- Văn Bảo Phước  

---

## ⭐️Thank for everyone .........
🙇🏻‍♂️🙇🏻‍♂️🙇🏻‍♂️🙇🏻‍♂️

