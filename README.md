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
> *URL*: `/store/products/`<br>
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

> ### Collection
> *URL*: `/store/collections/`<br>
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
> *URL*: `/store/carts/`<br>
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
> *Description*: List all the products in the cart or add them<br>
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
> *URL*: `/store/customers/`<br>
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


## Contact
If you have any questions or encounter issues, please contact our support team at support@rash-store.com.
