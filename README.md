# REST API — Amaliy mashg‘ulot

## Mavzu
**REST API yaratish va HTTP so‘rovlarini sinash**

## Maqsad
Ushbu amaliy mashg‘ulotda talaba REST API, endpoint, JSON, HTTP metodlari va status kodlari bilan amalda ishlaydi.

Mashg‘ulot davomida quyidagi metodlar bajariladi:

- `GET` — ma’lumot olish
- `POST` — yangi ma’lumot qo‘shish
- `PUT` — mavjud ma’lumotni o‘zgartirish
- `DELETE` — ma’lumotni o‘chirish

---

## 1. GitHub Codespaces orqali ishga tushirish

Repository ichida:

**Code → Codespaces → Create codespace on main**

ni bosing.

Terminal ochilgach:

```bash
pip install -r requirements.txt
```

So‘ng:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

`Ports` oynasidan **8000-port** ni oching.

Swagger oynasi uchun manzil oxiriga:

```text
/docs
```

qo‘shiladi.

Masalan:

```text
https://...-8000.app.github.dev/docs
```

---

# 2. API endpointlari

| Metod | Endpoint | Vazifasi |
|---|---|---|
| GET | `/students` | Barcha talabalarni chiqarish |
| GET | `/students/{id}` | Bitta talabani chiqarish |
| POST | `/students` | Yangi talaba qo‘shish |
| PUT | `/students/{id}` | Talaba ma’lumotini yangilash |
| DELETE | `/students/{id}` | Talabani o‘chirish |

---

# 3. Talaba bajarishi kerak bo‘lgan topshiriqlar

## 1-topshiriq
Swagger orqali:

```text
GET /students
```

so‘rovini bajaring.

Natijani tekshiring.

---

## 2-topshiriq
`POST /students` orqali o‘zingizni yangi talaba sifatida qo‘shing.

Namuna:

```json
{
  "name": "Ism Familiya",
  "group": "1-3"
}
```

Qaytgan `id` va **201 Created** status kodini yozib oling.

---

## 3-topshiriq
Yangi qo‘shilgan talabaning `id` raqamidan foydalanib:

```text
GET /students/{id}
```

so‘rovini bajaring.

---

## 4-topshiriq
`PUT /students/{id}` orqali o‘zingizning guruhingizni o‘zgartiring.

Masalan:

```json
{
  "name": "Ism Familiya",
  "group": "2-1"
}
```

---

## 5-topshiriq
Mavjud bo‘lmagan ID bilan:

```text
GET /students/999
```

so‘rovini bajaring.

**404 Not Found** xatosi qaytishini tekshiring.

---

## 6-topshiriq
`DELETE /students/{id}` orqali o‘zingiz qo‘shgan yozuvni o‘chiring.

So‘ng yana:

```text
GET /students
```

orqali ro‘yxatni tekshiring.

---

# 4. Mustaqil mini-topshiriq

Quyidagilardan bittasini tanlang:

1. `email` maydonini qo‘shing.
2. `course` maydonini qo‘shing.
3. `/students/count` endpointini yarating.
4. `/students/group/{group_name}` endpointini yarating.
5. Talabaning ismiga ko‘ra qidiruv endpointini yarating.

---

# 5. Hisobot uchun talablar

Talaba quyidagilarni topshiradi:

1. GitHub repository havolasi.
2. Swagger ishlayotgan ekran rasmi.
3. `GET /students` natijasi.
4. `POST /students` natijasi.
5. `PUT` natijasi.
6. `DELETE` natijasi.
7. `404 Not Found` xatosi rasmi.
8. Mustaqil mini-topshiriq natijasi.
9. 5–7 jumladan iborat xulosa.

---

# 6. Nazorat savollari

1. REST API nima?
2. Endpoint nima?
3. GET va POST o‘rtasidagi farq nima?
4. PUT nima uchun ishlatiladi?
5. DELETE nima qiladi?
6. JSON nima?
7. `200 OK` nimani anglatadi?
8. `201 Created` nimani anglatadi?
9. `404 Not Found` qachon qaytadi?
10. Swagger UI nima uchun kerak?

---

# 7. Baholash mezoni

| Faoliyat | Ball |
|---|---:|
| API’ni ishga tushirish | 10 |
| GET so‘rovi | 10 |
| POST so‘rovi | 15 |
| PUT so‘rovi | 15 |
| DELETE so‘rovi | 10 |
| 404 xatoni tekshirish | 10 |
| Mustaqil mini-topshiriq | 20 |
| Hisobot va xulosa | 10 |
| **Jami** | **100** |

---

## Kutiladigan natija

Mashg‘ulot yakunida talaba REST API bilan amalda ishlaydi, HTTP metodlarini farqlaydi, JSON ma’lumot yuboradi va Swagger orqali API’ni sinab ko‘ra oladi.
