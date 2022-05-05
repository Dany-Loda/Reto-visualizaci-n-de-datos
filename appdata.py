# -*- coding: utf-8 -*-
# Equipo dinamita

# Importar librerias
import dash # helps you initialize your application
import dash_core_components as dcc # allows you to create interactive components like graphs, dropdowns, or date ranges
import dash_html_components as html # lets you access HTML tags
import pandas as pd #  helps you read and organize the data

data = pd.read_csv("retoternium.csv")
del(data['Unnamed: 0'])

app = dash.Dash(__name__)
