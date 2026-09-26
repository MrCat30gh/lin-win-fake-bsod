import time
import psutil
import platform
import random
import sys

def show_linux_bsod():
    try:
        import tkinter as tk
        import qrcode
        from PIL import ImageTk, Image
    except ImportError:
        return

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='#0000BB')
    root.config(cursor="none")

    tux_ascii = (
        "    .--.       | | |\n"
        "   |o_o |      | | |\n"
        "   |:_/ |      | | |\n"
        "  //   \\ \\     (   )\n"
        " (|     | )     (_)\n"
        "/'\\_   _/`\\\n"
        "\\___)=(___/"
    )

    tux_label = tk.Label(
        root,
        text=tux_ascii,
        font=("Courier New", 14, "bold"),
        bg="#0000BB",
        fg="#FFFFFF",
        justify="left"
    )
    tux_label.place(x=50, y=50)

    panic_link = "Linux Kernel panic! Fuck your computer! Dont open somnitelniye ssilki!!! уалдщьл щльоа щывлшоа ошыоат шыыаыв ашоыв отавыщ соысщшмсо9ысшвоывщшьасывдлот смсль мщотсщлс ьавдьм тчсьтоьмащо"
    qr = qrcode.QRCode(version=1, box_size=8, border=2)
    qr.add_data(panic_link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    qr_photo = ImageTk.PhotoImage(qr_img)
    qr_label = tk.Label(root, image=qr_photo, bg="#0000BB")
    qr_label.image = qr_photo
    qr_label.place(relx=0.5, rely=0.4, anchor="center")


    info_text = (
        "KERNEL PANIC!\n\n"
        "Please reboot your computer.\n\n"
        "Fatal exception in interrupt"
    )

    info_label = tk.Label(
        root,
        text=info_text,
       font=("Courier New", 18, "bold"),
        bg="#0000BB",
        fg="#FFFFFF",
        justify="center"
    )
    info_label.place(relx=0.5, rely=0.75, anchor="center")

    root.after(60000, root.destroy)
    root.mainloop()

def trigger_terminal_chaos():
    psutil.cpu_percent(interval=None)
    time.sleep(0.1) 
    
    cpu_usage = psutil.cpu_percent(interval=None)
    if cpu_usage < 90:
        show_linux_bsod()

def start_game():
    print("Welcome to russian roulette. Press enter to shoot. 6 attempts. Good luck")
    bullet_slot = random.randint(1, 6)
    
    for attempt in range(1, 7):
        input()
        if attempt == bullet_slot:
            print("YOUR PC IS DEAD AXAXAXAXAXAXAXXAX\n")
            time.sleep(1)
            trigger_terminal_chaos()
            return
        else:
            if attempt < 6:
                print("You're still alive huh? Try again")
            else:
                print("Ok, I'll let you go, but never ever open a suspicious file before checking it. ESPECIALLY if its opensource!!!")

if __name__ == "__main__":
    start_game()

