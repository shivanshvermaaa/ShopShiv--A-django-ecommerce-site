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

## 📸 Screenshots  
Here are some screenshots that showcase the app's UI and key features.

---

### 🏠 Front Page
<img src="https://github.com/user-attachments/assets/0c439c8d-6df0-460a-9e20-e9613761237c" alt="Front Page" width="600" height="800">

---

### 🛍️ Product Info Page
<img src="https://github.com/user-attachments/assets/3279b99f-9720-45a2-8cfd-ed049198da10" alt="Product Info Page" width="600" height="800">

---

### 🧾 All Products Showcase
<img src="https://github.com/user-attachments/assets/1b71efa8-ee39-4a52-a74e-30cef2637b6c" alt="All Products" width="600" height="800">

---

### 🔐 Login Page
<img src="https://github.com/user-attachments/assets/37d815d3-bf43-4abe-8450-a9b0fa0324f3" alt="Login Page" width="600" height="800">

---

### 🧑‍💻 Register Page
<img src="https://github.com/user-attachments/assets/3bb55e3b-88df-4e12-91d3-d817becf5868" alt="Register Page" width="600" height="800">

---

### 🏠 Dashboard (After Login)
<p align="center">
  <img src="https://github.com/user-attachments/assets/19c236af-df25-4dd8-a12d-d106a1619479" alt="Dashboard 1" width="600" height="800">
  <br><br>
  <img src="https://github.com/user-attachments/assets/4d5c046f-1ea1-46b8-add5-fe41af90ee54" alt="Dashboard 2" width="600" height="800">
</p>

---

### 👤 Profile Management Page  
Update email, username, or delete your account.

<img src="https://github.com/user-attachments/assets/2cd24bcb-0ca4-4eb6-9656-2d866302f5b2" alt="Profile Management" width="600" height="800">

---

### 🚚 Update Shipping Page  
Lets users update their shipping address.

<img src="https://github.com/user-attachments/assets/39df9b3d-5344-4d93-9d37-354e98dd99b0" alt="Update Shipping" width="600" height="800">

---

### 📧 Email Sent Page (After Registration)
<img src="https://github.com/user-attachments/assets/9ecf3f80-bb0a-4b9e-ae44-03c2bfac0007" alt="Email Sent Page" width="600" height="800">

---

### ✉️ Email Verification Page  
The user also receives a success or failure notification after verifying the link.

<img src="https://github.com/user-attachments/assets/ff434ead-2ea6-45b7-9594-73c770bfc52c" alt="Email Verification" width="600" height="800">

---

### 💳 Checkout Page  
Shipping address auto-fills if already saved.

<img src="https://github.com/user-attachments/assets/63255161-9829-43b1-975a-e4543290ce47" alt="Checkout Page" width="600" height="800">

---

### 🧾 Payment Integration  
After successful payment, order details are securely stored in the backend.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1a5f09b6-a6aa-4603-8955-3466bc00c75e" alt="Payment 1" width="600" height="800">
  <br><br>
  <img src="https://github.com/user-attachments/assets/8d366f78-44ff-41c5-ad1c-33b1a511f895" alt="Payment 2" width="600" height="800">
  <br><br>
  <img src="https://github.com/user-attachments/assets/2c9965b0-268f-4475-9454-6cda0b6a8421" alt="Payment 3" width="600" height="800">
</p>

---

### 🖥️ Backend  
Displays how order details and user data are managed and stored securely in the backend.

<p align="center">
  <img src="https://github.com/user-attachments/assets/4a73b0e5-4c47-4213-b2a2-98214a623014" alt="Backend View 1" width="600" height="800">
  <br><br>
  <img src="https://github.com/user-attachments/assets/9178f9a5-d8cb-47cf-9bc0-d3b4597085f0" alt="Backend View 2" width="600" height="800">
</p>

<hr>




















