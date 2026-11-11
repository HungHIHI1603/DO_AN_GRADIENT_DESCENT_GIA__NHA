// Xu ly thao tac du doan tren giao dien web.
const form = document.getElementById("prediction-form"); // Lay form du doan.
const resultBox = document.getElementById("result-box"); // Lay khu vuc ket qua.
const predictButton = document.getElementById("predict-button"); // Lay nut du doan.

form.addEventListener("submit", async (event) => { // Lang nghe su kien gui form.
    event.preventDefault(); // Ngan trinh duyet tai lai trang.
    const area = document.getElementById("area").value; // Doc dien tich nguoi dung nhap.
    predictButton.disabled = true; // Tam khoa nut khi dang xu ly.
    predictButton.querySelector("span").textContent = "Đang tính toán..."; // Cap nhat trang thai nut.
    resultBox.innerHTML = '<div class="result-placeholder"><strong>Đang chạy Gradient Descent...</strong><span>Vui lòng chờ trong giây lát.</span></div>'; // Hien thi trang thai xu ly.

    try { // Bat dau goi backend.
        const response = await fetch("/du-doan", { // Gui yeu cau den Flask.
            method: "POST", // Su dung phuong thuc POST.
            headers: { "Content-Type": "application/x-www-form-urlencoded" }, // Khai bao dang du lieu gui.
            body: new URLSearchParams({ dien_tich: area }) // Dong goi dien tich.
        }); // Ket thuc yeu cau fetch.
        const data = await response.json(); // Doc ket qua JSON.
        if (!response.ok || !data.ok) { // Kiem tra ket qua co loi khong.
            throw new Error(data.message || "Không thể thực hiện dự đoán."); // Phat sinh loi de hien thi.
        } // Ket thuc kiem tra loi.

        resultBox.innerHTML = ` 
            <div class="result-content">
                <div class="result-label">GIÁ NHÀ ƯỚC TÍNH</div>
                <div class="result-price">${data.gia.toLocaleString("vi-VN", {maximumFractionDigits: 2})} <small style="font-size:12px;font-weight:600">triệu đồng</small></div>
                <div class="result-sub">Tương đương khoảng ${data.gia_ty.toLocaleString("vi-VN", {maximumFractionDigits: 3})} tỷ đồng · diện tích ${data.dien_tich} m²</div>
                <div class="result-details">
                    <div><span>Số vòng lặp</span><strong>${data.so_vong_lap}</strong></div>
                    <div><span>Learning rate</span><strong>${data.alpha}</strong></div>
                    <div><span>Hàm mục tiêu J</span><strong>${data.loss.toFixed(4)}</strong></div>
                </div>
            </div>`; // Hien thi ket qua du doan.
    } catch (error) { // Bat loi ket noi hoac loi du lieu.
        resultBox.innerHTML = `<div class="alert">${error.message}</div>`; // Hien thi noi dung loi.
    } finally { // Luon thuc hien sau khi xu ly.
        predictButton.disabled = false; // Mo lai nut du doan.
        predictButton.querySelector("span").textContent = "Chạy dự đoán"; // Khoi phuc ten nut.
    } // Ket thuc finally.
}); // Ket thuc lang nghe su kien.
