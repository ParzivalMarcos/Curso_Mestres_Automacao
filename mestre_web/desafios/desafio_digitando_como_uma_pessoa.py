from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

class Challange:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--lang=pt-BR")
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe',
            options=chrome_options
        )
        self.text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque pulvinar pretium accumsan. Phasellus pharetra dui quis magna iaculis congue. Nullam ullamcorper molestie cursus. Donec vulputate augue a quam egestas efficitur. Curabitur non venenatis erat, eu molestie lectus. Sed sed nisl quis felis tempor mollis. Fusce vel felis mauris. Donec ornare ut massa nec scelerisque. Vestibulum sit amet vestibulum ex. Cras a elit lacinia, vehicula nisl at, ullamcorper nibh. Ut cursus fermentum augue, ut mollis nulla faucibus at. In hac habitasse platea dictumst. Mauris id diam sit amet quam vulputate feugiat. Etiam placerat rhoncus purus, vel efficitur magna ultrices a. Donec scelerisque sollicitudin dapibus. Nullam velit nisl, consequat id ullamcorper finibus, ullamcorper ut nulla."

    
    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/index.html")
        challange_button = self.driver.find_element_by_xpath("//a[text()='Desafios']")
        challange_button.click()

        text_field = self.driver.find_element_by_id("campoparagrafo")
        self.type_like_a_person(self.text, text_field)


    def type_like_a_person(self, text, element):
        for letter in text:
            element.send_keys(letter)
            sleep(random.randint(1, 5) / 30)

challange = Challange()
challange.Start()