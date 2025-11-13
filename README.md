# 🛍️ Microservices E-Commerce Project – Full Stack (FastAPI + MySQL + Nginx + Docker Compose)

## 🚀 Overview

This project demonstrates a **production-style microservices-based e-commerce system** built using modern cloud-native principles.  
It includes a **frontend**, **API gateway**, and **three isolated backend services** — all orchestrated via Docker Compose.

---

## 🧱 Architecture

```
[ Frontend (port 3000) ]
        │
        ▼
[ Nginx API Gateway (port 80) ]
        │
 ┌──────┼────────────┐
 ▼      ▼             ▼
User   Product       Order  (FastAPI, ports 8001/2/3)
 │       │             │
MySQL   MySQL        MySQL
```

- **Frontend** → Runs on port `3000` (local browser or containerized)
- **Nginx Gateway** → Acts as a reverse proxy for all backend APIs (`/api/v1/...`)
- **FastAPI Microservices** → Independent services for `User`, `Product`, and `Order`
- **MySQL Databases** → One per microservice, with isolated schemas and persistent Docker volumes

---

## ✨ Features

- 🧩 **Modular Microservices**: Each business domain (User, Product, Order) runs independently.  
- 🗄️ **Dedicated Databases**: Three MySQL instances (one per service) ensure full data isolation.  
- ⚙️ **Centralized API Gateway**: Nginx handles routing and simplifies frontend-backend communication.  
- ⚡ **FastAPI-powered APIs**: High-performance async backend with auto-generated Swagger docs.  
- 🐳 **Container Orchestration**: All components networked and launched via Docker Compose.  
- 🌍 **Auto Environment Detection**: Frontend automatically detects whether it’s running locally or on a server (no config changes needed).  

---

## 🗂 Folder Structure

```
microservices-project/
├── docker-compose.yml
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   └── (assets, scripts, styles)
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── user-service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── models.py
│       └── routers/
├── product-service/
│   └── (similar structure)
├── order-service/
│   └── (similar structure)
└── README.md
```

---

## 🧰 Prerequisites

- **Docker** ≥ 20.10  
- **Docker Compose** ≥ 1.29  
- **Ports required:** `80`, `3000`, `8001–8003`, `3306–3308`  
- **Recommended RAM:** ≥ 2GB  

---

## ⚙️ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourname/microservices-project.git
cd microservices-project
```

### 2️⃣ Build & Start All Containers

```bash
docker-compose up --build -d
```

Wait for the containers to initialize (check with):
```bash
docker-compose ps
```

### 3️⃣ Access the Application

| Component | URL | Description |
|------------|-----|-------------|
| 🖥️ Frontend | [http://localhost:3000](http://localhost:3000) | Simple demo UI |
| 🌐 API Gateway (Nginx) | [http://localhost](http://localhost) | Central routing for APIs |
| 🧩 User Service | [http://localhost:8001/docs](http://localhost:8001/docs) | FastAPI Swagger |
| 📦 Product Service | [http://localhost:8002/docs](http://localhost:8002/docs) | FastAPI Swagger |
| 🛒 Order Service | [http://localhost:8003/docs](http://localhost:8003/docs) | FastAPI Swagger |

---

## 🧩 Example API Endpoints

| Service | Endpoint | Method | Description |
|----------|-----------|--------|-------------|
| User | `/api/v1/users/` | POST | Create new user |
| User | `/api/v1/users/` | GET | List all users |
| Product | `/api/v1/products/` | POST | Add product |
| Product | `/api/v1/products/` | GET | List all products |
| Order | `/api/v1/orders/` | POST | Create order |
| Order | `/api/v1/orders/` | GET | List orders |

All APIs are auto-documented in Swagger UI at `/docs`.

---

## 🌍 Frontend Configuration (Auto Environment Detection)

Your `frontend/index.html` automatically detects where it’s running:

```js
const hostname = window.location.hostname;
let API_BASE = '';

if (hostname === 'localhost' || hostname === '127.0.0.1') {
    API_BASE = 'http://localhost';
} else {
    API_BASE = `${window.location.protocol}//${window.location.hostname}`;
}
```

✅ Works automatically:
- Local: `http://localhost:3000` → API calls `http://localhost/api/...`  
- Server: `http://<public-ip>:3000` → API calls `http://<public-ip>/api/...`

No manual change required!

---

## 🧾 Environment Variables

Each service uses its own DB connection string:

| Service | Env Variable | Example |
|----------|--------------|----------|
| User | `DATABASE_URL` | `mysql+pymysql://user:password@user-db:3306/user_db` |
| Product | `DATABASE_URL` | `mysql+pymysql://user:password@product-db:3306/product_db` |
| Order | `DATABASE_URL` | `mysql+pymysql://user:password@order-db:3306/order_db` |

You can adjust these in `docker-compose.yml`.

---

## 🧑‍💻 Developer Workflow

| Task | Command |
|------|----------|
| Rebuild backend service | `docker-compose build user-service && docker-compose restart user-service` |
| View logs | `docker-compose logs -f nginx` |
| Stop all containers | `docker-compose down` |
| Rebuild everything clean | `docker-compose down -v && docker-compose up --build -d` |

---

## 🧠 Troubleshooting

| Issue | Cause | Solution |
|--------|--------|-----------|
| ❌ CORS errors | Duplicate headers | Ensure only FastAPI’s `CORSMiddleware` handles CORS (not Nginx) |
| 🕒 Databases unhealthy | MySQL still initializing | Wait 30–60 seconds |
| ⚠️ 502 Bad Gateway | Service not yet ready | Restart nginx: `docker-compose restart nginx` |
| ⚓ Port conflict | Port already in use | Stop previous Docker containers |

---

## 📘 FAQ

> **Q:** Why use separate MySQL instances?  
> **A:** Demonstrates real-world microservice data isolation.

> **Q:** Can I deploy this to AWS EC2?  
> **A:** Yes, it’s fully compatible. Just update security groups to allow ports 80 and 3000.

> **Q:** Can the frontend be containerized?  
> **A:** Yes. Add a Dockerfile in `/frontend` and connect it to the same Docker network.

> **Q:** How do I view API docs?  
> **A:** Visit `/docs` on any service port (8001–8003).

---

## 📄 License

MIT License © 2025 Saurabh Yadav

---

🎉 **You now have a complete microservices e-commerce stack running via Docker Compose.**
