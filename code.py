import os
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter  # importing tkinter module
import mysql.connector as sq

global username
global fullname
global addressline1
global addressline2
global city
global pincode
global phonenum


def app():
    def order():
        window_main = tkinter.Tk()  # creating main window
        bg1 = Image.open("omg.png")
        render = ImageTk.PhotoImage(bg1)
        img = tkinter.Label(image=render)
        img.image = render
        img.place(x=0, y=0)

        window_main.geometry("1280x720")  # setting the revolution
        window_main.title("FoodJet")  # window name
        window_main.configure(bg="ghostwhite")
        # intro = Image.open("omg.png")
        # render = ImageTk.PhotoImage(intro)
        # img = tkinter.Label(image=render)
        # img.image = render
        # img.place(x=520, y=10)
        # head=tkinter.Label(window_main,text="   FoodJET   ",font=("League Spartan",32),fg="White",bg="slateblue1") #foodjet
        # head.place(x=520,y=10) #Position of foodjet
        cartitems = []
        mos = ''

        def address():
            try:
                w1.destroy()
            except:
                pass

            def errorcheck():
                global fullname
                global addressline1
                global addressline2
                global city
                global pincode
                global phonenum
                fullname = ad1.get()
                addressline1 = ad2.get()
                addressline2 = ad3.get()
                city = ad4.get()
                pincode = ad5.get()
                phonenum = ad6.get()

                if ad1.get() != "" and ad2.get() != "" and ad4.get() != "" and ad5.get() != "" and ad6.get() != "":

                    if ad1.get().replace(" ", "").isalpha() and ad2.get().replace(" ", "").replace("-", "").replace(",",
                                                                                                                    "").replace(
                            ".", "").replace("/", "").replace(":", "").replace("\ ", "").replace("&", "").replace(";",
                                                                                                                  "").isalnum() and ad4.get().replace(
                            " ", "").isalpha() and ad5.get().replace(" ", "").isnumeric() and ad6.get().replace(" ",
                                                                                                                "").isnumeric():
                        if len(ad5.get()) == 6:
                            if len(ad6.get()) == 10:
                                wind.destroy()
                                payment()
                            else:
                                con = tkinter.Label(wind,
                                                    text="                                                          ",
                                                    font=("Lexend Deca", 20), fg="white", bg="#5754F6").place(x=370,
                                                                                                              y=550)
                                con = tkinter.Label(wind, text="Phone Number Incorrect!", font=("Lexend Deca", 15),
                                                    fg="white", bg="#5754F6").place(x=370, y=550)
                                # bon=tkinter.Button(wind,text="RESET",command=address, font=("Lexend Deca",21),fg="white",bg="RED").place(x=200,y=550)

                        else:
                            con = tkinter.Label(wind,
                                                text="                                                               ",
                                                font=("Lexend Deca", 20), fg="white", bg="#5754F6").place(x=370, y=550)
                            con = tkinter.Label(wind, text="Pincode Incorrect!", font=("Lexend Deca", 15), fg="white",
                                                bg="#5754F6").place(x=370, y=550)
                            # bon=tkinter.Button(wind,text="RESET",command=address, font=("Lexend Deca",21),fg="white",bg="RED").place(x=200,y=550)


                    else:
                        con = tkinter.Label(wind,
                                            text="                                                               ",
                                            font=("Lexend Deca", 20), fg="white", bg="#5754F6").place(x=370, y=550)
                        # bon=tkinter.Button(wind,text="RESET",command=address, font=("Lexend Deca",21),fg="white",bg="RED").place(x=200,y=550)
                        con = tkinter.Label(wind, text="Information Entered Incorrect!", font=("Lexend Deca", 15),
                                            fg="white", bg="#5754F6").place(x=370, y=550)

                else:
                    con = tkinter.Label(wind,
                                        text="                                                                            ",
                                        font=("Lexend Deca", 20), fg="white", bg="#5754F6").place(x=370, y=550)
                    # bon=tkinter.Button(wind,text="RESET",command=address, font=("Lexend Deca",21),fg="white",bg="RED").place(x=200,y=550)
                    con = tkinter.Label(wind, text="You Can't Leave Required Fields Empty!", font=("Lexend Deca", 15),
                                        fg="white", bg="#5754F6").place(x=370, y=550)

            wind = tkinter.Tk()  # creating main window
            wind.geometry("1280x720")  # setting the revolution
            wind.title("ADDRESS")  # window name
            pay = Image.open("pay.png")
            render = ImageTk.PhotoImage(pay)
            img = tkinter.Label(image=render)
            img.image = render
            img.place(x=0, y=0)
            try:
                chandu_window.destroy()
                shyam_window.destroy()
                binod_window.destroy()
                mukesh_window.destroy()
                sharma_window.destroy()
                bablu_window.destroy()
            except:
                pass

            con = tkinter.Label(wind, text="ENTER YOUR ADDRESS HERE!", font=("Lexend Deca", 25), fg="#4F4BF6",
                                bg="white", ).place(x=500, y=5)
            con = tkinter.Label(wind, text="FULL NAME", font=("League Spartan", 17), fg="white", bg="#5754F6").place(
                x=200, y=70)
            con = tkinter.Label(wind, text="(compulsory, only alphabets)", font=("Raleway Black", 10), bg="#5754F6",
                                fg="yellow").place(x=200, y=105)
            global ad1
            ad1 = tkinter.Entry(wind, width=30, font=("League Spartan", 17), fg="black", bg="white")
            ad1.place(x=500, y=70)

            fullname = ad1.get()

            con = tkinter.Label(wind, text="ADDRESS LINE 1", font=("League Spartan", 17), fg="white",
                                bg="#5754F6").place(x=200, y=130)
            con = tkinter.Label(wind, text="(compulsory, only alphanumeric)", font=("Raleway Black", 10), bg="#5754F6",
                                fg="yellow", ).place(x=200, y=160)
            global ad2
            ad2 = tkinter.Entry(wind, width=40, font=("League Spartan", 17), fg="red", bg="white")
            ad2.place(x=500, y=130)

            addressline1 = ad2.get()
            con = tkinter.Label(wind, text="ADDRESS LINE 2", font=("League Spartan", 17), fg="white",
                                bg="#5754F6").place(x=200, y=200)
            con = tkinter.Label(wind, text="(optional, only alphanumeric)", font=("Raleway Black", 10), bg="#5754F6",
                                fg="yellow").place(x=200, y=230)
            global ad3
            ad3 = tkinter.Entry(wind, width=40, font=("League Spartan", 17), fg="red", bg="white")
            ad3.place(x=500, y=200)

            addressline2 = ad3.get()

            con = tkinter.Label(wind, text="CITY", font=("League Spartan", 17), fg="white", bg="#5754F6").place(x=200,
                                                                                                                y=260)
            con = tkinter.Label(wind, text="(compulsory, only alphabets)", font=("Raleway Black", 10), bg="#5754F6",
                                fg="yellow").place(x=200, y=290)
            global ad4
            ad4 = tkinter.Entry(wind, width=20, font=("League Spartan", 17), fg="RED", bg="white")
            ad4.place(x=500, y=270)

            city = ad4.get()

            con = tkinter.Label(wind, text="PINCODE", font=("League Spartan", 17), fg="white", bg="#5754F6").place(
                x=200, y=313)
            con = tkinter.Label(wind, text="(compulsory, only 6-digits)", font=("Raleway Black", 10), bg="#5754F6",
                                fg="yellow").place(x=200, y=350)
            global ad5
            ad5 = tkinter.Entry(wind, width=6, font=("League Spartan", 17), fg="RED", bg="white")
            ad5.place(x=500, y=330)

            pincode = ad5.get()

            con = tkinter.Label(wind, text="PHONE NUMBER (+91)", font=("League Spartan", 17), fg="white",
                                bg="#5754F6").place(x=200, y=380)
            con = tkinter.Label(wind, text="(compulsory, only 10-digits)", font=("Raleway Black", 10), bg="#5754F6",
                                fg="yellow").place(x=200, y=415)
            global ad6
            ad6 = tkinter.Entry(wind, width=10, font=("League Spartan", 17), fg="RED", bg="white")
            ad6.place(x=500, y=380)

            phonenum = ad6.get()

            con = tkinter.Label(wind, text="CLICK SUBMIT TO GO TO PAYMENT PAGE", font=("Lexend Deca", 23), fg="black",
                                bg="#FAFF00").place(x=200, y=470)
            bon = tkinter.Button(wind, text="SUBMIT", command=errorcheck, font=("Lexend Deca", 21), fg="white",
                                 bg="#FF0000").place(x=870, y=470)

        def chandu_menu():  # Adding Items from The Spice Route to Cart
            def ord_fin():
                mos = ''
                for jd in range(0, len(cart)):
                    mos = mos + "\n" + str(cartitems[jd])

                chandu_window.destroy()
                global w1
                w1 = tkinter.Tk()
                w1.title("ORDER DETAILS")
                w1.geometry("1280x720")
                w1.configure(bg="deep sky blue")

                thnxpic = Image.open("thnx.png")
                render = ImageTk.PhotoImage(thnxpic)
                img = tkinter.Label(image=render)
                img.image = render
                img.place(x=0, y=0)

                # inputtxt = Text(w1, height = 10, width = 25, font=("League Spartan",25),fg="white").place(x=240,y=100)
                # inputtxt.insert(Tk.END, "THANKYOU")

                n1 = tkinter.Label(w1, text="THANKYOU " + username + "  FOR ORDERING FROM US!",
                                   font=("Lexend Deca", 30), fg="White", bg="#5E17EB").place(x=280, y=150)

                n1 = tkinter.Label(w1, text="YOUR ORDER DETAILS", font=("League Spartan", 25), fg="#FFF500",
                                   bg="#5E17EB").place(x=420, y=230)
                n1 = tkinter.Label(w1, text="FOOD ITEMS BOOKED" + mos, font=("League Spartan", 25), fg="#5E17EB",
                                   bg="white").place(x=310, y=280)
                n1 = tkinter.Label(w1, text="TOTAL PRICE:" + str(tot), font=("Lexend Deca", 25), fg="#FF1616",
                                   bg="white").place(x=820, y=280)
                pay = tkinter.Button(w1, text="ENTER MY ADDRESS", command=address, font=("Lexend Deca", 25), fg="black",
                                     bg="#9EFF00").place(x=470, y=540)

            def showsum():
                cart_items = tkinter.Label(chandu_window, text="ITEMS IN CART =" + str(len(cart)) + "!",
                                           font=("League Spartan", 23), fg="dark blue", bg="white").place(x=200, y=520)
                cart_price = tkinter.Label(chandu_window, text="TOTAL = ???" + str(tot) + "!",
                                           font=("League Spartan", 23), fg="dark blue", bg="white").place(x=600, y=520)
                con = tkinter.Button(chandu_window, text="CONFIRM", command=ord_fin, font=("League Spartan", 23),
                                     fg="black", bg="gold").place(x=600, y=580)

            cart = []
            price = []
            cartitems = cart

            def addtocart1():  # Adding Price and Items

                if i1.get() == 1:
                    cart.append("Chilli Panner Dry")
                    if e1.get().isnumeric():
                        n = int(e1.get())
                    else:
                        n = 1

                    cost = n * 90
                    price.append(cost)

                if i2.get() == 1:
                    cart.append("Veg Kebab")
                    if e2.get().isnumeric():
                        n = int(e2.get())
                    else:
                        n = 1
                    cost = n * 70
                    price.append(cost)

                if i3.get() == 1:
                    cart.append("Panner Manchurian Dry")
                    if e3.get().isnumeric():
                        n = int(e3.get())
                    else:
                        n = 1

                    cost = n * 95
                    price.append(cost)
                if i4.get() == 1:
                    cart.append("Schezwan Chowmein")
                    if e4.get().isnumeric():
                        n = int(e4.get())
                    else:
                        n = 1
                    cost = n * 110
                    price.append(cost)

                if i5.get() == 1:
                    cart.append("Honey Chilli Potato")
                    if e5.get().isnumeric():
                        n = int(e5.get())
                    else:
                        n = 1
                    cost = n * 80
                    price.append(cost)

                global tot
                tot = 0
                tot = sum(price)
                cartitems = cart

            window_main.destroy()
            chandu_window = tkinter.Tk()
            chandu_window.geometry("1280x720")
            chandu_window.title("The Spice Route")
            woww = Image.open("wow.png")
            render = ImageTk.PhotoImage(woww)
            img = tkinter.Label(image=render)
            img.image = render
            img.place(x=0, y=0)
            chandu = tkinter.Label(chandu_window, text="   MENU   ", font=("League Spartan", 30), fg="deep sky blue",
                                   bg="white")
            headch = tkinter.Label(chandu_window, text="   MENU   ", font=("League Spartan", 30), fg="deep sky blue",
                                   bg="white")
            headch.place(x=630, y=5)

            i1 = tkinter.IntVar()  # For checkbutton : choice of
            i2 = tkinter.IntVar()  # For checkbutton : choice of
            i3 = tkinter.IntVar()
            i4 = tkinter.IntVar()
            i5 = tkinter.IntVar()
            e1 = tkinter.StringVar()
            e2 = tkinter.StringVar()
            e3 = tkinter.StringVar()
            e4 = tkinter.StringVar()
            e5 = tkinter.StringVar()

            py1 = tkinter.Radiobutton(chandu_window, text='CHILLI PANNER DRY : ???90', variable=i1, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=100)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=100)
            nu = tkinter.Entry(chandu_window, textvariable=e1, width=2, font=("League Spartan", 20), fg="red",
                               bg="white").place(x=830, y=100)

            py2 = tkinter.Radiobutton(chandu_window, text='VEG KEBAB : ???70', variable=i2, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=160)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=160)
            nu2 = tkinter.Entry(chandu_window, textvariable=e2, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=160)

            py3 = tkinter.Radiobutton(chandu_window, text='PANNER MANCHURIAN : ???95', variable=i3, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=220)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=220)
            nu3 = tkinter.Entry(chandu_window, textvariable=e3, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=220)

            py1 = tkinter.Radiobutton(chandu_window, text='SCHEZWAN CHOWMEIN : ???110', variable=i4, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=280)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=280)
            nu4 = tkinter.Entry(chandu_window, textvariable=e4, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=280)

            py1 = tkinter.Radiobutton(chandu_window, text='HONEY CHILLI POTATO : ???80', variable=i5, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=340)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=340)
            nu5 = tkinter.Entry(chandu_window, textvariable=e5, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=340)

            b1 = tkinter.Button(chandu_window, text="ADD TO CART", command=addtocart1, font=("League Spartan", 23),
                                fg="WHITE", bg="PURPLE").place(x=200, y=450)

            re = tkinter.Button(chandu_window, text="DONE", command=showsum, font=("League Spartan", 23), fg="black",
                                bg="lawn green").place(x=700, y=450)

        def shyam_menu():
            def ord_fin():
                mos = ''
                for jd in range(0, len(cart)):
                    mos = mos + "\n" + str(cartitems[jd])
                shyam_window.destroy()
                global w1
                w1 = tkinter.Tk()
                w1.title("ORDER DETAILS")
                w1.geometry("1280x720")
                w1.configure(bg="deep sky blue")

                thnxpic = Image.open("thnx.png")
                render = ImageTk.PhotoImage(thnxpic)
                img = tkinter.Label(image=render)
                img.image = render
                img.place(x=0, y=0)

                n1 = tkinter.Label(w1, text="THANKYOU " + username + "  FOR ORDERING FROM US!",
                                   font=("Lexend Deca", 30), fg="White", bg="#5E17EB").place(x=280, y=150)

                n1 = tkinter.Label(w1, text="YOUR ORDER DETAILS", font=("League Spartan", 25), fg="#FFF500",
                                   bg="#5E17EB").place(x=420, y=230)
                n1 = tkinter.Label(w1, text="FOOD ITEMS BOOKED" + mos, font=("League Spartan", 25), fg="#5E17EB",
                                   bg="white").place(x=310, y=280)
                n1 = tkinter.Label(w1, text="TOTAL PRICE:" + str(tot), font=("Lexend Deca", 25), fg="#FF1616",
                                   bg="white").place(x=820, y=280)
                pay = tkinter.Button(w1, text="ENTER MY ADDRESS", command=address, font=("Lexend Deca", 25), fg="black",
                                     bg="#9EFF00").place(x=470, y=540)

            def addtocart2():

                if i1.get() == 1:
                    cart.append("Spring Fling Pizza")
                    if e1.get().isnumeric():
                        n = int(e1.get())
                    else:
                        n = 1

                    cost = n * 90
                    price.append(cost)

                if i2.get() == 1:
                    cart.append("Cheese Panner Burger")
                    if e2.get().isnumeric():
                        n = int(e2.get())
                    else:
                        n = 1
                    cost = n * 70
                    price.append(cost)

                if i3.get() == 1:
                    cart.append("Cheese Nachos")
                    if e3.get().isnumeric():
                        n = int(e3.get())
                    else:
                        n = 1

                    cost = n * 95
                    price.append(cost)
                if i4.get() == 1:
                    cart.append("Mexican Fries")
                    if e4.get().isnumeric():
                        n = int(e4.get())
                    else:
                        n = 1
                    cost = n * 110
                    price.append(cost)

                if i5.get() == 1:
                    cart.append("Grilled Sandwich")
                    if e5.get().isnumeric():
                        n = int(e5.get())
                    else:
                        n = 1
                    cost = n * 80
                    price.append(cost)

                global tot
                tot = 0
                tot = sum(price)
                cartitems = cart

            def showsum():
                cart_items = tkinter.Label(shyam_window, text="ITEMS IN CART =" + str(len(cart)) + "!",
                                           font=("League Spartan", 23), fg="dark blue", bg="white").place(x=200, y=520)
                cart_price = tkinter.Label(shyam_window, text="TOTAL = ???" + str(tot) + "!", font=("League Spartan", 23),
                                           fg="dark blue", bg="white").place(x=600, y=520)
                con = tkinter.Button(shyam_window, text="CONFIRM", command=ord_fin, font=("League Spartan", 23),
                                     fg="black", bg="gold").place(x=600, y=580)

            cart = []
            price = []
            cartitems = cart

            window_main.destroy()

            shyam_window = tkinter.Tk()
            shyam_window.geometry("1280x720")
            shyam_window.title("Paterro???s Kitchen")
            woww = Image.open("wow.png")
            render = ImageTk.PhotoImage(woww)
            img = tkinter.Label(image=render)
            img.image = render
            img.place(x=0, y=0)
            headch = tkinter.Label(shyam_window, text="   MENU   ", font=("League Spartan", 30), fg="deep sky blue",
                                   bg="white")
            headch.place(x=520, y=0)

            i1 = tkinter.IntVar()  # For checkbutton : choice of
            i2 = tkinter.IntVar()  # For checkbutton : choice of
            i3 = tkinter.IntVar()
            i4 = tkinter.IntVar()
            i5 = tkinter.IntVar()
            e1 = tkinter.StringVar()
            e2 = tkinter.StringVar()
            e3 = tkinter.StringVar()
            e4 = tkinter.StringVar()
            e5 = tkinter.StringVar()

            py1 = tkinter.Radiobutton(shyam_window, text='SPRING FLING PIZZA : ???90', variable=i1, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=100)
            nu1 = tkinter.Label(shyam_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=100)
            nu = tkinter.Entry(shyam_window, textvariable=e1, width=2, font=("League Spartan", 20), fg="red",
                               bg="white").place(x=830, y=100)

            py2 = tkinter.Radiobutton(shyam_window, text='CHEESE PANNER BURGER : ???70', variable=i2, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=160)
            nu1 = tkinter.Label(shyam_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=160)
            nu2 = tkinter.Entry(shyam_window, textvariable=e2, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=160)

            py3 = tkinter.Radiobutton(shyam_window, text='CHEESE NACHOS : ???95', variable=i3, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=220)
            nu1 = tkinter.Label(shyam_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=220)
            nu3 = tkinter.Entry(shyam_window, textvariable=e3, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=220)

            py1 = tkinter.Radiobutton(shyam_window, text='MEXICAN FRIES : ???110', variable=i4, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=280)
            nu1 = tkinter.Label(shyam_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=280)
            nu4 = tkinter.Entry(shyam_window, textvariable=e4, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=280)

            py1 = tkinter.Radiobutton(shyam_window, text='GRILLED SANDWICH : ???80', variable=i5, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=340)
            nu1 = tkinter.Label(shyam_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=340)
            nu5 = tkinter.Entry(shyam_window, textvariable=e5, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=340)

            b1 = tkinter.Button(shyam_window, text="ADD TO CART", command=addtocart2, font=("League Spartan", 23),
                                fg="WHITE", bg="PURPLE").place(x=200, y=450)

            re = tkinter.Button(shyam_window, text="DONE", command=showsum, font=("League Spartan", 23), fg="black",
                                bg="lawn green").place(x=700, y=450)

        def mukesh_menu():  # Adding Items from The Spice Route to Cart
            def ord_fin():
                mos = ''
                for jd in range(0, len(cart)):
                    mos = mos + "\n" + str(cartitems[jd])
                chandu_window.destroy()
                global w1
                w1 = tkinter.Tk()
                w1.title("ORDER DETAILS")
                w1.geometry("1280x720")
                w1.configure(bg="deep sky blue")

                thnxpic = Image.open("thnx.png")
                render = ImageTk.PhotoImage(thnxpic)
                img = tkinter.Label(image=render)
                img.image = render
                img.place(x=0, y=0)

                n1 = tkinter.Label(w1, text="THANKYOU " + username + "  FOR ORDERING FROM US!",
                                   font=("Lexend Deca", 30), fg="White", bg="#5E17EB").place(x=280, y=150)

                n1 = tkinter.Label(w1, text="YOUR ORDER DETAILS", font=("League Spartan", 25), fg="#FFF500",
                                   bg="#5E17EB").place(x=420, y=230)
                n1 = tkinter.Label(w1, text="FOOD ITEMS BOOKED" + mos, font=("League Spartan", 25), fg="#5E17EB",
                                   bg="white").place(x=310, y=280)
                n1 = tkinter.Label(w1, text="TOTAL PRICE:" + str(tot), font=("Lexend Deca", 25), fg="#FF1616",
                                   bg="white").place(x=820, y=280)
                pay = tkinter.Button(w1, text="ENTER MY ADDRESS", command=address, font=("Lexend Deca", 25), fg="black",
                                     bg="#9EFF00").place(x=470, y=540)

            def showsum():
                cart_items = tkinter.Label(chandu_window, text="ITEMS IN CART =" + str(len(cart)) + "!",
                                           font=("League Spartan", 23), fg="dark blue", bg="white").place(x=200, y=520)
                cart_price = tkinter.Label(chandu_window, text="TOTAL = ???" + str(tot) + "!",
                                           font=("League Spartan", 23), fg="dark blue", bg="white").place(x=600, y=520)
                con = tkinter.Button(chandu_window, text="CONFIRM", command=ord_fin, font=("League Spartan", 23),
                                     fg="black", bg="gold").place(x=600, y=580)

            cart = []
            price = []
            cartitems = cart

            def addtocart1():  # Adding Price and Items

                if i1.get() == 1:
                    cart.append("Chilli Panner Dry")
                    if e1.get().isnumeric():
                        n = int(e1.get())
                    else:
                        n = 1

                    cost = n * 90
                    price.append(cost)

                if i2.get() == 1:
                    cart.append("Veg Kebab")
                    if e2.get().isnumeric():
                        n = int(e2.get())
                    else:
                        n = 1
                    cost = n * 70
                    price.append(cost)

                if i3.get() == 1:
                    cart.append("Panner Manchurian Dry")
                    if e3.get().isnumeric():
                        n = int(e3.get())
                    else:
                        n = 1

                    cost = n * 95
                    price.append(cost)
                if i4.get() == 1:
                    cart.append("Schezwan Chowmein")
                    if e4.get().isnumeric():
                        n = int(e4.get())
                    else:
                        n = 1
                    cost = n * 110
                    price.append(cost)

                if i5.get() == 1:
                    cart.append("Honey Chilli Potato")
                    if e5.get().isnumeric():
                        n = int(e5.get())
                    else:
                        n = 1
                    cost = n * 80
                    price.append(cost)

                global tot
                tot = 0
                tot = sum(price)
                cartitems = cart

            window_main.destroy()
            chandu_window = tkinter.Tk()
            chandu_window.geometry("1280x720")
            chandu_window.title("The Spice Route")
            woww = Image.open("wow.png")
            render = ImageTk.PhotoImage(woww)
            img = tkinter.Label(image=render)
            img.image = render
            img.place(x=0, y=0)
            headch = tkinter.Label(chandu_window, text="   MENU   ", font=("League Spartan", 30), fg="deep sky blue",
                                   bg="white")
            headch.place(x=630, y=5)

            i1 = tkinter.IntVar()  # For checkbutton : choice of
            i2 = tkinter.IntVar()  # For checkbutton : choice of
            i3 = tkinter.IntVar()
            i4 = tkinter.IntVar()
            i5 = tkinter.IntVar()
            e1 = tkinter.StringVar()
            e2 = tkinter.StringVar()
            e3 = tkinter.StringVar()
            e4 = tkinter.StringVar()
            e5 = tkinter.StringVar()

            py1 = tkinter.Radiobutton(chandu_window, text='CHILLI PANNER DRY : ???90', variable=i1, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=100)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=100)
            nu = tkinter.Entry(chandu_window, textvariable=e1, width=2, font=("League Spartan", 20), fg="red",
                               bg="white").place(x=830, y=100)

            py2 = tkinter.Radiobutton(chandu_window, text='VEG KEBAB : ???70', variable=i2, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=160)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=160)
            nu2 = tkinter.Entry(chandu_window, textvariable=e2, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=160)

            py3 = tkinter.Radiobutton(chandu_window, text='PANNER MANCHURIAN : ???95', variable=i3, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=220)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=220)
            nu3 = tkinter.Entry(chandu_window, textvariable=e3, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=220)

            py1 = tkinter.Radiobutton(chandu_window, text='SCHEZWAN CHOWMEIN : ???110', variable=i4, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=280)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=280)
            nu4 = tkinter.Entry(chandu_window, textvariable=e4, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=280)

            py1 = tkinter.Radiobutton(chandu_window, text='HONEY CHILLI POTATO : ???80', variable=i5, value=1,
                                      font=("Raleway Black", 20), fg="white", bg="black").place(x=200, y=340)
            nu1 = tkinter.Label(chandu_window, text="Quantity", font=("Raleway Black", 20), fg="White", bg="RED").place(
                x=700, y=340)
            nu5 = tkinter.Entry(chandu_window, textvariable=e5, width=2, font=("League Spartan", 20), fg="red",
                                bg="white").place(x=830, y=340)

            b1 = tkinter.Button(chandu_window, text="ADD TO CART", command=addtocart1, font=("League Spartan", 23),
                                fg="WHITE", bg="PURPLE").place(x=200, y=450)

            re = tkinter.Button(chandu_window, text="DONE", command=showsum, font=("League Spartan", 23), fg="black",
                                bg="lawn green").place(x=700, y=450)

        def flow1(i):
            if city.index(i) % 2 == 0:

                # The Spice Route
                chandu = tkinter.Label(window_main, text=" THE SPICE ROUTE ", font=("Raleway Black", 27), fg="White",
                                       bg="Violet")
                chandu.place(x=40, y=250)
                # Price
                chandu_s = tkinter.Label(window_main, text="Price For Two - ???200", font=("League Spartan", 25),
                                         fg="dark blue", bg="white")
                chandu_s.place(x=40, y=315)
                # Order
                buychandu = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                           bg="Orange", command=chandu_menu)
                buychandu.place(x=40, y=370)

                # The Imperial Spice
                imperial = tkinter.Label(window_main, text=" THE IMPERIAL SPICE ", font=("Raleway Black", 27),
                                         fg="White", bg="Violet")
                imperial.place(x=40, y=500)
                # Price
                imperial_s = tkinter.Label(window_main, text="Price For Two - ???210", font=("League Spartan", 25),
                                           fg="dark blue", bg="white")
                imperial_s.place(x=40, y=565)
                # Order
                imperialchandu = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25),
                                                fg="Black", bg="Orange", command=shyam_menu)
                imperialchandu.place(x=40, y=620)

                # Paterro???s Kitchen

                shyam = tkinter.Label(window_main, text=" PATERRO'S KITCHEN ", font=("Raleway Black", 27), fg="White",
                                      bg="Violet")
                shyam.place(x=450, y=250)
                # Price
                shyam_s = tkinter.Label(window_main, text="Price For Two - ???190", font=("League Spartan", 25),
                                        fg="dark blue", bg="white")
                shyam_s.place(x=450, y=315)
                # Order
                buyshyam = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                          bg="Orange", command=shyam_menu)
                buyshyam.place(x=450, y=370)

                # South King Spice
                sk = tkinter.Label(window_main, text=" SOUTH KING SPICE ", font=("Raleway Black", 27), fg="White",
                                   bg="Violet")
                sk.place(x=450, y=500)
                # Price
                sk_s = tkinter.Label(window_main, text="Price For Two - ???250", font=("League Spartan", 25),
                                     fg="dark blue", bg="white")
                sk_s.place(x=450, y=565)
                # Order
                buysk = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                       bg="Orange", command=chandu_menu)
                buysk.place(x=450, y=620)

                # Shalimar Restaurant
                mukesh = tkinter.Label(window_main, text=" SHALIMAR RESTAURANT ", font=("Raleway Black", 27),
                                       fg="White", bg="Violet")
                mukesh.place(x=900, y=250)
                # Price
                mukesh_s = tkinter.Label(window_main, text="Price For Two - ???170", font=("League Spartan", 25),
                                         fg="dark blue", bg="white")
                mukesh_s.place(x=900, y=315)
                # Order
                buymukesh = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                           bg="Orange", command=mukesh_menu)
                buymukesh.place(x=900, y=370)

                # Megu Restaurant
                meg = tkinter.Label(window_main, text=" MEGU RESTAURANT ", font=("Raleway Black", 27), fg="White",
                                    bg="Violet")
                meg.place(x=900, y=500)
                # Price
                meg_s = tkinter.Label(window_main, text="Price For Two - ???260", font=("League Spartan", 25),
                                      fg="dark blue", bg="white")
                meg_s.place(x=900, y=565)
                # Order
                buymeg = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                        bg="Orange", command=shyam_menu)
                buymeg.place(x=900, y=620)

            else:

                # Califo Pizzeria
                sharma = tkinter.Label(window_main, text=" CALIFO PIZZERIA ", font=("Raleway Black", 27), fg="White",
                                       bg="Violet")
                sharma.place(x=40, y=250)
                # Price
                sharma_s = tkinter.Label(window_main, text="Price For Two - ???240", font=("League Spartan", 25),
                                         fg="dark blue", bg="white")
                sharma_s.place(x=40, y=315)
                # Order
                buysharma = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                           bg="Orange", command=chandu_menu)
                buysharma.place(x=40, y=370)

                # Magic Wheels
                mgw = tkinter.Label(window_main, text=" MAGIC WHEELS ", font=("Raleway Black", 27), fg="White",
                                    bg="Violet")
                mgw.place(x=40, y=500)
                # Price
                mgw_s = tkinter.Label(window_main, text="Price For Two - ???210", font=("League Spartan", 25),
                                      fg="dark blue", bg="white")
                mgw_s.place(x=40, y=565)
                # Order
                mgw = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                     bg="Orange", command=shyam_menu)
                mgw.place(x=40, y=620)

                # Indian Star Hut
                binod = tkinter.Label(window_main, text=" INDIAN STAR HUT ", font=("Raleway Black", 27), fg="White",
                                      bg="Violet")
                binod.place(x=450, y=250)
                # Price
                binod_s = tkinter.Label(window_main, text="Price For Two - ???190", font=("League Spartan", 25),
                                        fg="dark blue", bg="white")
                binod_s.place(x=450, y=315)
                # Order
                buybinod = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                          bg="Orange", command=shyam_menu)
                buybinod.place(x=450, y=370)

                # Meal Cage
                cage = tkinter.Label(window_main, text=" MEAL CAGE ", font=("Raleway Black", 27), fg="White",
                                     bg="Violet")
                cage.place(x=450, y=500)
                # Price
                cage_s = tkinter.Label(window_main, text="Price For Two - ???250", font=("League Spartan", 25),
                                       fg="dark blue", bg="white")
                cage_s.place(x=450, y=565)
                # Order
                buycage = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                         bg="Orange", command=chandu_menu)
                buycage.place(x=450, y=620)

                # Moti Mahal
                bablu = tkinter.Label(window_main, text=" MOTI MAHAL  ", font=("Raleway Black", 27), fg="White",
                                      bg="Violet")
                bablu.place(x=900, y=250)
                # Price
                bablu_s = tkinter.Label(window_main, text="Price For Two - ???160", font=("League Spartan", 25),
                                        fg="dark blue", bg="white")
                bablu_s.place(x=900, y=315)
                # Order
                buybablu = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                          bg="Orange", command=shyam_menu)
                buybablu.place(x=900, y=370)

                # Bangalore Spices
                bs = tkinter.Label(window_main, text=" BANGALORE SPICES ", font=("Raleway Black", 27), fg="White",
                                   bg="Violet")
                bs.place(x=900, y=500)
                # Price
                bs_s = tkinter.Label(window_main, text="Price For Two - ???220", font=("League Spartan", 25),
                                     fg="dark blue", bg="white")
                bs_s.place(x=900, y=565)
                # Order
                buybs = tkinter.Button(window_main, text=" ORDER NOW ", font=("League Spartan", 25), fg="Black",
                                       bg="Orange", command=chandu_menu)
                buybs.place(x=900, y=620)

        loca = tkinter.Label(window_main, text=" SELECT YOUR CITY ", font=("Raleway Black", 25), fg="white", bg="green")
        loca.place(x=309, y=130)
        i = tkinter.StringVar()
        city = ["Mumbai", "Jaipur", "Bangalore", "Chennai", "Hyderabad", "Kolkata", "Agra", "Varanasi", "Pune", "Kochi",
                "Udaipur", "Ahmedabad", "New Delhi", "Lucknow", "Chandigarh", "Amritsar", "Jodhpur", "Kanpur", "Mysore",
                "Surat", "Gurugram", "Shimla", "Indore", "Manali", "Nashik"]
        city.sort()
        i.set("CITY")
        Menu_l = tkinter.OptionMenu(window_main, i, *city, command=flow1)
        Menu_l.configure(font=("Raleway Black", 22), bg="DEEP SKY BLUE", fg="white", activebackground="WHITE")
        Menu_l.place(x=730, y=130)

    def payment():
        def cod():
            try:
                p1.destroy()
            except:
                pass
            p2 = tkinter.Tk()
            p2.title("COD Payment Mode")
            p2.geometry("1140x759")
            p2.configure(bg="slateblue1")
            load = Image.open("a5.jpg")
            render = ImageTk.PhotoImage(load)
            img = tkinter.Label(image=render)
            img.image = render
            img.place(x=0, y=0)
            l3 = tkinter.Label(p2, text="Thankyou For Choosing Our Service!", bg="#347893", fg="white",
                               font=("League Spartan", 25))
            l3.place(x=290, y=100)
            add = tkinter.Label(p2, text="Your Food Will Be Delivered In Next 30 Minutes", fg="WHITE", bg="#347893",
                                font=("Raleway Black", 20)).place(x=290, y=200)
            n1 = tkinter.Label(p2, text="ORDERED BY     " + fullname + " !", fg="WHITE", bg="#347893",
                               font=("League Spartan", 19)).place(x=300, y=300)
            n2 = tkinter.Label(p2, text="ADDRESS LINE 1 -    " + addressline1 + "", fg="WHITE", bg="#347893",
                               font=("League Spartan", 19)).place(x=300, y=350)
            n3 = tkinter.Label(p2, text="ADDRESS LINE 2 -   " + addressline2 + "", fg="WHITE", bg="#347893",
                               font=("League Spartan", 19)).place(x=300, y=400)
            n4 = tkinter.Label(p2, text="CITY -  " + city + "", fg="WHITE", bg="#347893",
                               font=("League Spartan", 19)).place(x=300, y=450)
            n5 = tkinter.Label(p2, text="PINCODE -    " + pincode + "", fg="WHITE", bg="#347893",
                               font=("League Spartan", 19)).place(x=580, y=450)
            n6 = tkinter.Label(p2, text="PHONE NUMBER -   " + "+91" + phonenum + "", bg="#347893", fg="WHITE",
                               font=("League Spartan", 19)).place(x=300, y=500)
            n7 = tkinter.Label(p2, text="YOURS FoodJets", fg="white", bg="#347893", font=("League Spartan", 21)).place(
                x=400, y=570)

        def cdc():
            def cdc2():
                def cdc3():
                    p3.destroy()
                    cdc2()  # cdc3 func. over

                def resend():
                    po.destroy()
                    cdc2()

                def quick():
                    def quick2():
                        def checkcvv2():
                            p4.destroy()
                            quick2()

                        def back():
                            p4.destroy()
                            cdc2()

                        def checkcvv():
                            if e5.get() == q:
                                p4.destroy()
                                cod()
                            else:
                                l1 = tkinter.Label(p4, text="*TRANSACTION COULD NOT BE COMPLETED DUE TO WRONG CVV*",
                                                   bg="#347893", fg="black", font=("League Spartan", 20))
                                l1.place(x=100, y=510)
                                l2 = tkinter.Label(p4, text="PLEASE MAKE CHANGES IN ABOVE SECTION", bg="#347893",
                                                   fg="white", font=("League Spartan", 17))
                                l2.place(x=300, y=560)
                                l2 = tkinter.Label(p4, text="OR ELSE HERE TO ENTER AGAIN", bg="#347893",
                                                   font=("League Spartan", 17))
                                l2.place(x=350, y=600)
                                b5 = tkinter.Button(p4, text="TRY AGAIN", font=("League Spartan", 20), bg="red",
                                                    fg="white", command=checkcvv2)
                                b5.place(x=440, y=650)

                        p4 = tkinter.Tk()
                        p4.title(" Quick Credit/Debit Card Payment Mode")
                        p4.geometry("1140x759")
                        p4.configure(bg="#347893")
                        load = Image.open("a2.jpg")
                        render = ImageTk.PhotoImage(load)
                        img = tkinter.Label(image=render)
                        img.image = render
                        img.place(x=0, y=0)
                        l = tkinter.Label(p4, text="WELCOME TO QUICK PAYMENT MODE", bg="#347893", fg="white",
                                          font=("League Spartan", 25))
                        l.place(x=250, y=80)

                        s = sq.connect(host="localhost", user="root", passwd="shubh", database="project")
                        cursor1 = s.cursor()
                        cursor1.execute("select*from user")
                        data = cursor1.fetchall()
                        l = []
                        for i in data:
                            l.append(i)
                        cursor1.close()
                        s.close()
                        for j in l:
                            if j[0] == username:
                                m = j[2]
                                n = j[3]
                                o = j[4]
                                p = j[5]
                                global q
                                q = j[6]
                                break
                        l1 = tkinter.Label(p4, text="ENTER CARD NO.", bg="#347893", fg="black",
                                           font=("League Spartan", 19))
                        l1.place(x=230, y=180)
                        m1 = tkinter.Label(p4, text="(16 DIGIT NO.)", bg="#347893", fg="yellow",
                                           font=("League Spartan", 8))
                        m1.place(x=230, y=215)
                        e1 = tkinter.Label(p4, text=m, width=16, font=("League Spartan", 17), bg="white", fg="red")
                        e1.place(x=600, y=180)

                        l2 = tkinter.Label(p4, text="ENTER NAME ON CARD", bg="#347893", fg="black",
                                           font=("League Spartan", 19))
                        l2.place(x=230, y=250)
                        e2 = tkinter.Label(p4, text=n, width=30, font=("League Spartan", 17), bg="white", fg="black")
                        e2.place(x=600, y=250)

                        l3 = tkinter.Label(p4, text="EXPIRY MONTH", bg="#347893", fg="black",
                                           font=("League Spartan", 19))
                        l3.place(x=230, y=320)
                        m3 = tkinter.Label(p4, text="(1/2  DIGIT NO.)", bg="#347893", fg="yellow",
                                           font=("League Spartan", 8))
                        m3.place(x=230, y=355)
                        e3 = tkinter.Label(p4, text=o, width=2, font=("League Spartan", 17), bg="white", fg="black")
                        e3.place(x=460, y=320)

                        l4 = tkinter.Label(p4, text="EXPIRY YEAR", bg="#347893", fg="black",
                                           font=("League Spartan", 19))
                        l4.place(x=600, y=320)
                        m4 = tkinter.Label(p4, text="(FROM 2021 TO 2050)", bg="#347893", fg="yellow",
                                           font=("League Spartan", 8))
                        m4.place(x=600, y=355)
                        e4 = tkinter.Label(p4, text=p, width=4, font=("League Spartan", 17), bg="white", fg="black")
                        e4.place(x=820, y=320)

                        l5 = tkinter.Label(p4, text="CVV", bg="#347893", fg="black", font=("League Spartan", 19))
                        l5.place(x=230, y=390)
                        m5 = tkinter.Label(p4, text="(3 DIGIT NO.)", bg="#347893", fg="yellow",
                                           font=("League Spartan", 8))
                        m5.place(x=230, y=425)
                        e5 = tkinter.Entry(p4, width=3, font=("League Spartan", 17), bg="white", fg="black", show="*")
                        e5.place(x=460, y=390)

                        b3 = tkinter.Button(p4, text="SUBMIT", font=("League Spartan", 20), bg="red", fg="white",
                                            command=checkcvv)
                        b3.place(x=350, y=450)
                        b4 = tkinter.Button(p4, text="BACK", font=("League Spartan", 20), bg="red", fg="white",
                                            command=back)
                        b4.place(x=620, y=450)

                    s = sq.connect(host="localhost", user="root", passwd="shubh", database="project")
                    cursor1 = s.cursor()
                    cursor1.execute("select*from user")
                    data = cursor1.fetchall()
                    l = []
                    for i in data:
                        l.append(i)
                    cursor1.close()
                    s.close()
                    for j in l:
                        if j[0] == username:
                            if str(j[3]) == "None":
                                p3.destroy()
                                global po
                                po = tkinter.Tk()
                                po.title("Failed")
                                po.geometry("1140x759")
                                po.configure(bg="#347893")
                                load = Image.open("a3.jpg")
                                render = ImageTk.PhotoImage(load)
                                img = tkinter.Label(image=render)
                                img.image = render
                                img.place(x=0, y=0)
                                l = tkinter.Label(po, text="NO PRE-RECORDED DATA FOUND", fg="white", bg="#347893",
                                                  font=("League Spartan", 28))
                                l.place(x=250, y=200)
                                l1 = tkinter.Label(po, text="YOU WOULD NEED TO ENTER THE REQUIRED CREDENTIALS",
                                                   fg="white", bg="#347893", font=("League Spartan", 20))
                                l1.place(x=150, y=270)
                                b1 = tkinter.Button(po, text="CLICK", font=("League Spartan", 20), bg="red", fg="white",
                                                    command=resend)
                                b1.place(x=520, y=450)

                            else:
                                p3.destroy()
                                quick2()

                def submit2():
                    if e1.get().isdigit() and e2.get().replace(" ",
                                                               "").isalpha() and e3.get().isdigit() and e4.get().isdigit() and e5.get().isdigit() and len(
                            e1.get()) == 16 and int(e3.get()) > 0 and int(e3.get()) < 13 and int(
                            e4.get()) > 2020 and int(e4.get()) < 2050 and len(e5.get()) == 3:
                        l1 = []
                        m = e1.get()
                        n = e2.get()
                        o = e3.get()
                        p = e4.get()
                        q = e5.get()
                        l1.append(m)
                        l1.append(n)
                        l1.append(o)
                        l1.append(p)
                        l1.append(q)
                        l1.append(username)
                        u = tuple(l1)
                        s = sq.connect(host="localhost", user="root", passwd="shubh", database="project")
                        cursor1 = s.cursor()
                        insert_query = """update user
                                          SET card_no= %s, name_on_card= %s, expiry_month= %s, expiry_year= %s, cvv=%s where username=%s"""

                        cursor1.execute(insert_query, u)
                        s.commit()
                        cursor1.close
                        s.close
                        p3.destroy()
                        cod()
                    else:
                        l1 = tkinter.Label(p3, text="*TRANSACTION COULD NOT BE COMPLETED DUE TO SOME REASONS*",
                                           bg="#347893", fg="black", font=("League Spartan", 20))
                        l1.place(x=100, y=510)
                        l2 = tkinter.Label(p3, text="PLEASE MAKE CHANGES IN ABOVE SECTION", bg="#347893", fg="white",
                                           font=("League Spartan", 17))
                        l2.place(x=300, y=560)
                        l2 = tkinter.Label(p3, text="OR ELSE HERE TO ENTER AGAIN", bg="#347893",
                                           font=("League Spartan", 17))
                        l2.place(x=355, y=600)
                        b5 = tkinter.Button(p3, text="TRY AGAIN", font=("League Spartan", 20), bg="red", fg="white",
                                            command=cdc3)
                        b5.place(x=440, y=650)  # submit2 func. over

                p3 = tkinter.Tk()
                p3.title("Credit/Debit Card Payment Mode")
                p3.geometry("1140x759")
                p3.configure(bg="#347893")
                load = Image.open("a2.jpg")
                render = ImageTk.PhotoImage(load)
                img = tkinter.Label(image=render)
                img.image = render
                img.place(x=0, y=0)
                l = tkinter.Label(p3, text="PLEASE ENTER THE REQUIRED DETAILS", fg="white", bg="#347893",
                                  font=("League Spartan", 28))
                l.place(x=230, y=80)

                l1 = tkinter.Label(p3, text="ENTER CARD NO.", bg="#347893", fg="black", font=("League Spartan", 19))
                l1.place(x=230, y=180)
                m1 = tkinter.Label(p3, text="(16 DIGIT NO.)", bg="#347893", fg="yellow", font=("League Spartan", 8))
                m1.place(x=230, y=215)
                e1 = tkinter.Entry(p3, width=16, font=("League Spartan", 17), bg="white", fg="red")
                e1.place(x=600, y=180)

                l2 = tkinter.Label(p3, text="ENTER NAME ON CARD", bg="#347893", fg="black", font=("League Spartan", 19))
                l2.place(x=230, y=250)
                e2 = tkinter.Entry(p3, width=30, font=("League Spartan", 17), bg="white", fg="black")
                e2.place(x=600, y=250)

                l3 = tkinter.Label(p3, text="EXPIRY MONTH", bg="#347893", fg="black", font=("League Spartan", 19))
                l3.place(x=230, y=320)
                m3 = tkinter.Label(p3, text="(1/2  DIGIT NO.)", bg="#347893", fg="yellow", font=("League Spartan", 8))
                m3.place(x=230, y=355)
                e3 = tkinter.Entry(p3, width=2, font=("League Spartan", 17), bg="white", fg="black")
                e3.place(x=460, y=320)

                l4 = tkinter.Label(p3, text="EXPIRY YEAR", bg="#347893", fg="black", font=("League Spartan", 19))
                l4.place(x=600, y=320)
                m4 = tkinter.Label(p3, text="(FROM 2021 TO 2050)", bg="#347893", fg="yellow",
                                   font=("League Spartan", 8))
                m4.place(x=600, y=355)
                e4 = tkinter.Entry(p3, width=4, font=("League Spartan", 17), bg="white", fg="black")
                e4.place(x=820, y=320)

                l5 = tkinter.Label(p3, text="CVV", bg="#347893", fg="black", font=("League Spartan", 19))
                l5.place(x=230, y=390)
                m5 = tkinter.Label(p3, text="(3 DIGIT NO.)", bg="#347893", fg="yellow", font=("League Spartan", 8))
                m5.place(x=230, y=425)
                e5 = tkinter.Entry(p3, width=3, font=("League Spartan", 17), bg="white", fg="black", show="*")
                e5.place(x=460, y=390)

                b3 = tkinter.Button(p3, text="SUBMIT", font=("League Spartan", 20), bg="red", fg="white",
                                    command=submit2)
                b3.place(x=350, y=450)
                b4 = tkinter.Button(p3, text="QUICK", font=("League Spartan", 20), bg="red", fg="white", command=quick)
                b4.place(x=620, y=450)  # cdc2 func. over

            p1.destroy()
            cdc2()  # cdc func. over

        p1 = tkinter.Tk()
        p1.title("Mode for Payment")
        p1.geometry("1280x720")
        p1.configure(bg="#347893")
        load = Image.open("a1.jpg")
        render = ImageTk.PhotoImage(load)
        img = tkinter.Label(image=render)
        img.image = render
        img.place(x=0, y=0)
        l = tkinter.Label(p1, text="PLEASE SELECT MODE FOR PAYMENT", fg="black", bg="#347893",
                          font=("League Spartan", 28))
        l.place(x=200, y=250)
        l1 = tkinter.Button(p1, text="CASH ON DELIVERY", command=cod, bg="red", fg="white", font=("League Spartan", 17))
        l1.place(x=220, y=450)
        l2 = tkinter.Button(p1, text="CREDIT/DEBIT CARD", command=cdc, bg="red", fg="white",
                            font=("League Spartan", 17))
        l2.place(x=600, y=450)

    def applogin():
        def login():
            def check():
                global username
                username = e1.get()
                password = e2.get()
                s = sq.connect(host="localhost", user="root", passwd="shubh", database="project")
                cursor1 = s.cursor()
                cursor1.execute("select*from user")
                data = cursor1.fetchall()
                l = []
                for i in data:
                    l.append(i)
                cursor1.close()
                s.close()
                for j in l:
                    if j[0] == username and j[1] == password:
                        loginscr.destroy()
                        order()
                        break
                else:
                    l6 = tkinter.Label(loginscr, text="*No Account Found With This Data! Check Your Credentials*",
                                       fg="red", bg="#FF908E", font=("League Spartan", 20))
                    l6.place(x=300, y=510)
                    b5 = tkinter.Button(loginscr, text="SIGN UP", font=("League Spartan", 28), bg="green", fg="black",
                                        command=signup)
                    b5.place(x=519, y=590)

            welcome.destroy()
            global loginscr
            loginscr = tkinter.Tk()
            loginscr.title("Log In")
            loginscr.geometry("1140x759")
            loginscr.configure(bg="deep sky blue")
            load = Image.open("1.jpg")
            render = ImageTk.PhotoImage(load)
            img = tkinter.Label(image=render)
            img.image = render
            img.place(x=0, y=0)
            l1 = tkinter.Label(loginscr, text="USERNAME", font=("League Spartan", 30), fg="white", bg="#FF908E")
            l1.place(x=300, y=310)
            global e1
            e1 = tkinter.Entry(loginscr, width=33, font=("Raleway Black", 25), bg="white", fg="black")
            e1.place(x=300, y=360)
            l2 = tkinter.Label(loginscr, text="PASSWORD", font=("League Spartan", 30), fg="white", bg="#FF908E")
            l2.place(x=300, y=410)
            global e2
            e2 = tkinter.Entry(loginscr, width=33, font=("Raleway Black", 25), bg="white", fg="black", show="*")
            e2.place(x=300, y=470)
            b1 = tkinter.Button(loginscr, text="SUBMIT", font=("Raleway Black", 28), bg="orchid1", fg="black",
                                command=check)
            b1.place(x=520, y=540)

        def signup():
            def submit():
                global username
                username = e3.get()
                password = e4.get()
                s = sq.connect(host="localhost", user="root", passwd="shubh", database="project")
                cursor1 = s.cursor()
                cursor1.execute("select*from user")
                data = cursor1.fetchall()
                l = []
                for i in data:
                    l.append(i)
                cursor1.close()
                s.close()
                for j in l:
                    if j[0] == username:
                        # f1=tkinter.Frame(signup,width=500,height=100,bg='white')
                        # f1.place(x=0,y=200)
                        l5 = tkinter.Label(signup, text="*Account With This Username Already Exists*", fg="firebrick1",
                                           font=("Raleway Black", 20), bg="#FF908E")
                        l5.place(x=380, y=600)
                        break
                else:
                    l2 = []
                    l2.append(username)
                    l2.append(password)
                    t = tuple(l2)
                    s = sq.connect(host="localhost", user="root", passwd="shubh", database="project")
                    cursor1 = s.cursor()
                    insert_query = """insert into user (username, password)
                                        values (%s, %s) """

                    cursor1.execute(insert_query, t)
                    s.commit()
                    cursor1.close
                    s.close
                    signup.destroy()
                    order()

            try:
                welcome.destroy()
                signup = tkinter.Tk()
                signup.title("Sign Up")
                signup.geometry("1140x759")
                signup.configure(bg="deep sky blue")
                load = Image.open("1.jpg")
                render = ImageTk.PhotoImage(load)
                img = tkinter.Label(image=render)
                img.image = render
                img.place(x=0, y=0)
                l3 = tkinter.Label(signup, text="USERNAME", font=("League Spartan", 30), fg="white", bg="#FF908E")
                l3.place(x=300, y=320)
                e3 = tkinter.Entry(signup, width=33, font=("Raleway Black", 25), bg="white", fg="black")
                e3.place(x=300, y=370)
                l4 = tkinter.Label(signup, text="PASSWORD", font=("League Spartan", 30), fg="white", bg="#FF908E")
                l4.place(x=300, y=440)
                e4 = tkinter.Entry(signup, width=33, font=("Raleway Black", 25), bg="white", fg="black", show="*")
                e4.place(x=300, y=490)
                b4 = tkinter.Button(signup, text="SUBMIT", font=("Raleway Black", 28), command=submit, bg="orchid1",
                                    fg="black")
                b4.place(x=510, y=550)

            except:
                loginscr.destroy()
                signup = tkinter.Tk()
                signup.title("Sign Up")
                signup.geometry("1140x759")
                signup.configure(bg="deep sky blue")
                load = Image.open("1.jpg")
                render = ImageTk.PhotoImage(load)
                img = tkinter.Label(image=render)
                img.image = render
                img.place(x=0, y=0)
                l3 = tkinter.Label(signup, text="USERNAME", font=("League Spartan", 30), fg="white", bg="#FF908E")
                l3.place(x=300, y=320)
                e3 = tkinter.Entry(signup, width=33, font=("Raleway Black", 25), bg="white", fg="black")
                e3.place(x=300, y=370)
                l4 = tkinter.Label(signup, text="PASSWORD", font=("League Spartan", 30), fg="white", bg="#FF908E")
                l4.place(x=300, y=440)
                e4 = tkinter.Entry(signup, width=33, font=("Raleway Black", 25), bg="white", fg="black", show="*")
                e4.place(x=300, y=490)
                b4 = tkinter.Button(signup, text="SUBMIT", font=("Raleway Black", 28), command=submit, bg="orchid1",
                                    fg="black")
                b4.place(x=510, y=550)

        welcome = tkinter.Tk()
        welcome.title("Welcome To The Login Page")
        welcome.geometry("1144x759")
        welcome.configure(bg="light cyan")
        load = Image.open("login.jpg")
        render = ImageTk.PhotoImage(load)
        img = tkinter.Label(image=render)
        img.image = render
        img.place(x=0, y=0)
        b2 = tkinter.Button(welcome, text="Sign Up", font=("League Spartan", 30), bg="slateblue1", fg="black",
                            command=signup)
        b2.place(x=350, y=400)
        b3 = tkinter.Button(welcome, text=" Log In ", font=("League Spartan", 30), bg="slateblue1", fg="black",
                            command=login)
        b3.place(x=710, y=400)
        new = tkinter.Label(welcome, text="New User? Sign Up First!", font=("Raleway Black", 12), fg="red",
                            bg="#FF908E")
        new.place(x=340, y=450)
        ok = tkinter.Label(welcome, text="To Order Your Favorite Food, You Need To Login First!",
                           font=("League Spartan", 20), fg="gray8", bg="#FF908E")
        ok.place(x=332, y=350)
        old = tkinter.Label(welcome, text="Returning User? Login Now!", font=("Raleway Black", 12), fg="red",
                            bg="#FF908E")
        old.place(x=680, y=450)
        # photo=tkinter.PhotoImage(file="login.png")
        # canvas=tkinter.Canvas(welcome,height=1280,width=720)
        # canvas.place(x=1,y=1)
        # canvas.create_image(1,1,image=photo, anchor="nw")

    applogin()


app()












