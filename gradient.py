# -*- coding: utf-8 -*-
"""Các phép tính hồi quy tuyến tính và Gradient Descent cho bài toán giá nhà."""

import csv  # Đọc dữ liệu từ tệp CSV.
import math  # Tính căn bậc hai khi chuẩn hóa dữ liệu.


def doc_du_lieu(duong_dan):  # Đọc diện tích và giá nhà từ tệp dữ liệu.
    dien_tich = []  # Tạo danh sách lưu diện tích.
    gia_nha = []  # Tạo danh sách lưu giá nhà.
    with open(duong_dan, encoding="utf-8-sig", newline="") as tep:  # Mở tệp CSV.
        for dong in csv.DictReader(tep):  # Đọc lần lượt từng dòng dữ liệu.
            dien_tich.append(float(dong["dien_tich_m2"]))  # Lấy diện tích theo m².
            gia_nha.append(float(dong["gia_nha_trieu_dong"]))  # Lấy giá theo triệu đồng.
    if len(dien_tich) < 2:  # Kiểm tra số lượng mẫu dữ liệu.
        raise ValueError("Cần ít nhất 2 dòng dữ liệu để huấn luyện.")  # Báo lỗi nếu thiếu mẫu.
    if len(dien_tich) != len(gia_nha):  # Kiểm tra số lượng hai cột.
        raise ValueError("Số lượng diện tích và giá nhà không khớp.")  # Báo lỗi nếu dữ liệu lệch.
    return dien_tich, gia_nha  # Trả về hai danh sách dữ liệu.


def chuan_hoa_du_lieu(danh_sach):  # Chuẩn hóa diện tích để tối ưu ổn định hơn.
    trung_binh = sum(danh_sach) / len(danh_sach)  # Tính giá trị trung bình.
    phuong_sai = sum((x - trung_binh) ** 2 for x in danh_sach) / len(danh_sach)  # Tính phương sai.
    do_lech_chuan = math.sqrt(phuong_sai)  # Tính độ lệch chuẩn.
    if do_lech_chuan == 0:  # Kiểm tra tất cả diện tích có giống nhau hay không.
        raise ValueError("Diện tích phải có sự khác nhau.")  # Báo lỗi nếu không thể chuẩn hóa.
    du_lieu_chuan = [(x - trung_binh) / do_lech_chuan for x in danh_sach]  # Đưa dữ liệu về thang đo chuẩn.
    return du_lieu_chuan, trung_binh, do_lech_chuan  # Trả dữ liệu và thông số chuẩn hóa.


def tinh_ham_muc_tieu(theta_0, theta_1, x, y):  # Tính hàm mất mát bình phương sai số.
    so_mau = len(y)  # Lấy số lượng mẫu dữ liệu.
    tong_binh_phuong = sum((theta_1 * xi + theta_0 - yi) ** 2 for xi, yi in zip(x, y))  # Cộng bình phương sai số.
    return tong_binh_phuong / (2 * so_mau)  # Chia cho 2m để đạo hàm gọn hơn.


def gradient_descent(x, y, alpha=0.05, so_vong_lap_toi_da=20000, epsilon=1e-8):  # Tối ưu hai tham số.
    x_chuan, trung_binh, do_lech_chuan = chuan_hoa_du_lieu(x)  # Chuẩn hóa diện tích.
    so_mau = len(y)  # Lấy số mẫu huấn luyện.
    theta_1 = 0.0  # Khởi tạo hệ số góc.
    theta_0 = sum(y) / so_mau  # Khởi tạo hệ số tự do bằng giá trung bình.
    for vong_lap in range(1, so_vong_lap_toi_da + 1):  # Bắt đầu các vòng lặp tối ưu.
        sai_so = [theta_1 * xi + theta_0 - yi for xi, yi in zip(x_chuan, y)]  # Tính sai số dự đoán.
        dao_ham_theta_1 = sum(e * xi for e, xi in zip(sai_so, x_chuan)) / so_mau  # Đạo hàm theo theta_1.
        dao_ham_theta_0 = sum(sai_so) / so_mau  # Đạo hàm theo theta_0.
        loss_cu = tinh_ham_muc_tieu(theta_0, theta_1, x_chuan, y)  # Tính hàm mục tiêu trước cập nhật.
        theta_1_moi = theta_1 - alpha * dao_ham_theta_1  # Cập nhật theta_1 theo Gradient Descent.
        theta_0_moi = theta_0 - alpha * dao_ham_theta_0  # Cập nhật theta_0 theo Gradient Descent.
        loss_moi = tinh_ham_muc_tieu(theta_0_moi, theta_1_moi, x_chuan, y)  # Tính hàm mục tiêu sau cập nhật.
        theta_0, theta_1 = theta_0_moi, theta_1_moi  # Chấp nhận hai tham số mới.
        if abs(loss_cu - loss_moi) < epsilon:  # Kiểm tra độ thay đổi của hàm mục tiêu.
            break  # Dừng khi hàm mục tiêu gần như không đổi.
    return {  # Trả về các thông tin cần dùng khi dự đoán và báo cáo.
        "theta_0": theta_0,  # Hệ số tự do đã tối ưu.
        "theta_1": theta_1,  # Hệ số góc đã tối ưu.
        "trung_binh": trung_binh,  # Trung bình diện tích của tập huấn luyện.
        "do_lech_chuan": do_lech_chuan,  # Độ lệch chuẩn diện tích.
        "so_vong_lap": vong_lap,  # Số vòng lặp thực tế.
        "loss": tinh_ham_muc_tieu(theta_0, theta_1, x_chuan, y),  # Hàm mục tiêu cuối cùng.
        "alpha": alpha,  # Tốc độ học được sử dụng.
        "epsilon": epsilon,  # Ngưỡng dừng được sử dụng.
    }


def du_doan_gia(dien_tich_moi, mo_hinh):  # Dự đoán giá nhà cho diện tích mới.
    x_chuan = (dien_tich_moi - mo_hinh["trung_binh"]) / mo_hinh["do_lech_chuan"]  # Chuẩn hóa diện tích mới.
    gia_du_doan = mo_hinh["theta_1"] * x_chuan + mo_hinh["theta_0"]  # Tính giá theo mô hình tuyến tính.
    return gia_du_doan  # Trả giá dự đoán theo triệu đồng.
