#Shivam Deswal
#Coin Change DP Visualizer
import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
# function to calculate the minimum number of coins required to make change for a given amount
def minCoins(coins, m):
    n = len(coins)
    dp = [[float('inf')] * (m+1) for i in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 0
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if coins[i-1] <= j:
                dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1)
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][m], dp

# function to display the minimum number of coins required to make change for a given amount
def display_result():
    coins = list(map(int, coin_entry.get().split(',')))
    m = int(amount_entry.get())
    result, dp = minCoins(coins, m)
    result_label.config(text="Minimum number of coins required: {}".format(result))
    
    # clear previous selected coins
    for child in coins_frame.winfo_children():
        child.destroy()
        
    # display selected coins
    used_coins = []
    i, j = len(coins), m
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            used_coins.append(coins[i-1])
            j -= coins[i-1]
            
    # create string of used coins
    used_coins_str = "Coins used: " + "+".join(map(str, used_coins))
    
    # display string in message box
    tk.messagebox.showinfo(title="Selected Coins", message=used_coins_str)


# function to reset the result, coins, and amount entries
def reset_result():
    coin_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    result_label.config(text="")
    
    # clear previous selected coins
    for child in coins_frame.winfo_children():
        child.destroy()

# create tkinter window
window = tk.Tk()
window.title("Coin Change Problem Visualizer")
window.geometry("500x400")

#background image
bg_image = Image.open("money.jpg")
bg_image = ImageTk.PhotoImage(bg_image,width="500px")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# create input widgets
coin_label = tk.Label(window, text="Enter coin denominations (separated by commas):", font=("Helvetica", 14))
coin_label.pack(pady=10)
coin_entry = tk.Entry(window, font=("Helvetica", 14))
coin_entry.pack()

amount_label = tk.Label(window, text="Enter amount to make change for:", font=("Helvetica", 14))
amount_label.pack(pady=10)

amount_entry = tk.Entry(window, font=("Helvetica", 14))
amount_entry.pack()

# create button to display result
submit_button = tk.Button(window, text="Find minimum number of coins", font=("Helvetica", 14), command=display_result)
submit_button.pack(pady=10)

# create label to display result
result_label = tk.Label(window, font=("Helvetica", 14))
result_label.pack(pady=10)

# create frame to display selected coins
coins_frame = tk.Frame(window)
coins_frame.pack(pady=10)

# create button to reset the result
reset_button = tk.Button(window, text="Reset", font=("Helvetica", 14), command=reset_result)
reset_button.pack(pady=10)

# set focus to coin entry on startup
coin_entry.focus()

# start the tkinter event loop
window.mainloop()