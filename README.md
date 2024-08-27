# Handmade Crafts E-Commerce Platform

This project is part of an assessment to design and implement a core API endpoint for creating new products on an e-commerce platform for selling handmade crafts.

## Overview

The goal of this project is to develop a backend API that handles the creation of new products on an e-commerce platform. The API is designed to accept product details via POST requests, validate the data, store it in a database, and provide appropriate error messages if any issues arise.

## Technologies Used

- **Backend Framework:** Django REST Framework (DRF)
- **Database:** SQLite
- **Language:** Python 3.11.4

## Data Model

The core data models are the **Product** and **Category** models:

### Product

- **product_name:** A unique name for the product.
- **description:** A descriptive write-up for the product.
- **selling_price:** The price at which the product will be sold.
- **category:** A foreign key linking to the Category model.
- **created_at:** Timestamp for when the product was created.
- **edited_at:** Timestamp for when the product was last edited.

### Category

- **name:** The name of the category (e.g., Jewelry, Pottery).
- **is_active:** A boolean indicating if the category is active.

## API Endpoints

### Create Product

- **Endpoint:** `/products/create/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "product_name": "Handmade Jewelry",
    "description": "A beautiful handmade jewelry piece.",
    "selling_price": "100",
    "category": "Jewelry"
  }
## Response

- **Success:** `201 Created`
- **Error:** `400 Bad Request` with appropriate error message

## Validation and Error Handling

Validation is performed at both the serializer level and the database level to ensure that all required fields are present and that the data conforms to the expected formats.

- **Product Name:** Must be unique and not null.
- **Description:** Must not be  null.
- **Selling Price:** Must be a valid decimal value.
- **Category:** Must exist in the database; otherwise, a validation error is returned.

Error handling is implemented to catch and return meaningful messages, such as:

- **Category not found** if the provided category name does not exist.

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>

2. **Create a Virtual Environment:**
    
    python3 -m venv venv
    source venv/bin/activate

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run Migrations:**
    ```bash
    python3 manage.py migrate

5. **Run the Development Server:**
    ```bash
    python3 manage.py runserver


