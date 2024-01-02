import altair as alt
from vega_datasets import data
import vegafusion as vf
vf.enable()

source = data.cars()

line = alt.Chart(source).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)'
)

band = alt.Chart(source).mark_errorband(extent='ci').encode(
    x='Year',
    y=alt.Y('Miles_per_Gallon').title('Miles/Gallon'),
)

a = line+band
a.save('chart.png')