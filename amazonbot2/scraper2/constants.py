import pandas as pd 
# from webdriver_manager.chrome import ChromeDriverManager

# Automatically download and manage ChromeDriver
# driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.amazon.in/ref=nav_logo"
df=pd.read_excel(r"C:\Users\mail2\Documents\lpth\selenium\project\amazonbot2\scraper2\amazon.xlsx")

link_list=[]
print(df.columns)
start = 0

for i in range(start,4):
    link=(df['ASIN'][i])
    link_list.append(link)
print(link_list[:4])
