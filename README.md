# API Setup and Installation Guide

## Prerequisites
- Python 3.9+
- git

## Environment Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/.git
   cd yourproject


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
- **id** (INT, primary key): Unique identifier for the user.
- **username** (VARCHAR): Username of the user.

## Conversations Table
- **id** (INT, primary key): Unique identifier for the conversation entry.
- **user_id** (INT, foreign key): References `id` in the Users table.
- **question** (TEXT): The question asked by the user.
- **answer** (TEXT): The response provided by the system.
- **created_at** (TIMESTAMP): The timestamp when the conversation was created.

