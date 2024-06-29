import tkinter.messagebox
import requests
import json
from random import randint
import tkinter
import customtkinter
import markdown
from tkhtmlview import HTMLLabel


def loot_crate(quality):
    popup = customtkinter.CTk()
    popup.title("DnD loot crate")

    with open(f"{quality}.json", "r") as file:
        data = json.load(file)
    
    id = randint(1,len(data))
    item = data[id - 1]
    address = item["url"]

    url = f"https://www.dnd5eapi.co/{address}"

    payload = {}
    headers = {
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)

    name = data["name"]
    category = data["equipment_category"]["name"]
    rarity = data["rarity"]["name"]

    if quality == "uncommon":
        color = "gray"
    elif quality == "rare":
        color = "green"
    elif quality == "veryrare":
        color = "purple"
    elif quality == "legendary":
        color = "yellow"

    name = tkinter.StringVar(value=name)
    label1 = customtkinter.CTkLabel(master=popup, 
                                textvariable = name,
                                width=120,
                                height=25,
                                fg_color=("black"),
                                font=("CTkFont", 30),
                                corner_radius=8)
    label1.place(relx=1, rely=10, anchor=tkinter.CENTER)
    label1.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    

    rarity = tkinter.StringVar(value=rarity)
    label2 = customtkinter.CTkLabel(master=popup, 
                                textvariable = rarity,
                                width=120,
                                height=25,
                                fg_color=(color),
                                font=("CTkFont", 20),
                                text_color= "black",
                                corner_radius=8)
    label2.place(relx=1, rely=10, anchor=tkinter.CENTER)
    label2.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

    category = tkinter.StringVar(value=category)
    label3 = customtkinter.CTkLabel(master=popup, 
                                textvariable = category,
                                width=120,
                                height=25,
                                fg_color=("black"),
                                font=("CTkFont", 20),
                                corner_radius=8)
    label3.place(relx=1, rely=10, anchor=tkinter.CENTER)
    label3.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    details = "<br />".join(data['desc'])
    detailshtml = markdown.markdown(details, extensions=['markdown.extensions.tables'])
    detailshtml = detailshtml

    htmllabel = HTMLLabel(popup, html=detailshtml)

    htmllabel.grid(row=3, column=0, padx=20, pady=20)
    
    # message = tkinter.Message(popup,
    #                           text= details,
    #                           font=("CTkFont", 15))

    # message.grid(row=3, column=0, padx=20, pady=20)

    print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")
    print(f"************* {name} *************")
    print("********************************************************")
    print(f"category: {category}")
    print(f"rarity: {rarity}")
    print("********************************************************")
    print("Details:")
    for desc in data["desc"]:
        print(desc)
    print("********************************************************")
    print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")    

    popup.mainloop()

