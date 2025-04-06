import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Loading the Iris Dataset from Seaborn and inspecting it

iris = sns.load_dataset("iris")

print(iris.head(10))
print("")
print(iris.info(10))

#Plot the distribution

figure, ax = plt.subplots(2, 2, figsize=(10, 10))
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for i in range(len(features)):
    row = i // 2
    column = i % 2
    sns.histplot(data=iris, x=features[i], hue='species', kde=True, ax=ax[row][column])

plt.show()

#Finding the Best Fit

sns.lmplot(data=iris, x='sepal_length', y='petal_length', hue='species')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()

#Creating the Comparison Plots

sns.pairplot(iris, hue='species')
plt.show()

#Extracting Data from XML

def extract_data(xml):
    
    soup_data = BeautifulSoup(xml, "xml")
    
    data = {
        "name": [],
        "price": [],
        "description": [],
        "calories": []
    }

    foods = soup_data.find_all("food")
    
    for food in foods:
        data["name"].append(food.find("name").text)
        data["price"].append(food.find("price").text)
        data["description"].append(food.find("description").text.strip())
        data["calories"].append(food.find("calories").text)

    return data

#Creating the DataFrame

def create_df(data):
    df = pd.DataFrame(data)
    return df

#Extracting Data from HTML

def extract_campuses(html):
    
    soup_data = BeautifulSoup(html, "html.parser")
    
    campuses = soup_data.find_all("h1", class_ = "campus")
    campus_text = [campus.text for campus in campuses]
    
    return campus_text

#Extracting Elements

def extract_table(html):

    enrollment = pd.read_html(html)
    df = enrollment[0]
    return df