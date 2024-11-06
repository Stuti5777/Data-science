import pandas as pd  # Importing the pandas library to work with data in tables

# Step 1: Creating a DataFrame from scratch to relate it with a dictionary
# A DataFrame is like a table of data; here, we’re creating one from a dictionary with three columns: "Name", "Age", and "City"
df = pd.DataFrame({
    "Name": ["Pulkit Chawla", "Tom Brouwers"],
    "Age": [23, 14],
    "City": ["Agra", "Amsterdam"]
})

# Displaying the first few rows of our DataFrame
# Run this line to see how the DataFrame looks with the default number of rows (5)
print(df.head())

# Checking the shape of our DataFrame
# This tells us the number of rows and columns in the DataFrame (rows, columns)
print(df.shape)

# Accessing a column like a dictionary
# We access a column (like "Name") as if it were a key in a dictionary to see all values under that column
print(df["Name"])

# Applying Numpy operations to a column
# Here, we use max() to get the oldest age in the "Age" column
print(df["Age"].max())

# Checking the type of the "Age" column
# The type shows us that each column is a pandas Series, which is like a single column of data
print(type(df["Age"]))

# Checking the shape of the "Age" column
# This tells us the number of elements in the column (rows,)
print(df["Age"].shape)

# Getting a summary of our DataFrame
# This shows the data types of each column and the memory usage, helpful for understanding the data structure
print(df.info())

# Getting basic statistics for numerical columns
# This provides summary statistics like mean, minimum, and maximum values for each numeric column (e.g., "Age")
print(df.describe())

# Step 2: Loading data from an external CSV file
# Here we’re loading data from a file, "titanic.csv", which contains information about Titanic passengers
# Run this part to view the first few rows after loading the data
data = pd.read_csv("titanic.csv")  # Make sure the file path is correct
print(data.head())
print(data.info())

# Checking the data types of each column in the Titanic dataset
print(data.dtypes)  # dtypes is an attribute that tells us what kind of data is in each column

# Selecting multiple columns together
# Here we create a smaller table with just the "Name" and "Age" columns
nameAndAge = data[["Name", "Age"]]
print(nameAndAge.head())  # Run this line to view the new table with only two columns
print(nameAndAge.shape)  # Check the shape to see the number of rows and columns

# Step 3: Filtering data based on a condition
# This creates a table with only the passengers who were above 35 years old
above35 = data[data["Age"] > 35]
print(above35.head())  # Run this to see the filtered list of passengers over 35
print(above35.shape)  # Check how many rows meet this condition

# Filtering based on multiple conditions
# This gives us passengers in class 2 or 3, i.e., the lower classes on the Titanic
class2And3 = data[data["Pclass"].isin([2, 3])]
print(class2And3[["Name", "Pclass"]].head())  # Run this to view a small table of passengers in class 2 or 3
print(class2And3.shape)

# Using OR (|) and AND (&) operators to combine conditions
# Here, we’re looking for passengers who are in either class 2 or class 3
class2And3 = data[(data["Pclass"] == 2) | (data["Pclass"] == 3)]
print(class2And3[["Name", "Pclass"]].head())  # This confirms the OR operation
print(class2And3.shape)

# Step 4: Calculating the mean fare of people in each Pclass and by gender
# We are calculating the average ticket price for passengers in different classes (Pclass) and by gender (Sex)
# Below, we calculate the mean fare for male passengers in first class
maleFirstClass = data[(data["Sex"] == "male") & (data["Pclass"] == 1)]
print("The mean fare of male first class passengers is", maleFirstClass["Fare"].mean())

# Repeat this for other combinations of class and gender
femaleFirstClass = data[(data["Sex"] == "female") & (data["Pclass"] == 1)]
maleSecondClass = data[(data["Sex"] == "male") & (data["Pclass"] == 2)]
femaleSecondClass = data[(data["Sex"] == "female") & (data["Pclass"] == 2)]
maleThirdClass = data[(data["Sex"] == "male") & (data["Pclass"] == 3)]
femaleThirdClass = data[(data["Sex"] == "female") & (data["Pclass"] == 3)]

# Printing mean fares for each category
# These lines show the average ticket price for each gender and class combination
print("The mean fare of female first class passengers is", femaleFirstClass["Fare"].mean())
print("The mean fare of male second class passengers is", maleSecondClass["Fare"].mean())
print("The mean fare of female second class passengers is", femaleSecondClass["Fare"].mean())
print("The mean fare of male third class passengers is", maleThirdClass["Fare"].mean())
print("The mean fare of female third class passengers is", femaleThirdClass["Fare"].mean())
