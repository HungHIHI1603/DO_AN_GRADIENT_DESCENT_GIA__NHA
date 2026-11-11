
# -*- coding: utf-8 -*-

# ============================================================
# UNG DUNG DU DOAN GIA NHA BANG GRADIENT DESCENT
# ============================================================

import tkinter as tk  # Thu vien tao giao dien Python.
from tkinter import ttk, messagebox, filedialog  # Cac thanh phan giao dien.
from pathlib import Path  # Thu vien xu ly duong dan tep.

from gradient import (  # Nhap cac ham xu ly thuat toan.
    doc_du_lieu,  # Ham doc du lieu CSV.
    gradient_descent,  # Ham toi uu tham so bang Gradient Descent.
    du_doan_gia  # Ham du doan gia nha.
)


class UngDungDuDoanGiaNha:  # Khai bao lop ung dung.

    def __init__(self, cua_so):  # Ham khoi tao ung dung.
        self.cua_so = cua_so  # Luu cua so chinh.
        self.cua_so.title("Du doan gia nha - Gradient Descent")  # Dat tieu de.
        self.cua_so.geometry("850x650")  # Dat kich thuoc cua so.
        self.cua_so.minsize(700, 550)  # Dat kich thuoc toi thieu.

        self.duong_dan_csv = Path(__file__).with_name(
            "du_lieu_gia_nha.csv"
        )  # Tim tep CSV cung thu muc voi app.py.

        self.mo_hinh = None  # Khoi tao bien luu mo hinh.
        self.tao_giao_dien()  # Tao giao dien ung dung.
        self.huấn_luyện()  # Doc du lieu va huan luyen mo hinh.

    def tao_giao_dien(self):  # Ham tao giao dien.

        khung = ttk.Frame(self.cua_so, padding=20)  # Tao khung chinh.
        khung.pack(fill="both", expand=True)  # Cho khung mo rong.

        tieu_de = ttk.Label(
            khung,
            text="DU DOAN GIA NHA BANG GRADIENT DESCENT",
            font=("Arial", 18, "bold")
        )  # Tao tieu de ung dung.
        tieu_de.pack(pady=15)  # Hien thi tieu de.

        mo_ta = ttk.Label(
            khung,
            text="Mo hinh hoi quy tuyen tinh: Dien tich nha -> Gia nha",
            font=("Arial", 11)
        )  # Tao dong mo ta.
        mo_ta.pack(pady=5)  # Hien thi mo ta.

        ttk.Separator(khung).pack(fill="x", pady=15)  # Tao duong phan cach.

        ttk.Label(
            khung,
            text="DU LIEU HUAN LUYEN",
            font=("Arial", 12, "bold")
        ).pack(anchor="w")  # Hien thi tieu de du lieu.

        hang_csv = ttk.Frame(khung)  # Tao hang chon tep CSV.
        hang_csv.pack(fill="x", pady=10)  # Hien thi hang chon tep.

        ttk.Button(
            hang_csv,
            text="Chon tep CSV",
            command=self.chon_csv
        ).pack(side="left")  # Tao nut chon tep CSV.

        self.nhan_ten_tep = ttk.Label(
            hang_csv,
            text=self.duong_dan_csv.name
        )  # Tao nhan ten tep.
        self.nhan_ten_tep.pack(side="left", padx=12)  # Hien thi ten tep.

        ttk.Separator(khung).pack(fill="x", pady=15)  # Tao duong phan cach.

        ttk.Label(
            khung,
            text="NHAP DIEN TICH CAN DU DOAN",
            font=("Arial", 12, "bold")
        ).pack(anchor="w")  # Hien thi tieu de nhap lieu.

        hang_nhap = ttk.Frame(khung)  # Tao hang nhap dien tich.
        hang_nhap.pack(anchor="w", pady=12)  # Hien thi hang nhap.

        self.o_nhap_dien_tich = ttk.Entry(
            hang_nhap,
            width=20,
            font=("Arial", 12)
        )  # Tao o nhap dien tich.

        self.o_nhap_dien_tich.insert(0, "50")  # Dat dien tich mac dinh.
        self.o_nhap_dien_tich.pack(side="left")  # Hien thi o nhap.

        ttk.Label(
            hang_nhap,
            text="m2",
            font=("Arial", 11)
        ).pack(side="left", padx=8)  # Hien thi don vi.

        ttk.Button(
            hang_nhap,
            text="HUAN LUYEN VA DU DOAN",
            command=self.du_doan_gia_nha
        ).pack(side="left", padx=15)  # Tao nut huan luyen va du doan.

        ttk.Button(
            khung,
            text="HUAN LUYEN LAI",
            command=self.huấn_luyện
        ).pack(anchor="w", pady=5)  # Tao nut huan luyen lai.

        ttk.Separator(khung).pack(fill="x", pady=15)  # Tao duong phan cach.

        ttk.Label(
            khung,
            text="KET QUA CHUONG TRINH",
            font=("Arial", 12, "bold")
        ).pack(anchor="w")  # Hien thi tieu de ket qua.

        self.vung_ket_qua = tk.Text(
            khung,
            height=18,
            font=("Consolas", 11),
            wrap="word"
        )  # Tao vung hien thi ket qua.

        self.vung_ket_qua.pack(
            fill="both",
            expand=True,
            pady=10
        )  # Hien thi vung ket qua.

        self.hien_thi("Chuong trinh san sang. Hay nhap dien tich va bam du doan.")  # Thong bao ban dau.

    def chon_csv(self):  # Ham chon tep du lieu.

        tep = filedialog.askopenfilename(
            title="Chon du lieu gia nha",
            filetypes=[("Tep CSV", "*.csv")]
        )  # Mo hop thoai chon tep CSV.

        if tep:  # Kiem tra nguoi dung da chon tep.
            self.duong_dan_csv = Path(tep)  # Luu duong dan tep.
            self.nhan_ten_tep.config(
                text=self.duong_dan_csv.name
            )  # Cap nhat ten tep tren giao dien.

            self.huấn_luyện()  # Huan luyen lai theo du lieu moi.

    def huấn_luyện(self):  # Ham huan luyen mo hinh.

        try:  # Bat dau khoi xu ly loi.

            x, y = doc_du_lieu(
                self.duong_dan_csv
            )  # Doc dien tich va gia nha tu CSV.

            self.mo_hinh = gradient_descent(
                x,
                y,
                alpha=0.05,
                so_vong_lap_toi_da=20000,
                epsilon=1e-8
            )  # Chay thuat toan Gradient Descent.

            noi_dung = (  # Tao noi dung ket qua huan luyen.
                "KET QUA HUAN LUYEN\n"
                "------------------------------\n"
                f"So mau du lieu: {len(x)}\n"
                f"Toc do hoc alpha: {self.mo_hinh['alpha']}\n"
                f"So vong lap: {self.mo_hinh['so_vong_lap']}\n"
                f"Theta 0: {self.mo_hinh['theta_0']:.6f}\n"
                f"Theta 1: {self.mo_hinh['theta_1']:.6f}\n"
                f"Ham muc tieu J: {self.mo_hinh['loss']:.6f}\n"
            )  # Ket thuc noi dung ket qua.

            self.hien_thi(noi_dung)  # Hien thi ket qua.

        except Exception as loi:  # Bat loi neu doc CSV hoac huan luyen that bai.
            self.mo_hinh = None  # Xoa mo hinh neu co loi.
            messagebox.showerror(
                "Loi huan luyen",
                str(loi)
            )  # Hien thi thong bao loi.

    def du_doan_gia_nha(self):  # Ham xu ly nut du doan.

        try:  # Bat dau xu ly loi.

            if self.mo_hinh is None:  # Kiem tra mo hinh da duoc huan luyen.
                self.huấn_luyện()  # Huan luyen neu chua co mo hinh.

            if self.mo_hinh is None:  # Kiem tra ket qua huan luyen.
                return  # Dung neu huan luyen that bai.

            dien_tich = float(
                self.o_nhap_dien_tich.get()
            )  # Lay dien tich nguoi dung nhap.

            if dien_tich <= 0:  # Kiem tra dien tich hop le.
                raise ValueError("Dien tich phai lon hon 0.")  # Bao loi neu khong hop le.

            gia = du_doan_gia(
                dien_tich,
                self.mo_hinh
            )  # Du doan gia nha bang mo hinh da toi uu.

            noi_dung = (  # Tao noi dung ket qua du doan.
                "KET QUA DU DOAN GIA NHA\n"
                "==============================\n"
                f"Dien tich nhap: {dien_tich:.2f} m2\n"
                f"Gia nha du doan: {gia:,.2f} trieu dong\n"
                f"Tuong duong: {gia / 1000:,.3f} ty dong\n\n"
                "THONG TIN GRADIENT DESCENT\n"
                "------------------------------\n"
                f"So vong lap: {self.mo_hinh['so_vong_lap']}\n"
                f"Toc do hoc alpha: {self.mo_hinh['alpha']}\n"
                f"Ham muc tieu J: {self.mo_hinh['loss']:.6f}\n\n"
                "Mo hinh da duoc toi uu bang Gradient Descent.\n"
                "Du lieu kem theo chi la du lieu minh hoa."
            )  # Ket thuc noi dung ket qua.

            self.hien_thi(noi_dung)  # Hien thi ket qua len giao dien.

        except ValueError as loi:  # Bat loi khi nhap sai du lieu.
            messagebox.showwarning(
                "Du lieu khong hop le",
                str(loi)
            )  # Hien thi canh bao.

        except Exception as loi:  # Bat cac loi khac.
            messagebox.showerror(
                "Loi du doan",
                str(loi)
            )  # Hien thi thong bao loi.

    def hien_thi(self, noi_dung):  # Ham cap nhat vung ket qua.

        self.vung_ket_qua.delete(
            "1.0",
            "end"
        )  # Xoa noi dung cu.

        self.vung_ket_qua.insert(
            "end",
            noi_dung
        )  # Hien thi noi dung moi.


if __name__ == "__main__":  # Kiem tra tep duoc chay truc tiep.

    cua_so_chinh = tk.Tk()  # Tao cua so ung dung.

    ung_dung = UngDungDuDoanGiaNha(
        cua_so_chinh
    )  # Khoi tao ung dung.

    cua_so_chinh.mainloop()  # Bat dau vong lap giao dien.
