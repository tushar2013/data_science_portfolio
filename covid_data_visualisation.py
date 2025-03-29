# 1. Import Libraries
import pandas as pd
import plotly.express as px

# 2. Load Data
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv'
data = pd.read_csv(url)

# 3. Visualize
fig = px.choropleth(data, locations="Country_Region", locationmode="country names",
                    color="Confirmed", title="COVID-19 Confirmed Cases",
                    hover_name="Country_Region")
fig.show()
