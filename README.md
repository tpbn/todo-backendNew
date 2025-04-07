# 📝 To-Do Application (React + Django REST API)

A simple full-stack to-do list app with:

Backend: https://todo-backend0.onrender.com
Frontend: https://react-todo-app-6o6a.onrender.com

---

## API Endpoints

Base URL: `https://todo-backend0.onrender.com/api/tasks/`

| Method | Endpoint              | Description            |
|--------|------------------------|------------------------|
| GET    | /api/tasks/           | Fetch all tasks        |
| POST   | /api/tasks/           | Create a new task      |
| PATCH  | /api/tasks/<id>/      | Update a task by ID    |
| DELETE | /api/tasks/<id>/      | Delete a task by ID    |

---

### 📨 Sample Payloads

- **POST/PATCH:**

```json
{
  "title": "Buy groceries",
  "completed": false
}
