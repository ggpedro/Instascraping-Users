import requests
import random
from bs4 import BeautifulSoup
import time

# Lista das contas a serem analisadas/ Users list to be updated
users = ('facebook', 'microsoft','michaeljackson', 'pgabrieltx', 'apple')

# Cabeçalho PT
print('Conta|Seguidores|Seguindo|Posts')

# Header EN
# print('User|Followers|Following|Posts')

# Para cada conta / For each user
for user in users:
    try:
        # Aguarda entre 3 e 14 segundos para simular o comportamento humano / Waits between 3 and 14 seconds to emulate humans interaction
        time.sleep(random.randint(3,14))
        
        # Obtem a página da conta / Go to each users page
        url = "https://www.instagram.com/" + user
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        # Obtenha o campo dos seguidores / Extract the number of followers
        followers = soup.find("meta", {"name": "description"})["content"]
        follower_count = followers.split("Followers")[0]
        follower_number = follower_count.replace(',','').replace('K','000').replace('M','000000')
        
        # Obtenha o texto da descrição / Extract the description text
        description = followers.split("Followers")[1]
       
        # Obtenha o número de contas que a conta analisada segue e o número de posts / Extract the users number of following and posts
        following_count = description[2:description.index(' Following')]
        following_number = following_count.replace(',','').replace('K','000')
        posts_count = description[description.index('wing, ')+6:description.index(' Posts')]
        posts_number = posts_count.replace(',','').replace('K','000')

        # Print os resultados / Print results
        print(user,'|', follower_number,'|', following_number,'|', posts_number)

    # Em caso de erro / In case of error
    except TypeError:
        print("User Does not exist")