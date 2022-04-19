from instagrapi import Client

cl = Client()
cl.login("luiz63736", "JoseLuiz12@")
#Highlight
#story id
cl.highlight_create(title="teste", story_ids=[
                    "2819958370192608393", "2819958370192608393"])
