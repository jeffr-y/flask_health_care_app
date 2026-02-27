# **Flask  Health Web Application**



A full-stack analytics project that collects user financial data through a Flask web application, stores it securely in MongoDB Atlas, and processes it through a structured analytics pipeline using Python, Pandas, and Jupyter notebooks. The project concludes with visualizations exported for client-facing presentations.



## **Project Overview**



This project demonstrated an end-to-end data workflow that integrates web development, cloud-based storage, object-oriented programming, data engineering, and exploratory data analysis. The system was designed to meet academic requirements while reflecting production-grade engineering practices such as modular structure, environment isolation, and cloud development

The workflow is intentionally separated into three layers to support clarity, reproducibility, and reviewer- friendly validations:

•	Data Collection Layer – A Flask web app developed on Render collects user financial information.

•	Data Storage Layer – All submissions are stored in MongoDB Atlas, ensuring secure, scalable, cloud-based persistence,

•	Analytics \& Visualization Layer – Jupyter notebooks load the stored data, convert it into structured objects, export CSV files, and generate visualizations for reporting



### **Folder Structure**



The project follows a modular layout to support clean separation of concerns, ease of review, and cloud deployment.



flask\_health\_care\_app/

|

|\_\_app.py

|\_\_requirements.txt

|\_\_.env   # Local not committed to git

|\_\_ models/

|    |\_ \_\_init\_\_.py

|    |\_ user\_class.py

|

|\_\_ wsgi.py

|

|\_\_ data/

|    |\_\_user\_data.csv

|

|\_\_ templates/

|     |\_form.html

|     |\_success.html

|

|\_\_ static/

|       |\_\_style

|

|\_\_ Visualizations/

|        |\_\_combined\_finance\_dashboard.png

|

|\_\_ data\_analysis.ipynb

|\_\_ analysis\_visualization.ipynb

|

|\_\_ README.md



### **Technologies Used**



•	Flask – web application framework

•	Render – Cloud hosting for the Flask app

•	MongoDB Atlas – Cloud database for persistent storage

•	Python (Pandas, Seaborn, Matplotlib) – Data processing and visualization

•	Jupyter Notebook – Analysis and reporting environment

•	Git $ GitHub – Version control and project management



#### **Application Workflow**



##### **Data Collection (Flask on Render)**

Users submit financial information through a web form. The backend validates input, converts the submission into a User class instance, and stores the data as a dictionary in MongoDB Atlas. Render handles hosting, environment variables, and automatic deployments and redeployments.



##### **Data Processing (Jupyter Notebook)**



The data\_analysis.ipynb notebook connects to MongoDB Atlas, retrieves all stored documents, and converts each record into a User object. The notebook then converts the objects into dictionaries, exports the dataset into data/user\_data.csv, and validates the structures for downstream analysis. This step satisfies the requirements to use a  User class. Loop through the collected data, and stores in a CSV file.

##### 

##### **Data Visualization**



&nbsp;The analysis\_ visualization .ipynb notebook loads the CSV and produces two required visualizations



•	Top 10 ages by average income

•	Gender distribution across spending categories

The final dashboard is exported to:

Visualizations/combined\_finance\_dashboard.png



###### This file is optimized for inclusion in a PowerPoint presentation for client reporting.



##### **Deployment on Render.**



The application is deployed using:

•	A requirements.txt file for dependency installation

•	A Render web service configured with

Start command: gunicorn app:app

Environment variable: MONGO\_URI stored securely in Render

Build environment: Python 3.x

Render automatically builds and services the Flask application, making it accessible via public URL: https://flask-health-care-app.onrender.com



##### **Running the project locally**



The project can be executed locally to support development, debugging, and validation of the analytics pipeline. The workflow mirrors the deployed environment. The data\_analysis.ipynb and the analysis\_visualization.ipynb are also run locally.



###### **Prerequisites**

•	Python 3.x

•	A virtual environment

•	MongoDB Atlas connection string in a .env file

•	All dependencies installed from requirements.txt



###### &nbsp;**Steps**

1\.	Clone the repository:

2\.	git clone <your-repo-url>

3\.	cd flask\_health\_care\_app

4\.	Create and activate a virtual environment

5\.	python -m venv venv

6\.	venv\\Scripts\\activate # windows

7\.	Install dependencies:

8\.	Pip install -r requirements.txt

9\.	Configure the environment variable by creating a.env file

10\.	 MONGO\_TRI = mongdb\_atlas\_connection\_string

11\.	Run the Flask application:

o	Python app.py



The application becomes available at http: 127.0.0.1:5000/.



12	Run the analytics notebooks by opening

o	aata\_analysis.ipynb to regenerate the CSV

o	analysis\_visualization\_ioynb to produce the dashboard



##### **Future Improvements**



Several enhancements could strengthen scalability, analytical depth, and user experience:

•	Automated ETL Scheduling – introduce a scheduled job (Render Cron or GitHub action) to regenerate the CSV and visualization automatically.



•	Enhance Data validation – Expand the User class to include stricter validation rules and type enforcement.



•	Interactive Dashboards: Replace static PNG export with interactive dashboards using Plotty Dash or Streamlit. 

•	Role-Based Access Control – Add authentication to the Flask app for secure data review and controlled submissions.

•	API Layer- Expose a Rest API for retrieving aggregated financial insights directly from the analytics pipeline.

•	Containerization – Package the application using Docker to ensure consistent deployment across environments

•	Expend Financial Metrics -incorporate additional indicators such as savings rate, debt-to-income-ratio, or spending efficiency.

•	These improvements would evolve the project from an academic demonstration into a more robust, production-ready financial analytics platform











