import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import math

from dash.dependencies import Input, Output

df_patient = pd.read_csv('coronavirusdataset/patient.csv')
df_patient['age'] = 2019 - df_patient['birth_year']

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Br(),html.Br(),html.Br(),
    html.H1(
        children='EDA of COVID-19 Data from South Korea',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='A visualisation of total suspects of COVID-19 based on age range or gender', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Br(),
    html.Div(
      className = 'container',
      children = [
        html.Label(children='Filter', style={
              'color': colors['text']
        }),
        dcc.Dropdown(
            id = 'dropdown',
            options=[
                {'label': 'Age', 'value': 'age_range'},
                {'label': 'Sex', 'value': 'sex'}
            ],
            value='age',
        )
      ]
    ),
    html.Br(),html.Br(),html.Br(),
    dcc.Graph(id='graph'),
    html.Br(),html.Br(),html.Br()
])

@app.callback(
  Output(component_id='graph', component_property='figure'),
  [Input(component_id='dropdown', component_property='value')]
)

def update_figure_graph(selected_var):
  df = df_patient[['id', 'age','sex']].dropna()
  df['age_range'] = df['age'].apply(group_age)

  df_fitur = pd.DataFrame({'count': df.groupby([selected_var]).size()}).reset_index()

  return {
    'data': [
        {'x': df_fitur[selected_var].tolist(), 'y': df_fitur['count'].tolist(), 'type': 'bar', 'name': selected_var}
    ],
    'layout': {
        'title': 'Total of COVID-19 suspects based on ' + selected_var,
        'plot_bgcolor': colors['background'],
        'paper_bgcolor': colors['background'],
        'font': {
          'color': colors['text']
        },
        'yaxis': {
          'title': 'Total suspects'
        },
        'xaxis': {
          'title': selected_var
        }
    }
  }

def group_age(age):
  if age % 10 != 0:
      lower = int(math.floor(age / 10.0)) * 10
      upper = int(math.ceil(age / 10.0)) * 10 - 1
      return f"{lower}-{upper}"
  else:
      lower = int(age)
      upper = int(age + 9) 
      return f"{lower}-{upper}"
    
if __name__ == '__main__':
    app.run_server(debug=True)
