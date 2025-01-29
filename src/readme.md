
**Project Description**

This project is a simple API built using Flask, a popular Python web framework. The API provides a single endpoint to retrieve a JSON response containing the current date and time, email, and GitHub URL.

**Setup Instructions**

To run the project locally, follow these steps:

1. Clone the repository using `git clone https://github.com/Prevz26/HNG-TASK-0.git`
2. Install the required dependencies using `pip install -r requirements.txt`
3. Run the application using `python src/app.py`
4. Open a web browser or an API tester and navigate to `http://localhost:5000/api/hng/backend/task0` to access the API endpoint

**API Documentation**

### Endpoint URL

* `GET /api/hng/backend/task0`

### Request/Response Format

* Request: GET
* Response: JSON object containing the current date and time, email, and GitHub URL

### Example Usage

* Using `curl` command: `curl http://localhost:5000/api/hng/backend/task0`
* Using a web browser: Open `http://localhost:5000/api/hng/backend/task0` in a web browser

**Example Response**

```json
{
  "email": "nkangprecious26@gmail.com",
  "current_datetime": "2025-01-29T10:27:10.987638+00:00Z",
  "github_url": "https://github.com/nkangprecious26"
}
```

**Backlink**

For more information on hiring Python developers, visit [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

