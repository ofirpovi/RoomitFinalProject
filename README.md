# ROOMIT

## Description

ROOMIT is the final project of our software engineering degree at Ben Gurion University. The goal of ROOMIT is to create a roommate matching platform that simplifies the process of finding compatible roommates. The platform caters to two types of users: roommates who already have a living arrangement and roommates who are looking for both a roommate and a place to live.

For roommates with an existing living arrangement, they provide their personal information, housing details, and roommate preferences. On the other hand, roommates who are searching for a roommate and a place to live fill in their personal information, roommate requirements, and property preferences. The system then calculates a matching score between the different roommates, displaying the most relevant roommate candidates for each user. The matches are sorted in descending order of the matching score, ensuring higher compatibility.

## Features

The ROOMIT project includes the following features:

1. User Profiles: Each user has a profile that includes personal information and, for roommates with a property, property details.

2. Home Page: The home page displays relevant roommate candidates for each user, along with their matching scores. It includes user photos and property information (if applicable). Each post serves as a link to the relevant user's profile.

3. Like System: Users can like other users from the home page. They can also view who has liked them and whom they have liked.

4. Filtering: Users can filter the posts on the home page based on various criteria, such as roommate requirements or property preferences.

5. Recommendation System: The system incorporates a recommendation feature that suggests potential roommates based on the preferences of similar users.

**Additional Planned Features**:

- Chat feature: Implement a chat system to facilitate communication between potential roommates.
- Map API: Integrate a map API to display the location of properties and enhance the user experience.
- More to come...
## Installation

To set up the ROOMIT project, follow these steps:

1. Clone the repository to your local machine.

```bash
git clone https://github.com/ofirpovi/RoomitFinalProject.git
```

2. Navigate to the project directory.

```bash
cd RoomitFinalProject
```

3. (Optional) Set up a virtual environment for the project.

```bash
python -m venv env
```

4. (Optional) Activate the virtual environment.

```bash
source env/bin/activate
```

5. Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```
OR

Alternatively, you can use the provided install_packages.bat file to automatically install the required packages.

- Double-click the install_packages.bat file and it will download and install all the necessary packages for the ROOMIT project.

## Usage

To run the ROOMIT project, follow these steps:

1. Navigate to the project directory.

```bash
cd RoomitFinalProject
```

2. (Optional) Activate the virtual environment (if you set one up).

```bash
source env/bin/activate
```

3. Start the Django development server.

```bash
python manage.py runserver
```

4. Open a web browser and visit `http://localhost:8000` to access the ROOMIT website.

**API Usage**: The project utilizes Django REST Framework, which provides an API for accessing and manipulating data. You can interact with the API using HTTP methods (GET, POST, PUT, DELETE) to perform various operations on resources.
