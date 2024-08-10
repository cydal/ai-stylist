
# AI Stylist Backend API

### Overview
The AI Stylist Backend API is an interface designed to enhance the fashion experience by providing personalized style recommendations. Built with FastAPI, this backend serves as the computational engine for a broader application that assists users in discovering and curating fashion choices based on their preferences and existing wardrobe.

### Features

**User Management**: Allows the registration and management of user profiles.
**Conversation Handling**: Facilitates real-time conversations with users, answering fashion-related queries.
**Image Analysis**: Integrates advanced image recognition capabilities to analyze clothing items uploaded by users, extracting relevant tags like color, style, and type.
**Outfit Matching**: Leverages a combination of user data and sophisticated algorithms to propose outfit combinations that match user styles and preferences, making it easier for users to make fashion decisions.
**Scalable**: Deployed on AWS ECS with Fargate.


### Aim
This API aims to simplify the decision-making process in fashion by using artificial intelligence to provide contextually relevant style advice. It supports a seamless user experience, from querying fashion tips to uploading wardrobe items and receiving outfit recommendations.

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


# Deploying FastAPI Application to AWS ECS with Fargate

## Overview

This guide outlines the steps to deploy a FastAPI application containerized with Docker to AWS using Amazon Elastic Container Service (ECS) with the Fargate launch type. Fargate allows you to run containers without managing servers or clusters.

## Prerequisites

- AWS account
- AWS CLI installed and configured
- Docker installed on your local machine
- FastAPI application Dockerized

## Steps

### Step 1: Prepare Your Docker Image

1. **Build your Docker image locally:**
```bash
docker build -t aifashionstylist .
```

2. **Tag Docker image for Amazon ECR:**
```bash
docker tag aifashionstylist:latest
your-account-id.dkr.ecr.your-region.amazonaws.com/aifashionstylist
```

### Step 2: Push Image to Amazon ECR

1. **Create an ECR Repository:**
- Navigate to the Amazon ECR console and create a new repository named `aifashionstylist`.
```bash
aws ecr create-repository \
    --repository-name aifashionstylist
```

2. **Authenticate Docker to ECR Repository:**
```bash
aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com
```

3. **Push image to ECR:**
```bash
docker push your-account-id.dkr.ecr.your-region.amazonaws.com/myfastapiapp
```

### Step 3: Set Up ECS with Fargate

1. **Create a Task Definition:**
- Go to the ECS console and create a new task definition.
- Select "Fargate" as the launch type.
- Define the task size (CPU and memory).
- Add a container definition with the image URL from ECR.
- Set the listening port to 80.

2. **Create a Cluster:**
- In the ECS console, create a new cluster using the "Networking only" template for Fargate.

3. **Create a Service:**
- Within the cluster, create a new service.
- Choose the task definition created earlier.
- Specify the desired number of tasks.
- Set up the network configuration:
  - Select the VPC and subnets.
  - Assign a security group that allows inbound traffic on port 80.
  - Enable "Auto-assign public IP" if your tasks need to be reachable from the internet.


## Accessing Your Application

After deployment, access your application via the public IP of the Fargate tasks.


## Additional Resources

- [Amazon ECS Documentation](https://docs.aws.amazon.com/ecs/index.html)
- [Amazon ECR Documentation](https://docs.aws.amazon.com/ecr/index.html)
- [AWS Fargate Documentation](https://docs.aws.amazon.com/fargate/index.html)