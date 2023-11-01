
![FastAPI Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

# FastAPI Wikipedia Application

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10.11 is installed

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Monu25Verma/wikepedia_fastapi.git
    cd WIKIPEDIA_FASTAPI
    ```

2. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI application:

    ```bash
    uvicorn wikipediaProject:app --host 0.0.0.0 --port 8000 --reload
    ```

    This will start the application on `http://localhost:8000` and automatically reload it when you make changes to the code.

2. Open your web browser and navigate to [http://localhost:8000](http://localhost:8000) to access the FastAPI application.

## API Documentation

The API documentation is automatically generated and provided by FastAPI. You can access it at [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redoc).

## Directory Structure

- `wikipediaProject.py`: The main FastAPI application.
- `requirements.txt`: Contains the project dependencies.
- `.env`: Project Environment Variables
- `README.md`: This file.

## Screenshots
- Create Dataset using Wikipedia Data
![Create Dataset](images\postinput1.png)


- Retrieve All Dataset from Database
![Retrieve All Dataset](images\getall_data3.jpg)


- Retrieve Single Desired Dataset from Database
![Retrieve Single Dataset](images\get_singledata.png)

## Assumptions

- The dataset we will create will be based on user given title which will at backend make api call to wikipedia to get data and serializing it to specific data model format to store.

- Retrieval of data was made based on 2 types:
    - Retrieving all data that is inside DB.
    - Retrieving dataset based on title request made by User.

## Author

- Monu Verma
- GitHub: [Monu25Verma](https://github.com/Monu25Verma)