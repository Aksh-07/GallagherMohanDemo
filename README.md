# PDF Extractor - Django Application

## Overview
PDF Extractor is a Django-based web application that allows users to upload PDFs and extract relevant invoice data. The project includes user authentication (login/logout) and a simple UI for managing invoice data.

## Features
- User authentication (Login/Logout)
- Upload PDFs for processing
- Extract and display parsed invoice data
- Secure session handling with Django authentication

---
## How to Set Up Locally After Cloning

If someone clones the repository and needs to run it locally, follow these steps:
P.S. **setup ssh before cloning**

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd GallagherMohanDemo/backend/
   ```

2. **Set up a virtual environment and activate it**:
   ```bash
   python -m venv venv / or use / python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **setup env variable**:
   we need to set google gemini api key
   
   in ubuntu
   ```bash
   touch .env
   nano .env
   ```
   in windows create a file named .env and save the api key
   
   add your api key as :
   GEMINI_API_KEY=`YOUR_API_KEY`
   
   and save the file

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

7. **Visit the application**:
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Environment Variables (if any)
If your project requires environment variables, create a `.env` file and define them there. Example:
```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

Then, use `python-decouple` or `dotenv` to load them in `settings.py` or in required file.
In our case i am storing gemini API key in .env and calling it in `ml_models/extract_info`.

---

## ml_models
First pdf data is converted into appropriate text format using pdfplumber
Then i am using Google's generative ai api for calling gemini-2.0-flash for extracting useful information using prompt

---


## Database

we are using inbuilt sqlite3 for database and storing invoice number, invoice date, due date, amount, and pdf file location using django models
The pdf file is stored locally in  /backend/media/invoices

## Additional Notes
- If you face migration issues, try:
  ```bash
  python manage.py migrate --run-syncdb
  ```
- To install new dependencies, use:
  ```bash
  pip install <package_name>
  pip freeze > requirements.txt
  ```

---

## Contributing
Contributions are welcome! Feel free to fork this repo, create a feature branch, and submit a pull request.

---
