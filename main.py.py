import dash
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html
from dash import dash_table

# dataframes
df = pd.read_csv('data/cleaned_data.csv')
gwp = df[df["Impact Category"] == 'climate change, global warming potential (GWP1000)']
tap = df[df["Impact Category"] == 'acidification: terrestrial, terrestrial acidification potential (TAP)']
eofp = df[df["Impact Category"] == 'photochemical oxidant formation: terrestrial ecosystems, photochemical oxidant formation potential: ecosystems (EOFP)']
hofp = df[df["Impact Category"] == 'photochemical oxidant formation: human health, photochemical oxidant formation potential: humans (HOFP)']
pmfp = df[df["Impact Category"] == 'particulate matter formation, particulate matter formation potential (PMFP)']
odpinfinite = df[df["Impact Category"] == 'ozone depletion, ozone depletion potential (ODPinfinite)']
sop = df[df["Impact Category"] == 'material resources: metals/minerals, surplus ore potential (SOP)']
lop = df[df["Impact Category"] == 'land use, agricultural land occupation (LOP)']
irp = df[df["Impact Category"] == 'ionising radiation, ionising radiation potential (IRP)']
htpnc = df[df["Impact Category"] == 'human toxicity: non-carcinogenic, human toxicity potential (HTPnc)']
htpc = df[df["Impact Category"] == 'human toxicity: carcinogenic, human toxicity potential (HTPc)']
mep = df[df["Impact Category"] == 'eutrophication: marine, marine eutrophication potential (MEP)']
fep = df[df["Impact Category"] == 'eutrophication: freshwater, freshwater eutrophication potential (FEP)']
ffp = df[df["Impact Category"] == 'energy resources: non-renewable, fossil, fossil fuel potential (FFP)']
tetp = df[df["Impact Category"] == 'ecotoxicity: terrestrial, terrestrial ecotoxicity potential (TETP)']
metp = df[df["Impact Category"] == 'ecotoxicity: marine, marine ecotoxicity potential (METP)']
fetp = df[df["Impact Category"] == 'ecotoxicity: freshwater, freshwater ecotoxicity potential (FETP)']
wcp = df[df["Impact Category"] == 'water use, water consumption potential (WCP)']

dataframes = {
    'climate change, global warming potential (GWP1000)': gwp,
    'acidification: terrestrial, terrestrial acidification potential (TAP)': tap,
    'photochemical oxidant formation: terrestrial ecosystems, photochemical oxidant formation potential: ecosystems (EOFP)': eofp,
    'photochemical oxidant formation: human health, photochemical oxidant formation potential: humans (HOFP)': hofp,
    'particulate matter formation, particulate matter formation potential (PMFP)': pmfp,
    'ozone depletion, ozone depletion potential (ODPinfinite)': odpinfinite,
    'material resources: metals/minerals, surplus ore potential (SOP)': sop,
    'land use, agricultural land occupation (LOP)': lop,
    'ionising radiation, ionising radiation potential (IRP)': irp,
    'human toxicity: non-carcinogenic, human toxicity potential (HTPnc)': htpnc,
    'human toxicity: carcinogenic, human toxicity potential (HTPc)': htpc,
    'eutrophication: marine, marine eutrophication potential (MEP)': mep,
    'eutrophication: freshwater, freshwater eutrophication potential (FEP)': fep,
    'energy resources: non-renewable, fossil, fossil fuel potential (FFP)': ffp,
    'ecotoxicity: terrestrial, terrestrial ecotoxicity potential (TETP)': tetp,
    'ecotoxicity: marine, marine ecotoxicity potential (METP)': metp,
    'ecotoxicity: freshwater, freshwater ecotoxicity potential (FETP)': fetp,
    'water use, water consumption potential (WCP)': wcp
}

# Text associated with each dropdown option
dropdown_texts = {
    'climate change, global warming potential (GWP1000)': '🌍\n\nAssesses the potential contribution of **greenhouse gases to global warming** and climate change, crucial for understanding long-term environmental impact.',
    'acidification: terrestrial, terrestrial acidification potential (TAP)': '🌱\n\nEvaluates the potential acidification impacts on terrestrial ecosystems, which can lead to **soil degradation** and **negative effects on plant life**.',
    'photochemical oxidant formation: terrestrial ecosystems, photochemical oxidant formation potential: ecosystems (EOFP)': '🌿\n\nMeasures the **potential formation of smog and other oxidants that can harm terrestrial ecosystems**, affecting biodiversity and ecosystem health.',
    'photochemical oxidant formation: human health, photochemical oxidant formation potential: humans (HOFP)': '👩‍⚕️\n\nQuantifies the **potential health impacts of smog and other oxidants on humans**, which can lead to respiratory problems and other health issues.',
    'particulate matter formation, particulate matter formation potential (PMFP)': '🌫️\n\nEstimates the potential formation of **particulate matter (PM2.5)** that can cause air pollution and pose significant health risks to humans.',
    'ozone depletion, ozone depletion potential (ODPinfinite)': '🌞\n\nMeasures the potential for substances to **deplete the stratospheric ozone layer**, which protects life on Earth from harmful ultraviolet radiation.',
    'material resources: metals/minerals, surplus ore potential (SOP)': '⚙️\n\nEvaluates the **potential depletion of metal and mineral resources**, indicating the environmental burden associated with raw material extraction.',
    'land use, agricultural land occupation (LOP)': '🏡\n\nAssesses the impact of **land occupation on agricultural areas**, which can affect food production and land availability.',
    'ionising radiation, ionising radiation potential (IRP)': '☢️\n\nQuantifies the potential impacts of **ionizing radiation on human health and the environment**, including risks from radioactive substances.',
    'human toxicity: non-carcinogenic, human toxicity potential (HTPnc)': '😷\n\nMeasures the **potential toxic effects of chemicals that are non-carcinogenic on human health**, important for ensuring safe environments.',
    'human toxicity: carcinogenic, human toxicity potential (HTPc)': '☠️\n\nAssesses the potential **carcinogenic impacts of chemicals on human health**, aiding in the regulation and management of hazardous substances.',
    'eutrophication: marine, marine eutrophication potential (MEP)': '🐠\n\nEvaluates the potential for **nutrient enrichment (eutrophication) in marine environments**, which can lead to algal blooms and ecosystem imbalance.',
    'eutrophication: freshwater, freshwater eutrophication potential (FEP)': '💧\n\nMeasures the potential for **nutrient enrichment in freshwater bodies**, causing algal blooms and affecting water quality and aquatic life.',
    'energy resources: non-renewable, fossil, fossil fuel potential (FFP)': '⛽\n\nAssesses the **depletion of fossil fuel resources**, emphasizing the importance of energy conservation and the transition to renewable sources.',
    'ecotoxicity: terrestrial, terrestrial ecotoxicity potential (TETP)': '🌲\n\nMeasures the potential **toxic impacts of chemicals on terrestrial ecosystems**, crucial for maintaining soil and plant health.',
    'ecotoxicity: marine, marine ecotoxicity potential (METP)': '🐋\n\nEvaluates the potential **toxic impacts of chemicals on marine ecosystems**, essential for protecting marine biodiversity.',
    'ecotoxicity: freshwater, freshwater ecotoxicity potential (FETP)': '🐟\n\nAssesses the potential **toxic impacts of chemicals on freshwater ecosystems**, vital for preserving aquatic life and water quality.',
    'water use, water consumption potential (WCP)': '🚰\n\nMeasures the potential **environmental impact of water consumption**, highlighting the importance of sustainable water use practices.'
}

# Define units for each dataframe
units = {
    'climate change, global warming potential (GWP1000)': 'kg CO2-eq',
    'acidification: terrestrial, terrestrial acidification potential (TAP)': 'kg SO2-eq',
    'photochemical oxidant formation: terrestrial ecosystems, photochemical oxidant formation potential: ecosystems (EOFP)': 'kg NMVOC-eq',
    'photochemical oxidant formation: human health, photochemical oxidant formation potential: humans (HOFP)': 'kg NOx-eq',
    'particulate matter formation, particulate matter formation potential (PMFP)': 'kg PM2.5-eq',
    'ozone depletion, ozone depletion potential (ODPinfinite)': 'kg CFC-11-eq',
    'material resources: metals/minerals, surplus ore potential (SOP)': 'kg Cu-eq',
    'land use, agricultural land occupation (LOP)': 'm2a',
    'ionising radiation, ionising radiation potential (IRP)': 'kBq U235-eq',
    'human toxicity: non-carcinogenic, human toxicity potential (HTPnc)': 'kg 1,4-DB-eq',
    'human toxicity: carcinogenic, human toxicity potential (HTPc)': 'kg 1,4-DB-eq',
    'eutrophication: marine, marine eutrophication potential (MEP)': 'kg N-eq',
    'eutrophication: freshwater, freshwater eutrophication potential (FEP)': 'kg P-eq',
    'energy resources: non-renewable, fossil, fossil fuel potential (FFP)': 'MJ',
    'ecotoxicity: terrestrial, terrestrial ecotoxicity potential (TETP)': 'kg 1,4-DB-eq',
    'ecotoxicity: marine, marine ecotoxicity potential (METP)': 'kg 1,4-DB-eq',
    'ecotoxicity: freshwater, freshwater ecotoxicity potential (FETP)': 'kg 1,4-DB-eq',
    'water use, water consumption potential (WCP)': 'm3'
}

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app



app.layout = [
    dbc.Card([
        dcc.Markdown('# LCA Dashboard', style={
            'text-align': 'center'
        }),
        html.P('A tool to assist with conscious consumerism of smartphones. Uses Brightway data from 2016.', style={
            'text-align':'center'
        })
        ], className= 'm-5'),

    dbc.Card([
        html.P('Select impact category:'),
        dcc.Dropdown(
            id='my-dropdown',
            options=[{'label': key, 'value': key} for key in dataframes.keys()],
            value='climate change, global warming potential (GWP1000)',  # Default value
            style={'width': '90%', 'height': '40px', 'font-size': '15px'},
            clearable = False
        ),
        dcc.Markdown(id='dropdown-text', style={
            'padding': '40px',
            'border': '2px solid #ddd',
            'border-radius': '5px',
            'background-color': '#f9f9f9',
            'margin-top': '20px',
            'font-size': '18px',
            'text-align': 'center'
        }),
        dcc.Graph(id='my-graph'),
        dash_table.DataTable(id='data-table')
    ], className= 'm-5'),

    dbc.Card([
        html.P('footer'),
    ], className= 'm-5')
]

# Define the callback to update the graph based on the dropdown selection
@app.callback(
    [Output('my-graph', 'figure'),
    Output('dropdown-text', 'children'),
    Output('data-table', 'data'),
    Output('data-table', 'columns')],
    [Input('my-dropdown', 'value')]
)
def update_graph(selected_df_key):
    df = dataframes[selected_df_key]
    
    max_score = df['Score'].max()
        
# Adjust the y-axis to encompass all the tops of the bars
    y_axis_range = [max_score * 0.975, max_score * 1.001]  # Extend range slightly above the max value
        
# Plot with dynamically adjusted y-axis range
    fig = px.bar(df, x='name', y='Score', color='name', 
                 color_discrete_sequence=["#E95824", "#009638", "#F7C600", "#002561", "#D72711"],
                 title=f'Scores by {selected_df_key}')
    
    unit = units[selected_df_key]

    fig.update_layout(
        yaxis=dict(
            title=unit,
            range=y_axis_range)
        )
    
    text = dropdown_texts.get(selected_df_key)

 # Prepare data and columns for the data table
    table_data = df.to_dict('records')
    table_columns = [{"name": col, "id": col} for col in df.columns]

    return fig, text, table_data, table_columns

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
