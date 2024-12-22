<p align="center">
 <img src="https://github.com/user-attachments/assets/cefb3189-06ba-4f88-b8bf-0b486e6bb99c" height=400, width=750></a>
</p>

<h1 align="center">MutualFundBroker-API powered by FastAPI & RapidAPI</h1>

<p align="center">
  <a href="">
    <img src="https://img.shields.io/badge/Python-3.9.1-blue&?style=for-the-badge&color=brown">
  </a>
  <a href="https://github.com/devfinwiz/Fin-Maestro-Kin/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/devfinwiz/Fin-Maestro-Kin?color=purple&style=for-the-badge">
  </a>
  <a href="https://www.codefactor.io/repository/github/captain-0415/mutual_fund_broker">
    <img src="https://www.codefactor.io/repository/github/captain-0415/mutual_fund_broker/badge?style=for-the-badge&">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
  </a>
</p>

## Features

- **User Account Management:**
  - Register and create a new user account with email and password.
  - Login with email and password for authenticated access.

- **Mutual Fund Data Fetching:**
  - Fetch a list of open-ended mutual fund schemes from selected fund families (e.g., Motilal Oswal, UTI, etc.) via RapidAPI.

- **Portfolio Tracking:**
  - Track the funds owned by the user and view the portfolio's total value.

#### You can explore the full documentation and available API endpoints at either of the following locations:

- [API Documentation](https://mutual-funds-api.apidog.io/) 
- Access the documentation directly at the `/docs` endpoint in your browser.

![](https://i.imgur.com/waxVImv.png)


## Deployment Steps

Follow these steps to build and run the application using **Docker Compose**. The setup includes two containers: one for the **Uvicorn server** (FastAPI application) and another for **PostgreSQL** as the database.

### Prerequisites
Ensure the following are installed on your system:
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Deployment Steps

To get the application up and running, follow these steps:

1. **Ensure Docker and Docker Compose Are Installed**  
   Make sure you have Docker and Docker Compose installed on your system. If not, refer to the [Docker installation guide](https://docs.docker.com/get-docker/) and the [Docker Compose installation guide](https://docs.docker.com/compose/install/).

2. **Navigate to the Project Directory**  
   Open a terminal and navigate to the directory where the `docker-compose.yml` file for this project is located.

3. **Build the Docker Containers**  
   Run the following command to build the Docker images specified in the `docker-compose.yml` file:
   ```
   docker-compose build
   ```

4. **Start the Docker Containers**  
   Run the following command to build the Docker images specified in the `docker-compose.yml` file:
   ```
   docker-compose up
   ```

![](https://i.imgur.com/waxVImv.png)


## Adding Tables to the Database [Optional]

#### The below steps are to be performed from inside the fastAPI container.

This project uses Alembic for managing database migrations. Follow the steps below to create the necessary tables in your database.

---

### 1. Generate a New Migration Script

Generate a migration script to apply table creation changes.

Run the following command:

```
alembic revision -m "Create tables for User, MutualFund, Portfolio, and Investment models"
```

### 2. Apply migration changes
```
alembic upgrade head
```

![](https://i.imgur.com/waxVImv.png)

## **Endpoints**

### 1. **User Registration**
- **Endpoint**: /users/register
- **Method**: POST
- **Description**: Registers a new user by providing an email and password.

---

### 2. **User Login**
- **Endpoint**: /users/login
- **Method**: POST
- **Description**: Logs in a user and returns an access token.

---

### 3. **Add Investment**
- **Endpoint**: /portfolio/invest/
- **Method**: POST
- **Description**: Adds a new investment to the user's portfolio.

---

### 4. **Fetch Portfolio**
- **Endpoint**: /portfolio/fetch
- **Method**: GET
- **Description**: Fetches the user's investment portfolio details.

---

### 5. **Fetch Funds by Fund Family**
- **Endpoint**: /funds/
- **Method**: GET
- **Description**: Fetches mutual fund details by providing a fund family name as a query parameter.

![](https://i.imgur.com/waxVImv.png)

## Usage
After deploying the container, interact with the api by sending HTTP requests to the exposed endpoints. Refer to the API [documentation](https://mutual-funds-api.apidog.io/) for detailed information on available endpoints and request formats.
