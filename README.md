# 🚀 AI Chat Workspace

A production-grade, highly extensible AI chat web application inspired by ChatGPT, Open WebUI, and modern AI operating systems. It is built from the ground up to offer low-latency streaming responses, immediate switching between local and cloud providers, an extensible tool calling architecture, and a premium modern user experience.

---

## ✨ Features

- **🌓 Premium Dark Mode UI**: A fully-responsive, high-contrast user interface styled using **Tailwind CSS v4** and fluid, micro-animated transitions powered by **Framer Motion**.
- **🔄 Multi-Provider Orchestration**: Switch dynamically between local and cloud models.
  - **Local Models**: Preconfigured to integrate seamlessly with **LM Studio** (tested on `Stheno` and `Qwen 2.5`) and other OpenAI-compatible local APIs.
  - **Cloud Providers**: Integrates with **Google AI Studio (Gemma 4)** and **OpenAI APIs** via OpenAI's standardized SDK formats.
- **⚡ SSE Streaming Engine**: Real-time token streaming using high-performance Server-Sent Events (SSE) on FastAPI, rendering instantly on the frontend.
- **🛠️ Extensible Tool Registry**: Modular tool architecture starting with a built-in **Web Search** tool blueprint, facilitating easy additions of customized agentic tools.
- **🗄️ Structured State & Storage**: 
  - **Frontend**: Global responsive application states managed using **Zustand** with persistent client storage.
  - **Backend**: Data architecture defined via **SQLAlchemy** ready for local **SQLite** (or easily migratable to PostgreSQL/MySQL).

---

## 🏛️ Project Architecture

The application is split into two cleanly separated microservices within a single workspace:

```
AI App/
├── backend/            # FastAPI Backend Service (Python 3.10+)
│   ├── app/
│   │   ├── api/        # REST Route mappings (SSE stream completions)
│   │   ├── core/       # Global Pydantic settings & database engines
│   │   ├── database/   # Declarative models (Conversations & Messages)
│   │   ├── providers/  # Abstracted LLM clients (OpenAI, Local, Google)
│   │   ├── tools/      # Modular tools & registry systems
│   │   └── main.py     # FastAPI entry point
│   ├── venv/           # Python virtual environment
│   └── requirements.txt# Backend dependency manifest
│
├── frontend/           # Next.js Frontend App (React 19, TypeScript)
│   ├── src/
│   │   ├── components/ # Atomic UI components (ChatArea, Sidebar, Settings)
│   │   ├── lib/        # Tailwind class merges & visual helpers
│   │   ├── store/      # Zustand state store
│   │   └── app/        # Next.js App router pages
│   └── package.json    # Frontend dependency manifest
│
├── package.json        # Root Workspace Configuration (NPM Scripts)
├── run-dev.js          # Root process orchestrator & runner
└── README.md           # Project Documentation
```

---

## ⚙️ Configuration & Environment

To use cloud models, create a `.env` file in the `backend/` directory based on the provided template:

```bash
cd backend
cp .env.example .env
```

Open `backend/.env` and supply your API keys:
```env
# Provider API Keys
GOOGLE_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# Local Provider Config (e.g. LM Studio server address)
LOCAL_PROVIDER_URL=http://localhost:1234/v1

# Database Configuration (defaults to SQLite local workspace file)
DATABASE_URL=sqlite:///./workspace.db
```

---

## 🚀 Getting Started

### The 1-Step Unified Runner (Recommended)

Start both servers concurrently with a single command from the project root:

```bash
npm run dev:all
```

This custom runner automatically:
1. Spawns the **FastAPI Backend** (`http://localhost:8000`) using the virtual environment's internal executables.
2. Spawns the **Next.js Frontend** (`http://localhost:5000`).
3. Formats and color-codes console logs into a single window.
4. Cleanly handles graceful shutdown of both services upon pressing `Ctrl + C`.

---

### Running Separately (Alternative)

If you prefer running the components in separate terminal sessions:

#### 📂 1. Run the Backend

```bash
cd backend
# Activate the virtual environment
.\venv\Scripts\activate   # On Windows (PowerShell: Activate.ps1)
# Install dependencies
pip install -r requirements.txt
# Run the FastAPI ASGI server
uvicorn app.main:app --reload --port 8000
```

#### 📂 2. Run the Frontend

```bash
cd frontend
# Run the dev server
npm run dev
```

Your web client will be available at **`http://localhost:5000`**.

---

## 🔌 Extensibility: Adding a Custom Tool

Adding a tool to your AI Workspace is exceptionally simple:

1. **Create the Tool**: Create a new class extending `BaseTool` in `backend/app/tools/`:
   ```python
   # backend/app/tools/weather.py
   from app.tools.base import BaseTool

   class WeatherTool(BaseTool):
       name = "get_weather"
       description = "Get current weather details for a specific city."

       async def execute(self, city: str) -> str:
           # Call your external weather API here
           return f"The current weather in {city} is sunny and 22°C."
   ```

2. **Register the Tool**: Add it to the registry in `backend/app/tools/registry.py`:
   ```python
   # Import the tool
   from app.tools.weather import WeatherTool
   
   # Add to the registry inside get_all_tools() or initialization logic
   ```

---

## 📄 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
