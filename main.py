from deal_finder_brain import DealFinderBrain
from email_sender import EmailSender

deal_finder = DealFinderBrain()
my_email_sender = EmailSender()

with open("games.txt", "r") as game_text:
    data = game_text.readlines()
    final_data = [i.strip("\n") for i in data]

for game in final_data:
    # print(game)
    result = ""
    sale_list = deal_finder.get_deals_for_game(game)
    for sale in sale_list:
        result += f"{sale}\n"

if result:
    my_email_sender.send_email(result)
else:
    print("No games on Sale")


