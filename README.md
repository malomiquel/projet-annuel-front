
# Project Documentation: Front-end for Patient Prediction Model

## Overview

This project is a front-end application built using Pynecone, a Python framework for creating web applications. The application serves as an interface for a patient prediction model, allowing users to input patient data and receive predictions.

## Project Structure

The project consists of the following files:

1. `.gitignore`: Specifies files and directories to be ignored by Git.
2. `README.md`: A placeholder for project documentation.
3. `pcconfig.py`: Configuration file for the Pynecone application.
4. `front_end/__init__.py`: An empty file, likely used to mark the directory as a Python package.
5. `front_end/front_end.py`: The main application file containing the front-end logic and UI components.

## Main Application (`front_end/front_end.py`)

### Functionality

The main application file defines the following key components:

1. **State Management**: A `State` class that handles form data, health check status, and prediction results.

2. **Health Check**: A function to verify the connection to the backend server.

3. **Prediction**: A function that sends form data to the backend server and receives predictions.

4. **User Interface**: 
   - A form for inputting patient data
   - A submit button to trigger predictions
   - A display area for showing prediction results
   - A health check button and status indicator

### Inputs

The application accepts the following patient data inputs:

- PRG
- PL
- PR
- SK
- TS
- M11
- BD2
- Age
- Insurance

### Outputs

The application provides the following outputs:

1. Health Check Status: Indicates whether the connection to the backend server is successful.
2. Prediction Result: Displays the prediction received from the backend server based on the input data.

## Configuration (`pcconfig.py`)

This file sets up the Pynecone application configuration, including:

- Application name: "front_end"
- Database URL: "sqlite:///pynecone.db"
- Environment: Development

## Usage

To use this application:

1. Ensure all dependencies are installed (Pynecone, requests).
2. Run the Pynecone application (typically using a command like `pc run`).
3. Access the web interface in a browser.
4. Use the "Vérifier la connexion" (Check connection) button to ensure connectivity with the backend.
5. Fill in the patient data form.
6. Click "Prédire" (Predict) to submit the data and receive a prediction.

## Notes

- The backend server is expected to be running at `http://ec2-35-180-228-111.eu-west-3.compute.amazonaws.com:5000`.
- The application supports dark/light mode toggling.
- Error handling is implemented for failed predictions or connections.
