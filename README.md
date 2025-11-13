# 🛍️ Microservices E-Commerce Demo – Full Stack (Hybrid: Local Frontend + Dockerized Backend)

## 🚀 Overview

This project demonstrates a **microservices-based e-commerce system** where:
- **Three FastAPI backend services** (User, Product, Order) each run in **separate containers**.  
- Each service has its **own MySQL database** for complete data isolation.  
- An **Nginx reverse proxy** serves as the central **API Gateway**, routing all `/api/...` requests to the correct backend service.  
- The **frontend** runs **locally (not containerized)** and interacts with the backend through Nginx.  

---

## 🧠 Architecture Overview

```
[ Local Frontend (localhost:3000) ]
           |
           v
[ Nginx API Gateway (localhost:80) ]
           |
  ┌────────┼────────┐
  v        v        v
User   Product   Order  (FastAPI, ports 8001/2/3)
 |        |        |
MySQL   MySQL   MySQL
```

---

## ✨ Features

- **True Microservices Design:** Each business domain (User, Product, Order) runs independently.  
- **Dedicated Databases:** Each service has its own MySQL database with persistent Docker volumes.  
- **Central API Gateway:** Nginx handles routing and API exposure securely via port `80`.  
- **Frontend Flexibility:** Frontend runs locally for rapid UI development and hot reload.  
- **FastAPI Power:** Async Python APIs with built-in Swagger docs.  
- **One-Command Backend Setup:** Bring up all backend components with Docker Compose.  

---

## 📁 Folder Structure

```
microservices-project/
├── docker-compose.yml
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── user-service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       └── ...
├── product-service/
│   ├── Dockerfile
│   └── app/
│       └── main.py
├── order-service/
│   ├── Dockerfile
│   └── app/
│       └── main.py
├── frontend/           # Local (not containerized)
│   ├── index.html
│   ├── scripts/
│   └── styles/
└── README.md
```

---

## 🧰 Prerequisites

- **Docker** ≥ 20.10  
- **Docker Compose** ≥ 1.29  
- **Python/Node (optional)** if developing the frontend locally  
- **OS:** Linux / macOS / Windows (WSL2 recommended)  

---

## ⚙️ Setup & Run

### Step 1. Start the Backend (Dockerized)

```bash
docker-compose up --build -d
```

Wait until all containers are healthy:
```bash
docker-compose ps
```

### Step 2. Run the Frontend Locally

If it’s a simple static app:
```bash
cd frontend
python3 -m http.server 3000
```
Or, if it’s a Node-based app:
```bash
npm install
npm start
```

---

## 🌐 Access Points

| Component | URL | Description |
|------------|-----|-------------|
| **Frontend** | [http://localhost:3000](http://localhost:3000) | Local static UI |
| **Nginx Gateway** | [http://localhost](http://localhost) | Routes to backend services |
| **User Service Docs** | [http://localhost:8001/docs](http://localhost:8001/docs) | FastAPI Swagger |
| **Product Service Docs** | [http://localhost:8002/docs](http://localhost:8002/docs) | FastAPI Swagger |
| **Order Service Docs** | [http://localhost:8003/docs](http://localhost:8003/docs) | FastAPI Swagger |

---

## 🔗 Example API Routes

| Service | Endpoint | Method | Description |
|----------|-----------|--------|-------------|
| User | `/api/v1/users/` | POST | Create user |
| User | `/api/v1/users/` | GET | List users |
| Product | `/api/v1/products/` | POST | Add product |
| Product | `/api/v1/products/` | GET | List products |
| Order | `/api/v1/orders/` | POST | Create order |
| Order | `/api/v1/orders/` | GET | List orders |

---

## ⚙️ Environment Configuration

Each microservice reads environment variables defined in `docker-compose.yml`, including:
- `DATABASE_HOST`, `DATABASE_USER`, `DATABASE_PASSWORD`
- `DATABASE_NAME`
- `SERVICE_PORT`

You can modify them directly in the compose file.

---

## 🧑‍💻 Development Tips

- Rebuild a single service:
  ```bash
  docker-compose build user-service
  docker-compose restart user-service
  ```
- Tail logs:
  ```bash
  docker-compose logs -f product-service
  ```
- Rebuild everything:
  ```bash
  docker-compose down
  docker-compose up --build -d
  ```

---

## 🧩 Troubleshooting

| Issue | Possible Fix |
|--------|---------------|
| Frontend can’t reach backend | Ensure frontend calls use `http://localhost/api/...` (not service ports) |
| 502 Bad Gateway | Check container health with `docker-compose ps` |
| Database errors | Wait 1–2 mins after first boot; MySQL may need init time |
| Port conflict | Stop old containers: `docker-compose down` |

---

## 📘 FAQ

> **Why is the frontend local?**  
> To enable hot-reload and quick UI iteration without rebuilding containers.  

> **Can I containerize it later?**  
> Yes! Add a `Dockerfile` in `/frontend` and expose it via Nginx easily.  

> **How is data persisted?**  
> Each database uses a Docker volume for persistence.  

---

## 📄 License

MIT License © 2025 Saurabh Yadav
