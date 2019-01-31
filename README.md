Visualize your data with Dash
==================================
At last in 2015 appeared Dash as an Open Source library for creating Web-based dashboards and other visual applications. Dash is based on Plotly - very powerful plot drawing library but is not limited to it, your Python code can do anything you want. Dash is built with React and Flask, which empowers it with modern UI elements like dropdowns and sliders.

In this repository we show you an example of simple Dashboard for fast visualization of data, which will be handy for any Data Scientist during process of Data Exploration.

Dash can be installed with (also pandas is required for loading dataset): 
```
pip install dash
```


To run dashboard type:
```
python app.py
```

- Our short code generated fully interactive dashboard. We use AdventureWorksDW2017 SQL Server database (vTargetMail view) to create a sample dataset.

![Dashboard](https://github.com/Addepto/DASH_DataVizualization/blob/master/images/dashboard.png)


- As default dashboard will be available on the http://127.0.0.1:8050/. Dataset data.csv should be adjacent to app.py. Any dataset in csv format where variables are numerical or strings can be visualized. Only datetime variables should be transformed to be understandable by pandas (for example to_datetime function) or cast to numerical value. 

- You can deploy your dashboard in several ways to be available for a broad public. You can use Dash servers for enterprises or use platforms like Digital Ocean or Heroku. You may also run the app on your own server.
