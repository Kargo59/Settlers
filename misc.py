############################    function that defines what happens after clicking the 'year of plenty' button     ##################################################################
def year_of_plenty():
    player1_knight_card.place_forget()
    player1_year_of_plenty_card.place_forget()
    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()
    player1_road_building_card.place_forget()
    player1_monopoly_card.place_forget()

    player1_roll_dice['state'] = 'disable'
    player1_trade['state'] = 'disable'
    player1_use_dev_card['state'] = 'disable'
    player1_build['state'] = 'disable'
    player1_end_turn['state'] = 'disable'
    player1_confirm['state'] = 'disable'
    player1_cancel['state'] = 'disable'

    # Toplevel object which will
    # be treated as a new window
    year_of_plenty = Toplevel(root)

    #what happens when 'X' on the top bar is clicked
    def on_exit():
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'
        year_of_plenty.destroy()

    year_of_plenty.protocol("WM_DELETE_WINDOW", on_exit)


    # sets the title of the Toplevel widget
    year_of_plenty.title("Year of plenty")

    # sets the geometry of toplevel
    year_of_plenty.geometry("300x250")

    # puts the new window in the center
    width = root.winfo_x()
    height = root.winfo_y()
    year_of_plenty.geometry("+%d+%d" % (width + 700, height + 400))

    # Make topLevelWindow remain on top until destroyed, or attribute changes.
    year_of_plenty.attributes('-topmost', 1)

    # A Label widget to show in toplevel - this 'dummy' label is made to put two other columns in the middle on the window
    Label(year_of_plenty, text="            ", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0, column=0, columnspan=1)

    # A Label widget to show in toplevel
    Label(year_of_plenty, text="Draw 2 cards from the bank", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0, column=1,
                                                                                                  columnspan=1)

    # funtion that closes  the "trade bank" new window

    def close_window():
        year_of_plenty.destroy()
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'

        # what happens after the 'confirm' button is clicked

    def confirm_bank():
        if v.get() == 'Brick':
            Player_1.brick +=2
            brick.set(Player_1.brick)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Lumber':
            Player_1.lumber += 2
            lumber.set(Player_1.lumber)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Wheat':
            Player_1.hay += 2
            hay.set(Player_1.hay)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Sheep':
            Player_1.sheep += 2
            sheep.set(Player_1.sheep)
        elif v.get() == 'Rock':
            Player_1.rock += 2
            rock.set(Player_1.rock)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'



        else:
            year_of_plenty.attributes('-topmost', 0)
            messagebox.showinfo("", "Choose a resource!")
            year_of_plenty.attributes('-topmost', 1)







    # Tkinter string variable
    # able to store any string value
    v = StringVar(year_of_plenty, "None")



    # Dictionary to create multiple buttons
    values_1 = {"Brick": "Brick",
                "Lumber": "Lumber",
                "Sheep": "Sheep",
                "Wheat": "Wheat",
                "Rock": "Rock"}

    y = 1

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values_1.items():
        Radiobutton(year_of_plenty, width=10, text=text, variable=v,
                    value=value, indicator=0,
                    background="lightskyblue").grid(row=y, column=1, columnspan=1)
        y += 1


    # 'cancel' button inside this window
    cancel_bank = Button(year_of_plenty, width=3, height=1, bg='white', text=chr(10008), fg='red', \
                         font=('Times New Roman', 20), \
                         command=close_window).grid(row=6, column=1, columnspan=1, padx=10, pady=20, sticky=W)

    # 'confirm' button inside this window
    confirm_bank = Button(year_of_plenty, width=3, height=1, bg='white', text=chr(10003), fg='green', \
                          font=('Times New Roman', 20), \
                          command=confirm_bank).grid(row=6, column=1, columnspan=1, padx=10, pady=20, sticky=E)


#####################################################                                                                  ###########################################
