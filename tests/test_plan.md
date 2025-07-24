# 🧪 Test Plan – React & Node.js Web App Automation

## 1. What Is Being Tested

This test suite validates the key functional flows of a React-based frontend and Node.js backend application. The app allows users to log in and manage a list of items (e.g., a todo list).

---

## 2. Test Coverage Areas

### UI Tests (Selenium):
- Login with valid credentials
- Login with invalid credentials
- Adding a new item
- Editing an existing item
- Deleting an item

### API Tests (Requests + Pytest):
- `POST /login`: Auth with valid/invalid credentials
- `GET /items`: Retrieve all items
- `POST /items`: Create item (positive/negative)
- `PUT /items/:id`: Update item (valid/invalid ID)
- `DELETE /items/:id`: Delete item (valid/invalid ID)

---

## 3. Tools Used and Why

| Tool           | Purpose                         |
|----------------|---------------------------------|
| Selenium       | UI automation in real browser   |
| Requests       | Lightweight HTTP API testing    |
| Pytest         | Test runner with fixture support|
| ChromeDriver   | Controlled browser for UI tests |

---

## 4. How to Run the Tests

Ensure both frontend and backend servers are running:
- Backend: `http://localhost:5000`
- Frontend: `http://localhost:3000`

Then run:

```bash
# Run UI tests
pytest ui_tests/

# Run API tests
pytest api_tests/
```

---

## 5. Assumptions and Limitations

- Chrome is installed and accessible on the system
- `admin` / `1234` is a valid login credential
- No persistent database — tests assume a reset or isolated state
- Only Chrome browser is supported (no cross-browser coverage)