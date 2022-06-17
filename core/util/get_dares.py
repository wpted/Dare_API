import requests
from bs4 import BeautifulSoup


dare_website = "https://www.mantelligence.com/funny-dares/"

response = requests.get(url=dare_website)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

question_list = [str(question.get_text())[3:].strip() for question in soup.find_all(class_="quest")]




if __name__ == '__main__':
    print(question_list)

