import pandas as pd
import re
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv("databreaches650.csv")

# Filter the data for the year 2012 and onwards
data = data[data['BreachDate'] >= '2012-01-01']

# Create a dictionary to store the counts of each data class
data_classes = {}

# Loop through each row of the dataset and count the number of breaches that contain each data class
for row in data['DataClasses']:
    # Remove square brackets and whitespace from the data classes
    cleaned_classes = re.sub('[\[\]\s]', '', row)
    for data_class in cleaned_classes.split(','):
        if data_class in data_classes:
            data_classes[data_class] += 1
        else:
            data_classes[data_class] = 1

# Sort the data classes by the number of breaches and take the top 20
top_data_classes = sorted(data_classes.items(), key=lambda x: x[1], reverse=True)[:20]

# Create a bar chart to show the top 20 most breached data classes
plt.bar([x[0] for x in top_data_classes], [x[1] for x in top_data_classes])
plt.xticks(rotation=90)
plt.xlabel('Breached Data Classes')
plt.ylabel('Number of Breaches')
plt.title('Top 20 Most Breached Data Classes ')
plt.show()
