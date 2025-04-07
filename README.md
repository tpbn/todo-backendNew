# To-Do Application

Deployed Links:

Backend:  https://todo-backend0.onrender.com

Frontend: https://react-todo-app-6o6a.onrender.com

---

**Base URL:**  
`https://todo-backend0.onrender.com/api/tasks/`

### API Endpoints

| Method | Endpoint             | Description               |
|--------|----------------------|---------------------------|
| GET    | `/api/tasks/`        | Fetch all tasks           |
| POST   | `/api/tasks/`        | Create a new task         |
| PATCH  | `/api/tasks/<id>/`   | Update a task by ID       |
| DELETE | `/api/tasks/<id>/`   | Delete a task by ID       |

> Replace `<id>` with the specific task's ID.  
> Example: `PATCH /api/tasks/2/`

---

### Request Body Format (POST / PATCH)

```json
{
  "title": "Do laundry",
  "completed": false
}
```

### Sample Response

```json
{
  "id": 2,
  "title": "Do laundry",
  "completed": false
}
```

---
