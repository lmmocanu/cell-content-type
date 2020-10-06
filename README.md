# API for determining a cell content type

This is a simple API written in Flask that can return the content type of an input cell data.

The endpoint `/api/v1/get-type.json` can be called with the get method and a "content" input parameter to get a type output.

Example request to the deployed Azure app: [https://cell-content-type.azurewebsites.net/api/content_type.json?content=1000](https://cell-content-type.azurewebsites.net/api/content_type.json?content=1000)

`app.py` contains the Flask API.

`parse_table.py` is a script that reads a `csv` file and produces an output `.xlsx` file where each cell contains the data type of the input cell. 

`query.py` is a simple script that contains a function to query the deployed API on Azure. Usage: `query(content)`.
