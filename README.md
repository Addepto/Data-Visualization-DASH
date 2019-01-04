Visualize your data with Dash
==================================

In this repository we show you an example of simple Dashboard for fast visualization of data, which will be handy for any Data Scientist during process of Data Exploration.

Dash can be installed with: 
```
pip install dash
```

To run dashboard type:
```
python app.py
```

![Dashboard](https://github.com/Addepto/DASH_DataVizualization/blob/master/images/dashboard.png)

- Our short code generated fully interactive dashboard. We use AdventureWorksDW2017 SQL Server database (vTargetMail view) to create a sample dataset.

- As default dashboard will be available on the http://127.0.0.1:8050/. Dataset data.csv should be adjacent to app.py. Any dataset in csv format where variables are numerical or strings can be visualized. Only datetime variables should be transformed to be understandable by pandas (for example to_datetime function) or cast to numerical value. 

- You can deploy your dashboard in several ways to be available for a broad public. You can use Dash servers for enterprises or use platforms like Digital Ocean or Heroku. You may also run the app on your own server.
