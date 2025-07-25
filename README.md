# Test Automation Framework – React & Node.js Application

This repository contains a complete test automation framework for a simple full-stack web application with a React frontend and a Node.js backend. The framework includes both UI tests (via Selenium WebDriver) and API tests (via Python requests and pytest), designed to validate core functionality such as authentication and CRUD operations.

---

## 📌 Project Overview

The application under test allows users to:
- Log in with credentials
- Create, edit, and delete items

This test suite verifies those core flows through both the UI and backend APIs.

---

## 🧪 Test Coverage

### UI Automation (Selenium + Pytest)
- Valid login
- Invalid login
- Add item
- Edit item
- Delete item

### API Tests (Requests + Pytest)
- `POST /login` – valid and invalid credentials
- `GET /items` – fetch all items
- `POST /items` – create new item
- `PUT /items/:id` – update existing item
- `DELETE /items/:id` – remove item

---

## 🧰 Tech Stack

- Python 3.8+
- Selenium WebDriver (Chrome)
- Pytest
- Requests
- Automatic ChromeDriver management
- Node.js backend
- React frontend

---

# 🚀 Getting Started
## first of all need to configure the React application(Frontend && Backend)
## ⚛️ Running the React Frontend

Before running the UI tests, you must start the React frontend application.

### 1. Navigate to the frontend folder:

```bash
cd frontend
```

### 2. Install frontend dependencies:

```bash
npm install
```

### 3. Start the React development server:

```bash
npm start
```

The application should now be available at:

```
http://localhost:3000
```

## ️ Running the Backend

Before running the tests, you must start the Backend server.

### 1. Navigate to the backend folder:

```bash
cd backend
```

### 2. Install backend dependencies:

```bash
npm install
```

### 3. Start the backend server:

```bash
npm start
```

The application should now be available at:

```
http://localhost:5000
```

Make sure this is running before launching the tests.

### 1. Clone and Install Dependencies

```bash
cd tests
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

### 2. Ensure the Application is Running

Start your backend server at:
```
http://localhost:5000
```

Start your React frontend at:
```
http://localhost:3000
```

### 3. Execute the Tests

#### Run all UI tests:
```bash
pytest ui_tests/ -v
```

#### Run all API tests:
```bash
pytest api_tests/ -v
```

---

## 📁 Project Structure

```
selenium_ui_tests/
├── api_tests/              # API test classes
├── pages/                  # Page Object Model classes for UI
├── ui_tests/               # UI test classes
├── utils/                  # Driver setup and management
├── conftest.py             # Pytest fixtures
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Notes

- The test suite automatically downloads and uses a compatible 64-bit ChromeDriver for consistency.
- Page Object Model (POM) pattern is used to separate test logic from UI element locators.
- No external test data or configuration files are required.
- All tests are self-contained and designed for local execution.

