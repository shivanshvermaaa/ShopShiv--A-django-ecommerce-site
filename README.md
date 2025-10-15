<h1 align="center">🛍️ ShopShiv- A Django E-Commerce Website</h1>

<p align="center">
A <b>full-featured E-Commerce web application</b> built with <b>Django</b>, offering a seamless online shopping experience.  
Includes <b>product listing, cart management (localStorage + AJAX)</b>, <b>checkout with PayPal</b>, and a complete <b>authentication system</b> — all designed for a modern and responsive experience.
</p>

<hr>

## 🚀 Features

### 🧭 Core Functionality

🏠 **Home Page:** Displays all available products with filtering and search options.  
🛒 **Add to Cart:** Add items to the cart instantly using <b>localStorage</b> (cart persists across page reloads).  
⚡ **AJAX Cart Actions:** Real-time cart updates and smooth button operations without page reloads.  
📦 **Checkout Page:** Summarizes cart items and handles the order process.  
💳 **Payment Integration (PayPal Sandbox):** Secure and real-world payment flow simulation without actual transactions.  
🧾 **Order Summary & Confirmation:** Displays a clear summary after successful payment.  

<hr>

### 👥 User Management

🔐 **User Registration & Login:** Implemented using Django’s built-in authentication system.  
📧 **Email Verification:** Sends activation link for account validation.  
🔑 **Password Reset:** Secure token-based reset via email.  
⚙️ **Profile Management:** Update personal details or delete accounts easily.  

<hr>

### 🧰 Admin Functionality

🧩 **Admin Dashboard:** Manage users, products, and orders from the Django Admin.  
📊 **Product Management:** Add, update, or delete product details and categories.

<hr>

## ⚙️ Technical Features

- ⚙️ <b>Django 5+</b> backend with modular app structure.  
- 🗄️ <b>SQLite / PostgreSQL</b> database support (configurable).  
- 🌐 <b>HTML, CSS, Bootstrap</b> for frontend styling.  
- 🧾 <b>Crispy Forms</b> for elegant form rendering.  
- ⚡ <b>AJAX Integration</b> for smooth UI interactions and asynchronous updates.  
- 🪶 Reusable base template (`base.html`) for consistent layout.  
- 🧱 CSRF protection and secure session handling.  
- 🔄 Organized <b>Git Branch Workflow</b>:
  - `main` — production-ready code  
  - `feature/cart` — cart logic and AJAX  
  - `feature/user-management` — authentication & profiles  
  - `feature/store-images` — product images and media  

<hr>

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML5, CSS3, Bootstrap, AJAX |
| **Backend** | Python (Django Framework) |
| **Database** | SQLite / PostgreSQL |
| **Authentication** | Django’s built-in Auth + Email Verification |
| **Payment Gateway** | PayPal Developer Sandbox |
| **Version Control** | Git + GitHub (Feature Branch Workflow) |

<hr>

<hr>

## 🔒 Authentication Flow

1. 🧾 **User Registration:** A new user registers — the account is created as **inactive**.  
2. 📧 **Email Verification:** A verification email is sent with an **activation link**.  
3. ✅ **Account Activation:** Once activated, the user can **log in** and access all features.  
4. 🔁 **Password Reset:** Secure, token-based reset process via email for forgotten passwords.


## 🏗️ Project Structure
```
django-ecommerce/
│
├── ecommerce/ # Main project configuration
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── store/ # Store app - products & home
│ ├── templates/store/
│ ├── static/store/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── forms.py
│
├── cart/ # Cart app - AJAX-based cart logic
│ ├── templates/cart/
│ ├── static/cart/
│ ├── views.py
│ ├── urls.py
│ └── models.py
│
├── payment/ # Payment app - PayPal integration
│ ├── templates/payment/
│ ├── static/payment/
│ ├── views.py
│ ├── urls.py
│ └── models.py
│
├── account/ # Authentication & user management
│ ├── templates/account/
│ ├── static/account/
│ ├── views.py
│ ├── urls.py
│ └── forms.py
│
├── static/ # Global static files (CSS, JS, media)
│ ├── css/
│ ├── js/
│ └── media/
│
├── requirements.txt
└── manage.py
```

<hr>

## 🧰 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/shivanshvermaaa/django-ecommerce
cd django-ecommerce

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows (PowerShell)
.\venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create an admin superuser (optional but recommended)
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Visit the site in your browser
# http://127.0.0.1:8000/
```
<hr>

## 💡 Future Enhancements

- 🔐 Add **JWT-based authentication** for APIs.  
- 📱 Integrate **Django REST Framework** for mobile/app API support.  
- ⭐ Implement **Product Reviews & Ratings**.  
- 💖 Add **Wishlist & Recently Viewed Items**.  
- ⚡ Enhance frontend using **React or Vue** for a SPA-like experience.

<hr>
<hr>

## 🤝 Contributing

Contributions are always welcome! 🎉  
If you'd like to improve this project — fix bugs, add new features, or enhance UI — feel free to:

1. Fork the repository  
2. Create a new feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m 'Add some feature'`)  
4. Push to your branch (`git push origin feature-name`)  
5. Open a Pull Request 🚀  

<hr>

## 📄 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it, provided proper credit is given.  
See the [LICENSE](LICENSE) file for more details.

