Cargo Stowage Management System


Overview
The Cargo Stowage Management System is a Python-based application developed using FastAPI to optimize cargo stowage processes. It provides efficient APIs for managing cargo placement, retrieval, waste identification, and time simulation while ensuring secure and scalable operations. The system integrates seamlessly with a frontend for user interaction and supports Docker-based deployment.

Features
Core Functionalities
Placement Recommendations:

-Optimizes cargo placement based on priority, dimensions, and preferred zones.

-Handles space constraints and suggests rearrangements.

-Item Search and Retrieval:

-Locates items based on their ID or name.

-Calculates retrieval steps considering obstructions.


Waste Management:

-Identifies expired or depleted items.

-Suggests disposal plans for undocking.


Time Simulation:

-Simulates usage and expiration of items over time.

-Supports "Next Day" and "Fast Forward X Days" functionality.


Import/Export APIs:

-Allows importing items and containers via CSV files.

-Exports current arrangements in CSV format.


Logging API:

-Tracks all actions performed (placement, retrieval, rearrangement, disposal).


Technologies Used
-Backend: FastAPI

-Frontend: HTML, CSS, JavaScript

-Database: SQLite

-Containerization: Docker


Encryption: 

-Cryptography library for sensitive data

-Testing Tools: Postman, Swagger UI

Setup Instructions
Backend Setup

Clone the repository:
(bash)
git clone <repository-url>
cd Cargo_Stowage_Management_System

Create a virtual environment and activate it:
(bash)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Install dependencies:
(bash)
pip install -r requirements.txt

Run the FastAPI application locally:
(bash)
uvicorn main:app --host 0.0.0.0 --port 8000

Access Swagger UI for testing APIs:
http://localhost:8000/docs

Frontend Setup
Open the index.html file in a browser.

Ensure the backend is running on http://localhost:8000.

Interact with the form to test cargo placement recommendations.

Docker Deployment
Build Docker Image:
(bash)
docker build -t cargo-stowage .

Run Docker Container:
(bash)
docker run --network=host cargo-stowage

Access the application at:
http://localhost:8000/docs


API Endpoints
Placement Recommendations (POST /api/placement)
Input: Items and containers data in JSON format.

Output: Optimal placement recommendations and rearrangements.

Item Search (GET /api/search)
Input: itemId or itemName.

Output: Item location and retrieval steps.

Waste Identification (GET /api/waste/identify)
Output: List of expired or depleted items.

Time Simulation (POST /api/simulate/day)
Input: Number of days to simulate.

Output: Updated item statuses.

Import Items (POST /api/import/items)
Input: CSV file containing item data.

Output: Import success status.

Export Arrangement (GET /api/export/arrangement)
Output: Current arrangement in CSV format.


Security Features
Data encryption using the Cryptography library for sensitive fields (e.g., item names, expiry dates).

HTTPS support with SSL certificates (key.pem and cert.pem).

CORS middleware to allow secure frontend-backend communication.


Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Commit your changes (git commit -m "Add feature").

Push to your branch (git push origin feature-name).

Submit a pull request.



Collaborators:
1. AnuTris
2. Menon71
3. KanavBh29
