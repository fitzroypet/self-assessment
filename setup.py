from setuptools import setup, find_packages

setup(
    name="analytics-maturity-assessment",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask==2.3.3",
        "flask-cors==4.0.0",
        "gspread==5.12.0",
        "oauth2client==4.1.3",
        "python-dotenv==1.0.0",
        "reportlab==4.0.4",
        "openai==1.3.0",
        "gunicorn==21.2.0"
    ],
) 