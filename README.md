# 📝 Vazifalar Ro'yxati (Fullstack Todo App)

Ushbu loyiha zamonaviy va tezkor **REST API** asosida ishlaydigan vazifalar menejeri bo'lib, **backend** va **frontend** qismlari to'liq integratsiya qilingan.

---

## 🚀 Loyiha Imkoniyatlari

* ✅ **Vazifa Yaratish:** Sarlavha, batafsil matn va muddatni kiritish
* 📜 **Real-vaqtda Yangilanish:** Ma'lumot qo'shilganda yoki o'chirilganda sahifa yangilanmasdan (AJAX) o'zgaradi
* 🗑️ **Vazifani O'chirish:** Har bir vazifa uchun alohida o'chirish tugmasi
* 🎨 **Zamonaviy Dizayn:** Tailwind CSS yordamida yaratilgan *Dark Mode* interfeys
* ⚡ **CORS Qo'llab-quvvatlash:** Frontend va Backend o'rtasida xavfsiz aloqa

---

## 🛠️ Texnologiyalar Steki

### 🔧 Backend (Python)

* **Flask** — REST API va server logikasini boshqarish
* **TinyDB** — JSON asosidagi yengil ma'lumotlar bazasi
* **Flask-CORS** — Turli portlardan keladigan so'rovlarga ruxsat berish

### 🎨 Frontend (JavaScript / HTML)

* **JavaScript (ES6+)** — `fetch` orqali asinxron so'rovlar va DOM bilan ishlash
* **Tailwind CSS** — Zamonaviy va moslashuvchan dizayn (JIT engine)
* **Vite** — Tezkor frontend build va development muhiti

---

## 📂 Fayllar Strukturasi

```text
├── app.py              # Flask server (Backend)
├── index.html          # Asosiy UI sahifasi
├── requirements.txt    # Python kutubxonalari
└── README.md           # Loyiha hujjatlari
```

---

## ⚙️ O'rnatish va Ishga Tushirish

### 🐧 Linux / 🍎 macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

### 🪟 Windows

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## 🔗 API Manzili (Backend)

```text
http://localhost:5000
```

---

## 📌 Eslatma

* CORS sozlamalari yoqilgan
* TinyDB ma'lumotlarni lokal JSON faylda saqlaydi

---

## 👨‍💻 Muallif

Ushbu loyiha o'quv va amaliy maqsadlarda ishlab chiqilgan.