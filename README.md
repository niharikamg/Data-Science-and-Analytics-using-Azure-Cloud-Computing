 Data Science and Analytics Using Azure Cloud

## Overview
This project focuses on analyzing retail data using **Azure Cloud Technologies**. The goal is to build an **end-to-end data pipeline**, apply **machine learning models**, and create an **interactive dashboard** to derive insights on customer engagement and spending behaviors.

## Technologies Used
- **Azure App Services** (Hosting the web application)
- **Azure SQL Database** (Storing transactions, households, and products data)
- **Flask (Python Web Framework)** (Interactive web application)
- **Scikit-learn** (Machine Learning for Basket Analysis and Churn Prediction)
- **Plotly/Dash** (Data visualization and interactive dashboards)

---

## Setup Instructions
### 1. Set Up Azure Resources
1. **Create an Azure SQL Database**
   - Configure a database for transactions, households, and products.
   - Run the SQL script `database_setup.sql` to create tables.
   
2. **Deploy the Web Application to Azure App Services**
   - Upload the Flask application (`flask_app.py`).
   - Configure `DATABASE_URL` in the app to connect to Azure SQL.
   - Deploy using **Azure CLI**:
   ```sh
   az webapp up --name retail-analytics --resource-group AzureProjectGroup --runtime "PYTHON:3.9"
   ```

### 2. Run the Web Application
1. **Launch the web interface**
   - Visit your deployed app: `https://retail-analytics.azurewebsites.net`
2. **Upload Transactions File**
   - Use `login.html` to enter credentials and upload transaction data.

### 3. Run Machine Learning Model
1. **Train the Basket Analysis Model**
   ```sh
   python ml_model.py
   ```
2. **Churn Prediction (Optional)**
   ```python
   from sklearn.linear_model import LogisticRegression
   model = LogisticRegression().fit(X_train, y_train)
   ```

### 4. Interactive Dashboard
- **Visualize insights** such as spending patterns and loyalty program impact.
- Use **Plotly/Dash** for an interactive analytics dashboard.

Example Visualization:
```python
import plotly.express as px
fig = px.bar(df, x='Date', y='Spend', color='Department')
fig.show()
```

---

## Submission
Submit the following:
1. **Azure Web App URL**
2. **Screenshots of working application and database setup**
3. **Final Code Repository**

---

## Conclusion
By following this guide, you will successfully **deploy a scalable data analytics application on Azure**, leveraging **machine learning, SQL, and cloud computing**.

🚀 Happy Building!

