<Overview>
This project features a web application built using Dash to visualize the environmental impacts of smartphone production across different countries. The application uses data from a life cycle assessment (LCA) and provides insights into various environmental impact categories.

<Requirements>
To run the project, you need the following:
- Python 3.x
- Dash and its dependencies:
  - dash
  - dash-bootstrap-components
  - dash-core-components
  - dash-html-components
  - dash-table
- Plotly: For creating interactive plots
- Pandas: For data manipulation

<Data Preparation>
Ensure the data files cleaned_data.csv and country_table_data.csv are placed in the data/ directory.

<Running the Application>
To start the Dash application, run the following command: python main.py
The application will be accessible at http://127.0.0.1:8050/ in your web browser.

<Features>
- Dropdown Menu: Select different environmental impact categories to view specific data.
- Visualizations:
  - Bar Charts: Display scores for selected impact categories.
  - World Map: Visual representation of impact scores across different countries.
  - Data Table: Detailed data view for each selected impact category.
- Country Comparison: Compare the environmental impacts for different countries.

<Data Sources>
The data used in this dashboard is derived from the Ecoinvent 3.9.1 database and follows ISO 14040 and ISO 14044 standards for life cycle assessment.

<License and Acknowledgements>
This project utilizes data from the Ecoinvent 3.9.1 database and adheres to the relevant standards for environmental impact assessment.
All rights reserved: © 2024, Mingyu Song, Kaayin Kee.