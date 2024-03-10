"""Graphs for tuberculosis death rates in African countries"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV
data = pd.read_csv('tuberculosis1.csv')
print(data)


# Make a line graph of the data
def plot_line_graph(data):
    """Plots a line graph of the data for the five latest years"""
    plt.figure(figsize=(18, 7))

    # Plot data for line graph - 5 plots
    plt.plot(data['Country Name'], data['2022'], label='2022')
    plt.plot(data['Country Name'], data['2021'], label='2021')
    plt.plot(data['Country Name'], data['2020'], label='2020')
    plt.plot(data['Country Name'], data['2019'], label='2019')
    plt.plot(data['Country Name'], data['2018'], label='2018')

    # Adding labels and legend
    plt.xlabel('Country', fontsize=20)
    plt.ylabel('Tuberculosis Death Rate ', fontsize=20)
    plt.title('Tuberculosis Death Rate in Africa (per 100,000 people)', fontsize=25)
    plt.xticks(rotation=90, fontsize=18)
    plt.yticks(fontsize=20)
    plt.legend()
    plt.margins(x=0)
    plt.tight_layout()
    plt.savefig('line_plot_1.png')
    plt.show()


plot_line_graph(data)


# Make a 2nd line graph with a sample from data
def plot_2nd_line_graph(data):
    """Plots a line graph of tuberculosis deaths for 22 years for 4 countries"""
    # Subset rows; Nigeria, Algeria, Somalia and Botswana
    nigeria = data[data['Country Name'] == 'Nigeria']
    print(nigeria)

    algeria = data[data['Country Name'] == 'Algeria']
    print(algeria)

    somalia = data[data['Country Name'] == 'Somalia']
    print(somalia)

    botswana = data[data['Country Name'] == 'Botswana']
    print(botswana)

    plt.figure(figsize=(12, 6))

    # Plot data for 4 countries
    plt.plot(nigeria.columns[1:], nigeria.values.flatten()[1:], marker='o', label='Nigeria')
    plt.plot(algeria.columns[1:], algeria.values.flatten()[1:], marker='o', label='Algeria')
    plt.plot(somalia.columns[1:], somalia.values.flatten()[1:], marker='o', label='Somalia')
    plt.plot(botswana.columns[1:], botswana.values.flatten()[1:], marker='o', label='Botswana')

    # Adding labels and legend
    plt.xlabel('Year', fontsize=20)
    plt.xticks(rotation=30, fontsize=12)
    plt.ylabel('Tuberculosis Deaths', fontsize=18)
    plt.title('Tuberculosis Deaths Over the Years in 4 African countries', fontsize=18)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('line_plot_2.png')
    plt.show()


plot_2nd_line_graph(data)


# Make bar chart for years 2000 and 2022
def plot_bar_chart(data):
    """Plots a bar chart of the data for the years 2000 and 2022"""
    plt.figure(figsize=(20, 8))

    # Plotting the bar chart
    plt.bar(data['Country Name'], data['2000'], alpha=0.7, edgecolor='black',
            label='2000', color='blue')
    plt.bar(data['Country Name'], data['2022'], alpha=0.7, edgecolor='black',
            label='2022', color='aqua')

    # Adding labels and legend
    plt.xlabel('Country', fontsize=20)
    plt.ylabel('Tuberculosis death rate', fontsize=20)
    plt.xticks(rotation=90, fontsize=18)
    plt.yticks(fontsize=20)
    plt.title('Death recorded by country in years 2000 & 2022', fontsize=22)
    plt.legend()
    plt.tight_layout()
    plt.savefig('bar_chart.png')
    plt.show()


plot_bar_chart(data)


# Make a scatter plot with Max and Min values
def plot_scatter_graph(data):
    """Plots a scatter graph of the all-time highest/lowest deaths recorded for each country"""

    # Make new rows; Max_Value, Min_Value
    data['Max_Value'] = data.iloc[:, 1:].max(axis=1)
    data['Min_Value'] = data.iloc[:, 1:].min(axis=1)
    print(data)

    plt.figure(figsize=(16, 8))

    # Plot the scatter graph
    plt.scatter(data['Country Name'], data['Max_Value'], s=100, label='Max', color='red')
    plt.scatter(data['Country Name'], data['Min_Value'], s=100, label='Min', color='lime')

    # Add labels and legend
    plt.xlabel('Country', fontsize=20)
    plt.ylabel('Tuberculosis Death (per 100,000 people)', fontsize=15)
    plt.xticks(rotation=90, fontsize=18)
    plt.yticks(fontsize=20)
    plt.title('Maximum and Minimum deaths for any year by African Country', fontsize=22)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('scatter_plot.png')
    plt.show()


plot_scatter_graph(data)
