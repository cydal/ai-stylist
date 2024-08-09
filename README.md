
# AI Stylist Backend API

### Overview
The AI Stylist Backend API is an interface designed to enhance the fashion experience by providing personalized style recommendations. Built with FastAPI, this backend serves as the computational engine for a broader application that assists users in discovering and curating fashion choices based on their preferences and existing wardrobe.

### Features

**User Management**: Allows the registration and management of user profiles, enabling personalized interactions and style suggestions.
**Conversation Handling**: Facilitates real-time conversations with users, answering fashion-related queries and providing advice tailored to user preferences.
**Image Analysis**: Integrates advanced image recognition capabilities to analyze clothing items uploaded by users, extracting relevant tags like color, style, and type.
**Outfit Matching**: Leverages a combination of user data and sophisticated algorithms to propose outfit combinations that match user styles and preferences, making it easier for users to make fashion decisions.
**Scalable**: Deployed on Google Cloud, the API ensures robust performance, scalability, and security, handling user data and interactions with utmost confidentiality.


### Aim
This API aims to simplify the decision-making process in fashion by using artificial intelligence to provide contextually relevant and personalized style advice. It supports a seamless user experience, from querying fashion tips to uploading wardrobe items and receiving outfit recommendations.

### Getting Started
Refer to the detailed documentation included in this repository to set up the API locally or deploy it to a cloud environment. Quick start guides, usage examples, and configuration details are provided to help you integrate and utilize the API effectively in your projects or applications.


# API Setup and Installation Guide

## Prerequisites
- Python 3.9+
- git

## Environment Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/cydal/ai-stylist.git
   cd ai-stylist


## Install dependencies

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt



## Running the Application

```bash
uvicorn app.main:app --reload
```


## Testing
```bash
pytest
```


### API Overview


### 1. **Create User**
**Endpoint:** `/api/users/`
**Method:** POST
**Description:** Registers a new user in the system.
- **Request Body:** `UserCreate` schema
  - `username` (string, required): Username of the user.
  - `style_preferences` (string, optional): Style preferences of the user.
- **Responses:**
  - `200`: Successful creation of user. Returns `User` schema.
  - `422`: Validation error.


### 2. **Add Conversation**
**Endpoint:** `/api/conversations/`
**Method:** POST
**Description:** Adds a new conversation entry linked to a user.
- **Parameters:**
  - `user_id` (query, integer, required): The ID of the user.
  - `question` (query, string, required): The question posed by the user.
- **Responses:**
  - `200`: Successfully added conversation. Returns `Conversation` schema.
  - `422`: Validation error.



### 3. **Get Conversations**
**Endpoint:** `/api/conversations/{user_id}`
**Method:** GET
**Description:** Retrieves all conversations for a specific user.
- **Parameters:**
  - `user_id` (path, integer, required): The ID of the user.
- **Responses:**
  - `200`: Successfully retrieved conversations.
  - `422`: Validation error.




### 4. **Match Styles**
**Endpoint:** `/api/conversations/match-styles/`
**Method:** GET
**Description:** Generates outfit combinations based on uploaded images and their tags.
- **Parameters:**
  - `user_id` (query, integer, required): The ID of the user.
- **Responses:**
  - `200`: Successfully generated outfit suggestions.
  - `422`: Validation error.




### 5. **Upload Image**
**Endpoint:** `/api/images/upload`
**Method:** POST
**Description:** Uploads an image and stores it with associated tags.
- **Parameters:**
  - `user_id` (query, integer, required): The ID of the user.
- **Request Body:** `multipart/form-data`
  - `file` (binary, required): The image file to upload.
- **Responses:**
  - `200`: Successfully uploaded image.
  - `422`: Validation error.



### 6. **Get Images**
**Endpoint:** `/api/images/{user_id}`
**Method:** GET
**Description:** Retrieves all images uploaded by a specific user.
- **Parameters:**
  - `user_id` (path, integer, required): The ID of the user.
- **Responses:**
  - `200`: Successfully retrieved images.
  - `422`: Validation error.


### 7. **Read Root**
**Endpoint:** `/`
**Method:** GET
**Description:** A simple root endpoint to check API status.
- **Responses:**
  - `200`: API is up and running.


### Schemas
- **User**: Represents a user with `id`, `username`, and optional `style_preferences`.
- **Conversation**: Represents a conversation with `id`, `user_id`, `question`, and `answer`.
- **ValidationError**: Details validation errors.



### Database Schema

```markdown
# Database Schema Overview

## Users Table
- id (INT, primary key): Unique identifier for the user.
- username (VARCHAR): Username of the user.

## Conversations Table
- id (INT, primary key): Unique identifier for the conversation entry.
- user_id (INT, foreign key): References `id` in the Users table.
- question (TEXT): The question asked by the user.
- answer (TEXT): The response provided by the system.
- created_at (TIMESTAMP): The timestamp when the conversation was created.