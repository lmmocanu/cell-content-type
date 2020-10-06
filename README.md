# API for determining a cell content type

This is a simple API written in Flask that can return the content type of an input cell data.

The endpoint `/api/v1/get-type.json` can be called with the get method and a "content" input parameter to get a type output.

Example request from the deployed Azure app: [https://cell-content-type.azurewebsites.net/api/content_type.json?content=1000](https://cell-content-type.azurewebsites.net/api/content_type.json?content=1000)
