# Pet Adoption Agency Application

## Overview
This Pet Adoption Agency application is a web-based platform designed to manage pet adoptions. It allows users to view available pets, add new pets, edit pet details, and delete pets.
Fun fact: Dalle was used to generate the profile header image


https://github.com/jiahaoli0465/adopt/assets/144624616/87e80b73-db0e-4194-a014-49ec9266e068


## Key Features
- **View Pets**: Browse through a list of available pets.
- **Pet Profile**: Great profile design.
- **Add New Pets**: Easily add new pets to the system.
- **Edit Pet Details**: Update information of existing pets.
- **Delete Pets**: Remove pets from the system.

## Technologies Used

### Flask
A lightweight WSGI web application framework in Python, used for handling requests, rendering templates, and managing backend logic.

### SQLAlchemy
An ORM library for Python, allowing for efficient interaction with the database through Python objects.

### WTForms
A flexible forms validation and rendering library for Python web development, used for:
- **Form Handling**: Simplifying the creation and management of web forms.
- **Validation**: Providing built-in validators to ensure data integrity.
- **Extensibility**: Adaptable to various field types and custom validations.

### HTML and CSS
- **HTML Templates**: For rendering the front-end interface.
- **CSS**: Custom styling for a visually appealing and responsive design.

### JavaScript (Axios)
Used for making asynchronous HTTP requests, allowing for dynamic operations like deleting pet records without page reloads.

## Design Elements
The application incorporates several design elements for an engaging user experience:
- **Responsive Layout**: Ensures a seamless experience across various devices and screen sizes.
- **Intuitive Navigation**: Easy-to-use interface with clear navigation options.
- **Visual Appeal**: Custom CSS styles and static assets like images provide a visually attractive layout.


## Installation and Setup

### Prerequisites

- Python (Version 3.6 or later)
- pip (Python package manager)
- PostgreSQL

### Installation Guide

1. **Clone the Repository**


2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - Initialize a PostgreSQL database named `adopt`.
   - Ensure the database URI in `app.py` matches your database configuration.

5. **Optional - set up using random seed data**
   ```bash
   python seed.py
   ```

## Usage

To run the application:

```bash
flask run
```

Then, navigate to the adress given from your terminal in your browser to use Flask Blogly.



## License

Adopt is released under the MIT License. See the [LICENSE](LICENSE.md) file for more details.

## Contact

For questions or feedback regarding Adopt, please contact me at:

- **Email**: [jiahaoli0465@gmail.com](mailto:jiahaoli0465@gmail.com)
- **GitHub Profile**: [jiahaoli0465](https://github.com/jiahaoli0465)
