import tkinter as tk

BEST_SCORE_FILE = "bestscore.txt"

def loadBestScore():
    try:
        with open(BEST_SCORE_FILE, "r") as file:
            bestScore = int(file.read())
    except (FileNotFoundError, ValueError):
        bestScore = 0
    return bestScore

def saveBestScore(score):
    with open(BEST_SCORE_FILE, "w") as file:
        file.write(str(score))

def onClick():
    global clickCount, bestScore
    clickCount += 1
    clickLabel.config(text=f"Number of clicks: {clickCount}")

    if clickCount > bestScore:
        bestScore = clickCount
        bestScoreLabel.config(text=f"Better result: {bestScore}")
        saveBestScore(bestScore)

clickCount = 0
bestScore = loadBestScore()

root = tk.Tk()
root.title("TaskClicker")

bestScoreLabel = tk.Label(root, text=f"Better result: {bestScore}", font=("Helvetica", 16))
bestScoreLabel.pack(pady=10)

clickLabel = tk.Label(root, text=f"Number of clicks: {clickCount}", font=("Helvetica", 16))
clickLabel.pack(pady=10)

clickButton = tk.Button(root, text="click", font=("Helvetica", 14), command=onClick)
clickButton.pack(pady=20)

root.geometry("300x200")
root.resizable(True, True)

root.mainloop()
