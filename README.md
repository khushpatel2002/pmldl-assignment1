# pmldl-assignment1

# Boston Housing Price Prediction

This project deploys a machine learning model to predict Boston housing prices using FastAPI for the backend and Streamlit for the frontend. The backend provides an API for making predictions, while the frontend allows users to interact with the model through a web interface.

## Project Structure

```
.
├── Makefile                # Optional: Build and clean commands
├── README.md               # Project documentation
├── code                    # Main code directory
│   ├── datasets            # Dataset-related scripts and data
│   │   └── download_dataset.py
│   ├── deployment          # Deployment configuration
│   │   ├── api             # FastAPI code
│   │   │   ├── Dockerfile  # Dockerfile for FastAPI
│   │   │   ├── boston      # API endpoints and models
│   │   │   │   ├── endpoints.py
│   │   │   │   └── models.py
│   │   │   ├── core        # Core configuration files
│   │   │   │   ├── config.py
│   │   │   ├── files       # Stored models and files
│   │   │   │   └── lin_model.joblib
│   │   │   ├── main.py     # FastAPI main application
│   │   │   └── requirements.txt  # FastAPI dependencies
│   │   ├── app             # Streamlit application
│   │   │   ├── Dockerfile  # Dockerfile for Streamlit
│   │   │   ├── app.py      # Streamlit app for frontend
│   │   │   └── requirements.txt  # Streamlit dependencies
│   │   └── docker-compose.yaml  # Docker Compose configuration
│   └── models              # Model training scripts and files
│       └── train_model.py  # Script to train and save models
├── data                    # Data directory
│   └── boston_housing.csv  # Boston housing dataset
└── models
    └── boston_housing_model.joblib  # Trained model file
```

## Requirements

- Docker
- Docker Compose

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/khushpatel2002/pmldl-assignment1.git
cd pmldl-assignment1
```

### 2. Build and Run Using Docker Compose

The project uses Docker Compose to build and manage both FastAPI and Streamlit services. To build and start the containers, run:

```bash
docker-compose up --build
```

### 3. Access the Applications

- **FastAPI**: Once the containers are up, FastAPI will be accessible at `http://localhost:2200`. You can check the API documentation at `http://localhost:2200/docs`.
  
- **Streamlit**: The Streamlit app will be accessible at `http://localhost:8501`. This app provides a user interface to input features and view predictions.

## API Usage

You can interact with the FastAPI server using tools like `curl`, `Postman`, or directly through the `/api/v1/docs` Swagger UI.

### Example Request

**Endpoint**: `/price/model/inference`

**Method**: `POST`

**Payload**:

```json
{
  "RM": 6.0,
  "PTRATIO": 18.0,
  "LSTAT": 12.5
}
```

**Response**:

```json
{
  "query": {
    "RM": 6.0,
    "PTRATIO": 18.0,
    "LSTAT": 12.5
  },
  "price": 24000.0
}
```

## Streamlit Application

The Streamlit app provides an easy-to-use interface for users to input the features `RM`, `PTRATIO`, and `LSTAT` and get predictions from the backend FastAPI service.

### Usage

1. Open the Streamlit application at `http://localhost:8501`.
2. Input the feature values:
   - Average number of rooms per dwelling (RM)
   - Pupil-teacher ratio by town (PTRATIO)
   - % lower status of the population (LSTAT)
3. Click on the "Predict House Price" button to get the predicted house price.

## Dockerfile and Docker Compose Explanation

### FastAPI Dockerfile (`deployment/api/Dockerfile`)

This Dockerfile sets up a Python environment with FastAPI and its dependencies, copies the necessary files, and runs the FastAPI server using Uvicorn.

### Streamlit Dockerfile (`deployment/app/Dockerfile`)

This Dockerfile sets up a Python environment for Streamlit, copies the Streamlit application files, and starts the Streamlit server.

### Docker Compose (`docker-compose.yaml`)

The Docker Compose file defines two services:
- **fastapi-app**: The backend FastAPI server.
- **streamlit-app**: The frontend Streamlit application.

Both services are connected through a shared network, allowing the Streamlit app to communicate with the FastAPI app using the service name `fastapi-app`.

## Troubleshooting

If you encounter issues while building or running the containers:

1. Ensure Docker and Docker Compose are installed and running.
2. Check for any port conflicts. Modify the exposed ports in the `docker-compose.yaml` if necessary.
3. Look at the container logs using `docker-compose logs` to identify potential errors.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [Docker](https://www.docker.com/)