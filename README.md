# Table of Contents
- [1. Django Project Setup Guide](#django-project-setup-guide)
- [2. RASH-STORE API Documentation](#rash-store-api-documentation)

# Django Project Setup Guide
Follow these steps to install and run the Django project:

### 1. Clone the Repository
Clone the repository from GitHub to your local machine:
```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

### 2. Set Up the Virtual Environment with Pipenv
Use `pipenv` to create a virtual environment and install the dependencies:
```bash
pipenv install
```

### 3. Activate the Pipenv Virtual Environment
Once the installation is complete, activate the virtual environment:
```bash
pipenv shell
```

### 4. Set Up the Environment Variables
If the project uses a `.env` file, copy the example file and modify it as needed:
```bash
cp .env.example .env
```
Edit the `.env` file with your specific values (e.g., database credentials, secret key, etc.).

### 5. Apply Database Migrations
Run the following command to apply the migrations and set up the database schema:
```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)
To access the Django admin interface, create a superuser:
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
If the project uses static files, run this command to collect them into one location:
```bash
python manage.py collectstatic
```

### 8. Run the Development Server
Finally, run the Django development server:
```bash
python manage.py runserver
```
The project will now be accessible at `http://127.0.0.1:8000/`.

# RASH-STORE API Documentation
### 1. **Introduction**
The RASH-STORE API is a backend service for managing an online store. It provides endpoints for listing products, managing shopping carts, creating orders, and more. This API is built using Django and provides both a customizable admin dashboard and a browsable API for ease of use.

### 2. **Authentication**
This API requires authentication for certain endpoints. The authentication is handled using JWT (JSON Web Tokens). You need to include your token in the `Authorization` header with each request.

Example:
```http
Authorization: JWT <your-jwt-token>
```

### 3. **Base URL**
All requests to the API should be made to the following base URL: 
> `https://rash-store.up.railway.app/`

### 4. **Endpoints**
All available endpoints, grouped by functionality (e.g., products, collections, cart).

> ### Products
> *URL*: `/store/products`<br>
> *Method*: `GET, POST`<br>
> *Description*: Retrieves a list of products or adds a product.<br>
> *Request Parameters*:<br>
> - `title`: The title of the product.<br>
> - `slug`: Slug to reference the product.<br>
> - `description`: Description of the product.<br>
> - `inventory` (optional): Quantity of the product.<br>
> - `unit_price` (optional): Product price.<br>
> - `collection` (optional): The collection belong to.<be>
> ---
> *URL*: `/store/products/<id>`<br>
> *Method*: `GET, PUT, PATCH, DELETE`<br>
> *Description*: View, edit or delete a product<br>
> *Request Parameters*:<be>
> - `title`: The title of the product.<br>
> - `slug`: Slug to reference the product.<br>
> - `description`: Description of the product.<br>
> - `inventory` (optional): Quantity of the product.<br>
> - `unit_price` (optional): Product price.<br>
> - `collection` (optional): The collection belong to.<br>
> ---
> *URL*: `/store/products/<id>/images`<br>
> *Method*: `GET, POST`<br>
> *Description*: List or add an image to the product<br>
> *Request Parameters*:<br>
> - `image`: Picture of the product.<br>
> ---
> *URL*: `/store/products/<id>/reviews`<br>
> *Method*: `GET, POST`<br>
> *Description*: List or add reviews to the product<br>
> *Request Parameters*:<br>
> - `name`: Name of the user.<br>
> - `description`: The comment about the product.<br>

> ### Collection
> *URL*: `/store/collections`<br>
> *Method*: `GET, POST`<br>
> *Description*: List or add collections<br>
> *Request Parameters*:<be>
> - `title`: The title of the collection.<br>
> ---
> *URL*: `/store/collections/<id>`<br>
> *Method*: `GET, PUT, PATCH, DELETE`<br>
> *Description*: View, update or delete a collection<br>
> *Request Parameters*:<br>
> - `title`: The title of the collection.<br>

> ### Cart
> *URL*: `/store/carts`<br>
> *Method*: `POST`<br>
> *Description*: Create a cart<br>
> *Request Parameters*:<br>
>  - none<br>
> ---
> *URL*: `/store/carts/<id>`<br>
> *Method*: `GET, DELETE`<br>
> *Description*: View or delete a cart<br>
> *Request Parameters*:<br>
> - none<be>
> ---
> *URL*: `/store/carts/<id>/items`<br>
> *Method*: `GET, POST`<br>
> *Description*: List all cart items or add them<br>
> *Request Parameters*:<br>
> - `product_id`: The id of the product.<br>
> - `quantity`: How much u wanna add.<br>
> ---
> *URL*: `/store/carts/<id>/items/<id>`<br>
> *Method*: `GET, PATCH, DELETE`<br>
> *Description*: View, update or delete the product inside the cart<br>
> *Request Parameters*:<br>
> - `quantity`: How much u wanna add.<br>

> ### Customer
> *URL*: `/store/customers`<br>
> *Method*: `GET`<br>
> *Description*: List all the customers<br>
> *Request Parameters*:<br>
>  - none<br>
> ---
> *URL*: `/store/customers/<id>`<br>
> *Method*: `GET, PUT`<br>
> *Description*: View or update a customer<br>
> *Request Parameters*:<br>
> - `product_id`: The id of the product.<br>
> - `Birth date`: Birth date<br>
> - `Membership`: Membership (Gold, Silver, Bronze)<br>

> ### Order
> *URL*: `/store/orders`<br>
> *Method*: `GET, POST`<br>
> *Description*: List or create orders<br>
> *Request Parameters*:<br>
> - `cart_id`: The id of the cart contains the products.<br>
> ---
> *URL*: `/store/orders/<id>`<br>
> *Method*: `GET, PATCH, DELETE`<br>
> *Description*: View or update an order item<br>
> *Request Parameters*:<br>
> - `payment_status`: The status of the payment (Pending, Complete, Failed)<br>

> ### Auth
> *URL*: `/auth/users`<br>
> *Method*: `GET, POST`<br>
> *Description*: List or create user accounts<br>
> *Request Parameters*:<br>
> - `username`: Username for the account.<br>
> - `password`: Password.<br>
> - `email`: User Email.<br>
> - `first_name` (optional): User name.<br>
> - `last_name` (optional): User last name.<br>
> ---
> *URL*: `/auth/users/me`<br>
> *Method*: `GET, PUT`<br>
> *Description*: View or update an user profile<br>
> *Request Parameters*:<br>
> - `email`: User Email.<br>
> - `first_name`: User name.<br>
> - `last_name`: User last name.<br>
> ---
> *URL*: `/auth/jwt/create`<br>
> *Method*: `POST`<br>
> *Description*: Authenticate a user and generate a JWT token<br>
> *Request Parameters*:<br>
> - `username`: Username for the account.<br>
> - `password`: Password.<br>

## Contact
If you have any questions or encounter issues, please contact our support team at support@rash-store.com.
