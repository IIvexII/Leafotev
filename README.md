# Leafotev 🍃

The leafotev project is an application built to help users identify plant diseases and pests. This project have two parts, the first part is the backend server that is built using FastAPI and the second part is the frontend that is built using Tkinter which is for the end user to interact with the application.

## Setup Backend Server 🚀(For Devs)

Backend server is where the machine learning model is hosted and where the frontend will send the images to be processed. This needs to be running for the frontend to work. 

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Backend

```bash
uvicorn --app-dir .\API\ main:app --reload
```

## Setup Frontend 🚀(For End-Users)

There is no need to install anything for the frontend, just run the `leafotev.exe` file and the application will start.

### Snapshots of User Application

<p float="middle">
  <img src="https://github.com/IIvexII/Leafotev/assets/41378765/29734eb0-2de7-41eb-b468-bf6740dec69a" width="500" />
  <img src="https://github.com/IIvexII/Leafotev/assets/41378765/3a64bdab-ab6d-4479-84e9-40d1a2098b62" width="500" /> 
</p>
