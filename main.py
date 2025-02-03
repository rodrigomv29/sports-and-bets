"""
import os
import json
from dotenv import load_dotenv
from llamaapi import LlamaAPI

load_dotenv()
api_key = os.getenv("LLAMA_API_KEY")

llama = LlamaAPI(api_key)

api_request_json = {
    "model": "llama3.1-70b",
    "messages": [
        {"role": "user", "content": "Explain the math behind money betting lines and what over/under means?"},
    ], 
}

# Execute the Request
response = llama.run(api_request_json)
try:
    print(json.dumps(response.json(), indent=2))
except:
    print("\n\n\n\n\n " + response.text)

"""
from tkinter import *
from tkinter import ttk
class SportsBettingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Betting App")

        self.mainframe = ttk.Frame(root, padding="10 10 10 10")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.bet_amount = StringVar()
        self.odds = StringVar()
        self.result = StringVar()

        ttk.Label(self.mainframe, text="Bet Amount:").grid(column=1, row=1, sticky=W)
        self.bet_amount_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.bet_amount)
        self.bet_amount_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.mainframe, text="Odds:").grid(column=1, row=2, sticky=W)
        self.odds_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.odds)
        self.odds_entry.grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.mainframe, text="Calculate", command=self.calculate_winnings).grid(column=3, row=3, sticky=W)

        ttk.Label(self.mainframe, text="Potential Winnings:").grid(column=1, row=4, sticky=W)
        ttk.Label(self.mainframe, textvariable=self.result).grid(column=2, row=4, sticky=(W, E))

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def calculate_winnings(self):
        try:
            bet = float(self.bet_amount.get())
            odds = float(self.odds.get())
            winnings = bet * odds
            self.result.set(f"${winnings:.2f}")
        except ValueError:
            self.result.set("Invalid input")

root = Tk()
app = SportsBettingApp(root)
root.mainloop()
