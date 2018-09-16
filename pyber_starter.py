
# coding: utf-8

# In[86]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
city_data = "data/city_data.csv"
ride_data= "data/ride_data.csv"

city_data_df = pd.read_csv(city_data)
ride_data_df = pd.read_csv(ride_data)


# In[87]:


combined_cityride_df = pd.merge(ride_data_df, city_data_df, how="left", on='city')
combined_cityride_df.head()


# In[141]:



plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare ($)")
x_limit = 60
x_axis = np.arange(0, x_limit, 1)
data = [random.random() for value in x_axis]

average_fare = combined_cityride_df["fare"]
Total_rides_per_city = combined_cityride_df["driver_count"]   

Urban, = plt.scatter(Total_rides_per_city, average_fare, marker="o", facecolors="red", edgecolors="white", label="Urban" )
Suburban, = plt.scatter(Total_rides_per_city, average_fare, marker="o", facecolors="blue", edgecolors="yellow", label="Suburban" )                       
Rural, = plt.scatter(Total_rides_per_city, average_fare, marker="o", facecolors="green", edgecolors="purple", label="Rural" )
plt.legend(handles=[Urban, Suburban, Rural], loc="best")
plt.ylim(0, 60)
plt.xlim(0, x_limit)
pl


# ## Total Fares by City Type

# In[88]:


CityFareType = combined_cityride_df.groupby(['type'])
count_CityFareType= CityFareType.sum()
count_CityFareType


# In[89]:


Type1=["Rural","Suburban","Urban"]
Fare = [4327.93,19356.33,39854.38]
colors = ["yellow", "blue", "pink"]
explode = (0, 0, 0.07)
plt.title("% of Total Fare by City Type")
plt.pie(Fare, explode=explode, labels=Type1, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=90)
plt.axis("equal")
plt.show()
# Save Figure


# ## Total Rides by City Type

# In[90]:


# Calculate Ride Percents

# Build Pie Chart

# Save Figure
cityride_df = pd.merge(ride_data_df, city_data_df, how="left", on='city')
CityType1 = cityride_df.groupby('type')
count_CityType= CityType1['type'].count()


# In[91]:


# Show Figure
Type=["Rural","Suburban","Urban"]
percent = [125,625,1625]
colors1 = ["yellow", "blue", "pink"]
explode1 = (0, 0, 0.07)
plt.title("% of Total Rides by City Type")
plt.pie(percent, explode=explode1, labels=Type, colors=colors1,
        autopct="%1.1f%%", shadow=True, startangle=90)
plt.axis("equal")
plt.savefig("../Images/PyPies.png")
plt.show()


# ## Total Drivers by City Type

# In[126]:



CityFareType2 = combined_cityride_df.groupby(['type'])
count_CityDriversType=CityFareType2.count()
count_CityDriversType.head()
Fare_=count_CityDriversType["fare"].sum()
Fare_


# In[97]:


# Show Figure
Type3=["Rural","Suburban","Urban"]
Driver = [537,8570,59602]
colors2 = ["yellow", "blue", "pink"]
explode2 = (0, 0, 0.07)
plt.title("% of Total Rides by City Type")
plt.pie(Driver, explode=explode2, labels=Type3, colors=colors2,
        autopct="%1.1f%%", shadow=True, startangle=90)
plt.axis("equal")

plt.show()

