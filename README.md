# 📝 Vazifalar Ro'yxati (Fullstack Todo App)

Ushbu loyiha zamonaviy va tezkor **REST API** asosida ishlaydigan vazifalar menejeri bo'lib, backend va frontend qismlari to'liq integratsiya qilingan. 

---

## 🚀 Loyiha Imkoniyatlari

* ✅ **Vazifa Yaratish:** Sarlavha, batafsil matn va muddatni kiritish.
* 📜 **Real-vaqtda Yangilanish:** Ma'lumot qo'shilganda yoki o'chirilganda sahifa yangilanmasdan (AJAX) o'zgaradi.
* 🗑️ **Vazifani O'chirish:** Har bir vazifa uchun maxsus o'chirish tugmasi.
* 🎨 **Zamonaviy Dizayn:** Tailwind CSS-ning murakkab selektorlari yordamida yaratilgan "Dark Mode" interfeysi.
* ⚡ **CORS Qo'llab-quvvatlash:** Frontend va Backend o'rtasidagi xavfsiz aloqa.

---

## 🛠️ Texnologiyalar Steki

### **Backend (Python)**
* **Flask:** Web-server va API endpointlarni boshqarish uchun.
* **TinyDB:** Ma'lumotlarni JSON formatida saqlash uchun yengil ma'lumotlar bazasi.
* **Flask-CORS:** Turli portlardan keladigan so'rovlarga ruxsat berish uchun.

### **Frontend (JavaScript/HTML)**
* **JavaScript (ES6+):** Asinxron `fetch` so'rovlari va DOM bilan ishlash.
* **Tailwind CSS:** JIT (Just-In-Time) engine va maxsus klasslar yordamida dizayn.
* **Vite:** Loyihani tezkor yig'ish va ishlab chiqish muhiti.

---

## 📂 Fayllar Strukturasi

```text
├── app.py              # Flask server (Backend)
├── db.json             # TinyDB bazasi (JSON formatda)
├── index.html          # Asosiy UI sahifasi
├── src/
│   └── main.js         # JavaScript mantiqi va API aloqasi
├── style.css           # Tailwind CSS stillari
└── README.md           # Loyiha hujjatlari