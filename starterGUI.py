import customtkinter
import tkinter
import requests
from termcolor import colored
import sys
import time
app = customtkinter.CTk()

app.geometry("1920x1080")
app.title("GEN98")
rasa_server_url = "http://localhost:5005" 
conversation_id = "default"
def clearChat():
    Output_box.configure(state='normal')
    Output_box.delete(0.0,"end")
    Output_box.configure(state='disabled')
def GetandDisplayResponse():
    text = input_box.get()
    input_box.delete(0,"end")
    user_message = text
    Output_box.configure(state='normal')
    Output_box.tag_config("1", foreground = "Yellow")
    Output_box.tag_config("2", foreground = "green")
    user_input_url = f"{rasa_server_url}/webhooks/rest/webhook"
    payload = {
                    "sender": conversation_id,
                    "message": user_message
                    }
    Output_box.insert(tkinter.END, "You->")
    Output_box.insert(tkinter.END, user_message+"\n", "1")
    Output_box.insert(tkinter.END, "RASA-> ")
    response = requests.post(user_input_url, json=payload)
    bot_responses = response.json()
    for bot_response in bot_responses:
            bot_response['text'] = bot_response['text'] + "\n"
            for i in bot_response['text']:
                Output_box.insert(tkinter.END, i,"2")
   
    
    Output_box.configure(state='disabled')
welcome_box = customtkinter.CTkLabel(master=app, text="""Welcome to the MNNIT BotRush Assistant!

I'm here to provide you with all the information you need about Motilal Nehru National Institute of Technology (MNNIT) and the exciting BotRush event. Whether you have questions about the college, event details, or anything else, feel free to ask, and I'll do my best to assist you.

To get started, simply type your questions or topics of interest, and I'll provide you with relevant information. Let's explore the world of MNNIT and the thrilling BotRush event together!
""",font=("Comic Sans MS",14), width=120,height=25,corner_radius=8,wraplength=700,text_color=("#BF9553"))
welcome_box.place(relx=0.5, rely=0.15, anchor = tkinter.CENTER)
input_box = customtkinter.CTkEntry(master = app,justify="center", width = 1000,placeholder_text="Your input message here",font=("Comic Sans MS", 14))
input_box.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)
side_panel = tkinter.Frame(app, width=350, bg="#333333")
side_panel.pack(fill="y", side="left")

# Create a banner label inside the side panel
banner = tkinter.Label(side_panel, text="MNNIT ROBOTICS CLUB", font=("Comic Sans MS", 16), bg="#333333",fg="white", padx=10, pady=10)
banner.pack(fill="x")
submit_button = customtkinter.CTkButton(master=app, width = 80, text="Submit", font =("Comic Sans MS",15),command=GetandDisplayResponse)
submit_button.place(relx = 0.5,rely=0.35, anchor = tkinter.CENTER)
Output_box = customtkinter.CTkTextbox(master = app, width = 1000,corner_radius=30,border_spacing=1,height=450,font=("Comic Sans MS",16))
Output_box.place(relx=0.5,rely=0.66, anchor = tkinter.CENTER)
Output_box.configure(state='disabled')
clear_button = customtkinter.CTkButton(master=app, width = 45, text="Clear Chat", font =("Comic Sans MS",10),command=clearChat)
clear_button.place(relx=0.25,rely=0.95, anchor = tkinter.CENTER)
app.mainloop()