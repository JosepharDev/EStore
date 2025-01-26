# EStore

EStore is an online marketplace that allows sellers to upload and sell digital images while enabling buyers to browse, purchase, and download them. To protect seller content, images are watermarked until they are purchased. The platform is built with Django, HTML, CSS, Bootstrap, and PayPal for secure payment processing.

## Features

### Core Features:

* **Sellers**:
  * Upload and manage digital images for sale.
  * View earnings and sales history.
* **Buyers**:
  * Browse a catalog of images by category or search.
  * Add items to the cart and complete purchases via PayPal.
  * Download purchased images without watermarks.

### Additional Features:

* **Watermarking System**: All images are watermarked until purchased to protect seller content.
* **Responsive Design**: Ensures the platform works seamlessly across devices.
* **User Authentication**: Secure sign-up, login, and profile management for both buyers and sellers.

## Technologies Used

* **Frontend**:
  * HTML, CSS, and Bootstrap for a clean and responsive user interface.
* **Backend**:
  * Django, a Python-based web framework for handling business logic.
* **Database**:
  * PostgreSQL for reliable and efficient data storage.
* **Payment Gateway**:
  * PayPal API for secure transactions.
* **Deployment**:
  * Docker for containerized deployment of the application.

## Installation and Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/JosepharDev/EStore.git
   cd estore
   ```
2. **Set up a virtual environment:**
   ```
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Run the development server:**
   ```
   python manage.py runserver
   ```
5. **Access the app:**
   Open `<span>http://127.0.0.1:8000/</span>` in your web browser.

## Usage

* **Sellers**: Create an account, log in, and upload images with relevant details (e.g., price, description).
* **Buyers**: Browse images, add to cart, and complete purchases via PayPal.
