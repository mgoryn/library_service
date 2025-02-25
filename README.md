---

# Library Service

A Django-based system for managing a library, including books, users, borrowings, and payments.

## Table of Contents

1. [About the Project](#about-the-project)
2. [Features](#features)
    - [Core Features](#core-features)
    - [Borrowings and Payments](#borrowings-and-payments)
    - [Technical Features](#technical-features)
3. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the Application](#running-the-application)
4. [Usage](#usage)
5. [API Features](#api-features)
6. [Contact](#contact)

---

## About the Project

**Library Service** is a comprehensive Django-based application that simplifies the management of library operations. It
includes functionality for managing books, users, borrowings, payments, and notifications. This system helps libraries
efficiently track the borrowing status of books, handle payments for overdue items, and keep users informed.

---

## Features

### Core Features

- **Book Management**: Manage books in the library with full CRUD functionality.
- **User Management**: Manage library users, including adding, updating, and deleting user accounts.
- **Borrowing Management**: Track which books are borrowed by which users and manage the borrowing process, including
  return dates.
- **Payment System**: Handle payments for overdue books and fines.
- **Notifications**: Send notifications about overdue books, successful payments, and new borrowings via Telegram (
  integration with the Telegram API).

### Borrowings and Payments

Borrowings are a central part of the system, allowing users to borrow books for a defined period and ensuring that
overdue books are tracked and managed effectively. The system also includes payment handling for overdue books and
fines.

- **Borrowing Process**: A user can borrow a book by specifying the start and due dates. The system creates a borrowing
  entry and associates it with the user and the book.
- **Overdue Handling**: If a book is not returned by the due date, it becomes overdue. The system automatically tracks
  overdue books and triggers notifications.
- **Payment for Overdue Books**: Once a book is returned late, the system calculates a daily fine and provides users
  with a way to pay for the overdue period. Payments are processed, and statuses are updated accordingly.
- **Manual Payment Updates**: Administrators can manually update the status of payments and handle exceptions in the
  system.

### Technical Features

- **REST API**: Fully functional API to interact with the library system, including managing books, users, borrowings,
  and payments.
- **JWT Authentication**: Secure user authentication using JSON Web Tokens (JWT).
- **Asynchronous Notifications**: Notifications about borrowings, overdue books, and payments are sent asynchronously
  using Django Celery.
- **Scalable Design**: The system is built using Django, designed to scale as your library grows.

---

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

- Docker & Docker Compose installed on your system.
- `git` for cloning the repository.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mgoryn/library_service.git
    ```

2. Navigate to the project directory:

    ```bash
    cd library_service
    ```

---

### Running the Application

To run the project using Docker Compose:

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

3. Apply the database migrations:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. Create a superuser for accessing the admin panel:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5. Access the application in your browser at:

    ```
    http://127.0.0.1:8000
    ```

---

## Usage

- Navigate through the app to manage books, users, borrowings, and payments.
- Use the admin interface to manage records or make manual updates for borrowings and payments.
- Test the notification system using the API to send messages about overdue books, new borrowings, and payment updates.

---

## API Features

The Library Service API offers a flexible and easy-to-use interface for interacting with the system programmatically.
Below are the key features and endpoints:

### Core API Endpoints

#### Books

- **List all books**.
- Retrieve, create, update, and delete book information.

#### Users

- **Manage users**: Create, update, or delete user accounts.

#### Borrowings

- **View current borrowings**: Track all borrowings, including active and overdue.
- **Create, update, or delete borrowings**: Borrow, return, or cancel books.
- **Track overdue books**: Automatically identifies overdue books and triggers notifications.

#### Payments

- **View and process payments**: Track payments for overdue books and fines.
- **Create and update payment statuses**: Admin can manually update payment statuses.

#### Notifications

- **Send notifications**: Notify users about overdue books, new borrowings, and successful payments.

---

### Key Features of the API

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations for all entities (books, users, borrowings,
  etc.).
- **Filtering and Searching**: Query endpoints with filters like user ID, book title, due date, payment status, etc.
- **Authentication**: Secure access using JWT with role-based permissions.
- **Asynchronous Notifications**: Background tasks for sending notifications.
- **Pagination**: Large datasets are paginated for better performance.
- **Error Handling**: Detailed error messages and HTTP status codes for all requests.
- **Scalability**: Built with Django, designed to handle increased workloads.

---

## Contact

For questions or suggestions, feel free to reach out:

- **Author**: [Mykhailo](https://github.com/mgoryn)
- **Project Link**: [GitHub Repository](https://github.com/mgoryn/library_service)

---

We hope this project helps streamline your library management process!

---
