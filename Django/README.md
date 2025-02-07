# 🏨 Django Hotel Room Booking System

This is a **Hotel Room Booking System** built with **Django**. It allows users to book rooms, manage availability, and view booking details.

---

## 🚀 Features
- List available hotels & rooms.
- Search hotels by **name** or **location**.
- Book available rooms & manage bookings.
- Filter rooms based on **availability**.
- Django **Admin Panel** for hotel management.
- Success/Error messages for actions.

---

## 📌 Setup & Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/Shankarhack/hotel-booking-django.git
cd hotel-booking-django
```

### 2️⃣ **Create a Virtual Environment** (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Apply Database Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ **Create a Superuser (for Admin Panel)**
```sh
python manage.py createsuperuser
```
> Follow the prompts to set a username, email, and password.

### 6️⃣ **Run the Development Server**
```sh
python manage.py runserver
```
> The app will be available at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.

---

## 🎨 **Project Structure**
```
hotel_booking/
│── bookings/               # Main Django App
│   ├── migrations/         # Database Migrations
│   ├── static/             # CSS, JS, Images
│   │   ├── css/
│   │   │   ├── styles.css  # Custom Styles
│   ├── templates/          # HTML Templates
│   │   ├── bookings/
│   │   │   ├── base.html
│   │   │   ├── hotel_list.html
│   │   │   ├── room_list.html
│── hotel_booking/          # Project Config
│── db.sqlite3              # SQLite Database
│── manage.py               # Django Management Script
│── requirements.txt        # Python Dependencies
│── README.md               # Documentation
```

---

## 🔗 **Endpoints**
| URL | Description |
|------|------------|
| `/` | List all hotels (with search) |
| `/hotel/<id>/rooms/` | Show rooms in a hotel |
| `/room/<id>/book/` | Book a room |
| `/admin/` | Django Admin Panel |

---

## 🌟 **Admin Panel**
You can access the **Django Admin Panel** to manage hotels, rooms, and bookings.

🔗 **URL:** `http://127.0.0.1:8000/admin/`  
👤 **Login with:** The superuser credentials you created earlier.

---

## 📌 **Deployment (Optional)**
If deploying on a production server, configure:
- `ALLOWED_HOSTS` in `settings.py`
- `DEBUG = False`
- Use **PostgreSQL/MySQL** instead of SQLite
- Run `collectstatic`:
  ```sh
  python manage.py collectstatic
  ```

---

## ✅ **Troubleshooting**
- **If migrations fail:**  
  ```sh
  python manage.py migrate --fake
  ```
- **If static files don’t load:**  
  Ensure `{% load static %}` is at the top of your templates.
- **If changes don’t reflect:**  
  Restart the server:  
  ```sh
  python manage.py runserver
  ```

---

## 🐜 **License**
This project is **open-source**. Feel free to modify and use it for personal or commercial purposes.

---

## 💡 **Contributing**
Pull requests are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`feature-new`).
3. Commit your changes.
4. Open a pull request.

---

## 💬 **Support & Contact**
For any issues, feel free to **open an issue** or contact:
📧 **Email:** shankar974059@gmail.com.com  
📣 **GitHub Issues:** [Report an Issue](https://github.com/shankarhack/hotel-booking-django/issues)

---

🚀 **Enjoy building with Django!** 🏨🎉