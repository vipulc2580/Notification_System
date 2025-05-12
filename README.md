# Notification System

*An advanced notification system that sends email, SMS, and in-app notifications with retries, logging, and task management using Celery.*

<a href="https://drive.google.com/file/d/1twW7PbFtwc8umeb-q_ZkZIyiDp5-NHV2/view?usp=sharing">Demo Video Link</a>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

## Introduction

The Notification System is designed to send different types of notifications, such as emails, SMS, and in-app notifications via http api request. Built with Celery for task management and retries, Redis for caching and queueing, and Twilio for SMS, this system ensures reliable and timely notifications, even in case of failures. 

## Features

- **Email Notifications**  
  Sends personalized email notifications with HTML content using Django’s email system.

- **SMS Notifications**  
  Integrates with Twilio API to send SMS notifications to users, with retries in case of failure.

- **In-App Notifications**  
  Provides real-time notifications within the app, with status tracking for successful delivery.

- **Task Management with Celery**  
  Uses Celery to handle background tasks such as sending emails and SMS, with automatic retries and logging for failures.

- **Redis for Queueing**  
  Redis is used as a message broker to manage queues for Celery tasks, ensuring smooth task processing.

- **Logging**  
  Logs task execution, retries, and errors to provide insight into the notification process.

## Technologies Used

- **Backend:** Django, Celery, Redis  
- **SMS Service:** Twilio API  
- **Task Queue:** Celery with Redis  
- **Logging:** Python’s built-in logging module  
- **Database:** PostgreSQL (or other preferred DB for storing notifications)

## Installation & Setup

### 1. **Clone the Repository**
  ```bash
    git clone https://github.com/vipulc2580/Notification_System.git
    cd Notification_System
  ```

### 2. **Set Up the Virtual Environment**
  ```python
    python -m venv env
    # On Windows
    env\Scripts\activate
  ```
### 3. **Install Dependencies**
  ```python
    pip install -r requirements.txt
  ```

### 4. **Set Up Environment Variables**
  ```python
    redis=redis://127.0.0.1:6379
    email_host=your_host
    email_port=587
    email_user=your_email@gmail.com
    email_passkey=your_email_pass_key
    default_from_email=your_default_email_to_send_mails
    email_use_tls=True
    TWILIO_ACCOUNT_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_token
    TWILIO_PHONE_NUMBER=your_twilio_number
  ```

### 5. **Migrate the Database**
  ```python
    python manage.py migrate
  ```

### 6. **Start the Celery Worker**
  ```python
    celery -A notification_system worker --loglevel=info
  ```

### 7. **Start the Django Development Server**
  ```python
    python manage.py runserver
  ```

## Usage

  ### **Sending Email Notifications:**
  - The system sends HTML email notifications to users. You can configure email templates and triggers based on your business logic.
  - Uses Django’s built-in email backend for sending emails.
  
  ### **Sending SMS Notifications:**
  - The system uses Twilio API to send SMS notifications to users based on their phone number.
  - Retries are implemented in case of failure, and the status of the SMS is logged.
  
  ### **Handling Tasks with Celery:**
  - Celery tasks are used for background processing of emails, SMS, and in-app notifications.
  - Tasks are retried automatically with a specified delay if they fail.
  
  ### **In-App Notifications:**
  - In-app notifications are updated in real time when the notification status changes (sent, failed, etc.).


## Acknowledgements
Thanks to Twilio for SMS integration, Celery for task management, Redis for caching and queueing, and Django for building the backend. This system is built to ensure reliability and scalability in sending notifications.
