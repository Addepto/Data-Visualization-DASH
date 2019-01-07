#Import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
from dash.dependencies import Input, Output

#Read dataset
df = pd.read_csv("data.csv")
#List of dataset columns
available_indicators = list(df)

#Initialize Dash
app = dash.Dash()

#Create layout
app.layout = html.Div(children=[

	#Left column
    html.Div([
		#Scatter Plot
        html.H1(children='Scatter Plot'),
        
        html.Div([
            html.Div([
				#X axis data selection
                dcc.Dropdown(
                    id='xaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value=available_indicators[0]
                ),
				#Choice between linear or log axis
                dcc.RadioItems(
                    id='xaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ],
            style={'width': '31%', 'display': 'inline-block'}),

            html.Div([
				#Y axis data selection
                dcc.Dropdown(
                    id='yaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value=available_indicators[1]
                ),
				#Choice between linear or log axis
                dcc.RadioItems(
                    id='yaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'width': '31%', 'float': 'center', 'display': 'inline-block'}),
            
            html.Div([
				#Filter by column
                dcc.Dropdown(
                    id='zaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value=available_indicators[1]
                ),
				#Filter choice
                dcc.RadioItems(
                    id='zaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Filter', 'No Filter']],
                    value='No Filter',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'width': '31%', 'float': 'center', 'display': 'inline-block'})
        ]), 
		#Plot graph
        dcc.Graph(id='graph'),
		
		#Bar chart
        html.H1(children='Bar chart'),
        
        html.Div([
            html.Div([
				#X axis data selection
                dcc.Dropdown(
                    id='bar_xaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value=available_indicators[0]
                ),
				#Choice between linear or log axis
                dcc.RadioItems(
                    id='bar_xaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ],
            style={'width': '31%', 'display': 'inline-block'}),

            html.Div([
				#Y axis data selection
                dcc.Dropdown(
                    id='bar_yaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value=available_indicators[1]
                ),
				#Choice between linear or log axis
                dcc.RadioItems(
                    id='bar_yaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'width': '31%', 'float': 'center', 'display': 'inline-block'}),
            
            html.Div([
				#Filter by column
                dcc.Dropdown(
                    id='bar_zaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value=available_indicators[1]
                ),
				#Filter choice
                dcc.RadioItems(
                    id='bar_zaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Filter', 'No Filter']],
                    value='No Filter',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'width': '31%', 'float': 'center', 'display': 'inline-block'})
        ]),
		#Plot graph        
        dcc.Graph(id='bar_chart'),
               
    ], style={'width': '48%', 'display': 'inline-block'}),
 
	#Right column
    html.Div([
		#Box Plot
        html.H1(children='Box Plot'),
        html.Div([
            html.Div([
				#X axis data selection
                dcc.Dropdown(
                    id='box_xaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value=available_indicators[0]
                ),
				#Choice between linear or log axis
                dcc.RadioItems(
                    id='box_xaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Filter', 'No Filter']],
                    value='No Filter',
                    labelStyle={'display': 'inline-block'}
                )
            ],
            style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
				#Y axis data selection
                dcc.Dropdown(
                    id='box_yaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value=available_indicators[1]
                ),
				#Choice between linear or log axis
                dcc.RadioItems(
                    id='box_yaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'width': '48%', 'float': 'center', 'vertical-align': 'top', 'display': 'inline-block'}),
            
        ]),  
		#Plot graph		
        dcc.Graph(id='box_graph'),
        
		#Histogram    
		html.H1(children='Histogram'),
			html.Div([
				html.Div([
					#Filter by column
					dcc.Dropdown(
						id='histogram_xaxis-column',
						options=[{'label': i, 'value': i} for i in available_indicators],
						value=available_indicators[0]
					),
					#Filter choice
					dcc.RadioItems(
						id='histogram_xaxis-type',
						options=[{'label': i, 'value': i} for i in ['Filter', 'No Filter']],
						value='No Filter',
						labelStyle={'display': 'inline-block'}
					)
				],
				style={'width': '48%', 'display': 'inline-block'}),

				html.Div([
					#Y axis data selection
					dcc.Dropdown(
						id='histogram_yaxis-column',
						options=[{'label': i, 'value': i} for i in available_indicators],
						value=available_indicators[1]
					)
				],style={'width': '48%', 'float': 'center', 'vertical-align': 'top', 'display': 'inline-block'}),
				
			]), 
			#Plot graph
			dcc.Graph(id='histogram_graph'),

        
    ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top'}),      
])



    
#Callback for Scatter Plot
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value'),
     dash.dependencies.Input('yaxis-column', 'value'),
     dash.dependencies.Input('zaxis-column', 'value'),
     dash.dependencies.Input('xaxis-type', 'value'),
     dash.dependencies.Input('yaxis-type', 'value'),
     dash.dependencies.Input('zaxis-type', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name, zaxis_column_name,
                 xaxis_type, yaxis_type, zaxis_type):

    if zaxis_type == 'Filter':
        data = []
        for value in df[zaxis_column_name].unique():
            data.append(go.Scattergl(
                x=df[df[zaxis_column_name] == value][xaxis_column_name],
                y=df[df[zaxis_column_name] == value][yaxis_column_name],
                name=str(value),
                text=df[df[zaxis_column_name] == value].index.values,
                mode='markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            ))
    else:
        data = [go.Scattergl(
            x=df[xaxis_column_name].values,
            y=df[yaxis_column_name].values,
            text=df.index.values,
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )]
    return {
        'data': data,
        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            hovermode='closest'
        )
    }
	
#Callback for Bar Chart	
@app.callback(
    dash.dependencies.Output('bar_chart', 'figure'),
    [dash.dependencies.Input('bar_xaxis-column', 'value'),
     dash.dependencies.Input('bar_yaxis-column', 'value'),
     dash.dependencies.Input('bar_zaxis-column', 'value'),
     dash.dependencies.Input('bar_xaxis-type', 'value'),
     dash.dependencies.Input('bar_yaxis-type', 'value'),
     dash.dependencies.Input('bar_zaxis-type', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name, zaxis_column_name,
                 xaxis_type, yaxis_type, zaxis_type):

    if zaxis_type == 'Filter':
        data = []
        for value in df[zaxis_column_name].unique():
            data.append(go.Bar(
                x=df[df[zaxis_column_name] == value][xaxis_column_name],
                y=df[df[zaxis_column_name] == value][yaxis_column_name],
                name=str(value),
                text=df[df[zaxis_column_name] == value].index.values
            ))
    else:
	
        data = [go.Bar(
            x=df[xaxis_column_name].values,
            y=df[yaxis_column_name].values,
			text=df.index.values,
        )]
    return {
        'data': data,
        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            hovermode='closest'
        )
    }

#Callback for Box Plot
@app.callback(
    dash.dependencies.Output('box_graph', 'figure'),
    [dash.dependencies.Input('box_xaxis-column', 'value'),
     dash.dependencies.Input('box_yaxis-column', 'value'),
     dash.dependencies.Input('box_xaxis-type', 'value'),
     dash.dependencies.Input('box_yaxis-type', 'value'),])
def update_graph(xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type):
    if xaxis_type == 'Filter':
        data = []
        for value in df[xaxis_column_name].unique():
            trace = {
                    "type": 'box',
                    "x": value,
                    "y": df[df[xaxis_column_name] == value][yaxis_column_name],
                    "name": str(value),
                    "box": {
                        "visible": True
                    },
                    "meanline": {
                        "visible": True
                    }
                }
            data.append(trace)
    else:
        trace = {
                    "type": 'box',
                    "x0": str(yaxis_column_name),
                    "y": df[yaxis_column_name].values,
                    "box": {
                        "visible": True
                    },
                    "meanline": {
                        "visible": True
                    }
                }
        data = [trace]
        
    x_title = xaxis_column_name
    if xaxis_type != 'Filter':
        x_title = ''
    
    return {
            "data": data,
            "layout" : {
                "title": "",
                "xaxis": {
                    'title': x_title,
                },
                "yaxis": {
                    'title': yaxis_column_name,
                    'type': 'linear' if yaxis_type == 'Linear' else 'log',
                }
            }
        }

#Callback for Histogram
@app.callback(
    dash.dependencies.Output('histogram_graph', 'figure'),
    [dash.dependencies.Input('histogram_xaxis-column', 'value'),
     dash.dependencies.Input('histogram_yaxis-column', 'value'),
     dash.dependencies.Input('histogram_xaxis-type', 'value')
    ])
def update_graph(xaxis_column_name, yaxis_column_name, xaxis_type):
    if xaxis_type == 'Filter':
        data = []
        for value in df[xaxis_column_name].unique():
            trace = go.Histogram(
                x=df[df[xaxis_column_name] == value][yaxis_column_name].values,
                name=str(value),
            )
            data.append(trace)
    else:
        trace = go.Histogram(
                x=df[yaxis_column_name].values,
            )
        data = [trace]
    
    return  {
                "data": data,
                "layout" : go.Layout(
                    barmode='stack',
                    xaxis=dict(
                        title=yaxis_column_name
                    ),
                    yaxis=dict(
                        title='count'
                    ),
               )
            }


if __name__ == '__main__':
    app.run_server(debug=True)