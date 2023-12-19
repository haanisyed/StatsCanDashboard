import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load your dataset
df = pd.read_excel(r"C:\Users\haani\Downloads\14100287.xlsx")

# Define unique sex values for dropdown options
sex_options = df['Sex'].unique()

# Define custom colors for each sex
sex_colors = {'Both sexes': 'blue', 'Males': 'orange', 'Females': 'pink'}

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        "Age Group Distribution by Sex - Statistics Canada",
        style={'background-color': 'navy', 'color': 'white', 'padding': '10px'}
    ),

    # Dropdowns for selecting an age group
    dcc.Dropdown(
        id='age-group-dropdown',
        options=[
            {'label': age_group, 'value': age_group} for age_group in df['Age group'].unique()
        ],
        value=df['Age group'].unique()[0],  # Default selection
        style={'width': '50%'}
    ),

    # Bar chart to display counts by age group and sex
    dcc.Graph(id='bar-chart'),
])

# Define callback to update the bar chart based on the selected age group
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('age-group-dropdown', 'value')]
)
def update_bar_chart(selected_age_group):
    # Filter data based on the selected age group
    filtered_data = df[df['Age group'] == selected_age_group]

    # Create a grouped bar chart using Plotly Express with custom colors
    fig = px.bar(
        filtered_data,
        x='Sex',
        y='VALUE',  # Assuming 'VALUE' is the column containing counts
        color='Sex',
        color_discrete_map=sex_colors,  # Use the specified colors
        title=f'Distribution of Age Group ({selected_age_group}) by Sex',
        labels={'VALUE': 'Count'}
    )

    # Set background color to white
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)



