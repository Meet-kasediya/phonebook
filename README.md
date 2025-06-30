![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
---

# Contact Management System

Flask-based web application that allows users to manage contacts and categorize them. Users can create, update, search, and delete contacts, as well as manage categories to which contacts can be assigned. The project uses SQLite as the database backend.

## Features

- **Create Contact**: Add new contacts with details such as name, email, phone number, address, and organization.
- **Search Contact**: Search for contacts by name, email, phone number, or other details.
- **Update Contact**: Modify contact details.
- **Delete Contact**: Remove contacts from the database.
- **Category Management**: Add, update, and delete categories, then assign contacts to specific categories.
- **View Contacts by Category**: View contacts organized by their categories.

## Technologies

- **Backend**: Flask
- **Database**: SQLite
- **Frontend**: HTML templates (Flask `render_template`)

## Setup and Installation

### Prerequisites

- **Python** (v3.6+)
- **SQLite** (this project uses SQLite as the database, which comes pre-installed with Python)
- **pip** (Python package manager)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com//Meet-kasediya/phonebook.git
   cd phonebook
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   - Open your browser and navigate to `http://127.0.0.1:5000`

## Application Routes

| Route               | Method(s) | Description                                     |
|---------------------|-----------|-------------------------------------------------|
| `/`                 | `GET`     | Home page                                       |
| `/CreateContact`    | `GET/POST`| Create a new contact                            |
| `/SearchContact`    | `GET`     | Search for contacts                             |
| `/results`          | `POST`    | Display search results                          |
| `/UpdateContact`    | `GET/POST`| Update an existing contact                      |
| `/gatherID`         | `POST`    | Gather contact ID for updating                  |
| `/deleteID`         | `POST`    | Delete a contact                                |
| `/contactcategory`  | `GET`     | View contacts grouped by categories             |
| `/addcategory`      | `GET/POST`| Add a new category                              |
| `/gathercategory`   | `POST`    | Gather category information for updating        |
| `/updatecategory`   | `GET/POST`| Update an existing category                     |
| `/deletecategory`   | `POST`    | Delete a category                               |
| `/gatheridforcategory` | `POST` | Gather contact ID to assign to a category       |
| `/addtocategory`    | `POST`    | Link a contact to a category                    |

## Usage

1. **Creating Contacts**: Go to `/CreateContact` to add a new contact with required fields.
2. **Searching Contacts**: Use `/SearchContact` to search contacts by various criteria.
3. **Updating and Deleting Contacts**: Modify or remove contacts via `/UpdateContact` and `/deleteID`.
4. **Managing Categories**: Add, update, or delete categories via `/addcategory`, `/updatecategory`, and `/deletecategory`.
5. **Assigning Categories**: Go to `/gatheridforcategory` to assign contacts to categories.

Pull requests are welcome. For major changes, please open an issue first to discuss the proposed changes.

## Live at
https://contact-management.up.railway.app
---
