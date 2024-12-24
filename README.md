
# Edge-to-Cloud Data Pipeline with Azure  

### Description  
This project, developed as part of my studies at Nackademin, demonstrates a real-time data pipeline from edge devices to the cloud using Microsoft Azure. It simulates the full lifecycle of sensor data—from generation to ingestion, processing, storage, and visualization—offering a scalable and automated solution for real-time monitoring and analytics.  

### Key Features  

#### 1. **Edge Simulation and Data Ingestion**  
- Python scripts simulate synthetic sensor data (e.g., temperature and humidity).  
- Data is streamed to **Azure Queue Storage** for reliable and asynchronous message handling.  

#### 2. **Data Storage and Automation**  
- Structured data is stored in a serverless **Azure SQL Database**.  
- **Azure Logic Apps** automate data movement from the queue to the database for seamless processing.  

#### 3. **Data Consumers and Visualization**  
- Integrated **Grafana** for real-time monitoring and visualization of trends.  
- Created a Python-based consumer to query and display data efficiently.  
- Built a web application using **Flask** and **Chart.js** for interactive sensor data visualization.  

#### 4. **Cost Optimization Analysis**  
- Compared Azure SQL Database (Serverless) with Azure VM hosting PostgreSQL for cost-effectiveness and scalability.  

### Architecture Diagram  
*(Include a diagram or image showing the pipeline's architecture to help others understand the flow.)*  

### Technologies Used  
- **Microsoft Azure**: Azure SQL, Queue Storage, Logic Apps  
- **Python**: Data simulation and custom data consumer  
- **Grafana**: Real-time monitoring and trend visualization  
- **Flask & Chart.js**: Web-based interactive visualization  
- **SQL**: Structured data storage and querying  
- **JavaScript**: Frontend for the visualization app  

### Installation and Usage  

#### Prerequisites  
1. Microsoft Azure account.  
2. Python installed locally.  
3. Grafana setup for real-time monitoring.  

#### Steps  
1. Clone this repository:  
   ```bash
   git clone https://github.com/Misbah-Bin-Hossain/Edge-to-Cloud-Data-Pipeline-with-Azure.git
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Configure Azure services:  
   - Set up Azure Queue Storage and Logic Apps.  
   - Create an Azure SQL Database and update the connection string in the Python scripts.  

4. Run the data simulator:  
   ```bash
   python simulate_sensor_data.py
   ```  

5. Launch the Flask web application for visualization:  
   ```bash
   flask run
   ```  

### Results  
This pipeline successfully demonstrates the ingestion, processing, storage, and visualization of real-time data, with the following benefits:  
- **Automation**: Azure Logic Apps streamline data workflows.  
- **Scalability**: Serverless SQL database adapts to varying data loads.  
- **Cost Efficiency**: Optimized hosting strategies for database management.  
- **Real-time Insights**: Integrated tools for monitoring and visualization.  

### Skills Demonstrated  
- **Cloud Computing**: Virtual Machines, Azure SQL, Logic Apps  
- **Data Engineering**: ETL pipelines, event-driven architecture  
- **Visualization**: Grafana, Power BI, Chart.js  
- **Operational Analysis**: Cost-benefit evaluations for cloud services  

### License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  
