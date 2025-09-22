import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('company_sales_data.csv')

print (data)

# plot total profit as a line plot
plt.plot(data['month_number'], data['total_profit'], marker='o', color='blue', linestyle='-')

# add title and labels
plt.title('Company Profit Per Month')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')

# rotate x-axis labels for better readability
plt.xticks(data['month_number'], rotation=45)

# display the plot  
plt.show()