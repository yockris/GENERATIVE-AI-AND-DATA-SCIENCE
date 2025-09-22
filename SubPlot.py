import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('company_sales_data.csv')

print (data)

# extract colums
months = data['month_number']
bathing_soap = data['bathingsoap']
face_wash = data['facewash']

# create subplots (2 rows, 1 column)
fig, ax  = plt.subplots(2, 1, figsize=(8, 6))


# plot bathing soap sales in the first subplot
ax[0].plot(months, bathing_soap, marker='o', color='blue', linestyle='-')
ax[0].set_title('Bathing Soap Sales Per Month')
ax[0].set_ylabel('units sold')
ax[0].grid(True)


#  plot face wash sales in the second subplot
ax[1].plot(months, face_wash, marker='o', color='green', linestyle='-')
ax[1].set_title('Face Wash Sales Per Month')
ax[1].set_ylabel('units sold')
ax[1].set_xlabel('Month Number')
ax[1].grid(True)

# ROtate x-axis labels for better readability
plt.setp(ax[0].xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax[1].xaxis.get_majorticklabels(), rotation=45)

# adjust layout to prevent overlap
plt.tight_layout()

# display the plot
plt.show()

