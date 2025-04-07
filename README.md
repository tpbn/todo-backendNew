# To-Do Application

Deployed Links:

Backend: https://todo-backend0.onrender.com

Frontend: https://react-todo-app-6o6a.onrender.com

---

### API Endpoints

**Base URL:**  
`https://todo-backend0.onrender.com/api/tasks/`

| Method | Endpoint             | Description           |
|--------|----------------------|-----------------------|
| GET    | /api/tasks/          | Fetch all tasks       |
| POST   | /api/tasks/          | Create a new task     |
| PATCH  | /api/tasks/<id>/     | Update a task by ID (e.g., `/api/tasks/2/`) |
| DELETE | /api/tasks/<id>/     | Delete a task by ID (e.g., `/api/tasks/1/`) |

---

**Request Format** for POST and PATCH:  
```json
{
  "title": "Buy groceries",
  "completed": false
}
