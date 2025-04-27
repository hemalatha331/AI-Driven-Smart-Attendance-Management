# AI Driven Smart Attendance Management

## Project Overview

AI Driven Smart Attendance Management is a web-based application designed to automate attendance tracking using face recognition. The system registers and extracts facial features, saves them into a CSV file, detects faces in real-time, and logs attendance. The application also sends SMS notifications using the Twilio API. The entire process is accessible through a web dashboard.

## Features

- **Face Registration**: Capture and register facial data for users.
- **Feature Extraction**: Extract facial features using dlib's ResNet50 model.
- **Attendance Logging**: Log attendance based on face detection.
- **SMS Notification**: Notify users about their attendance using Twilio API.
- **Web Dashboard**: An intuitive web interface built with Flask to manage and monitor the attendance system.

## Technologies Used

- **dlib ResNet50 Model**: For face recognition and feature extraction.
- **OpenCV**: For face detection and image processing.
- **Flask**: For creating the web dashboard and handling the backend logic.
- **Twilio API**: For sending SMS notifications to users.
- **SQLite**: For managing the attendance data.
- **Python**: The core programming language used for implementation.

## Project Images

Here are some screenshots from the project:


### Face Registration Page

![faceregister.png](https://github.com/hemalatha331/AI-Driven-Smart-Attendance-Management/blob/main/Project%20images/faceregister.png)

### User Registration Details

![registerdetails.png](https://github.com/hemalatha331/AI-Driven-Smart-Attendance-Management/blob/main/Project%20images/registerdetails.png)


### Face Detection Sample

![facedetect.png](https://github.com/hemalatha331/AI-Driven-Smart-Attendance-Management/blob/main/Project%20images/facedetect.png)

### Web Dashboard

![attendace trach web.png](https://github.com/hemalatha331/AI-Driven-Smart-Attendance-Management/blob/main/Project%20images/attendace%20trach%20web.png)

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
- dlib
- OpenCV
- Twilio
- SQLite (or any relational database)
  
### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hemalatha331/AI-Driven-Smart-Attendance-Management.git
