import tkinter
from tkinter import *
from PIL import ImageTk, Image
import datetime as dt
from tkcalendar import DateEntry


class BookingList:
    def __init__(self):
        self.bookingList = []

    def addBooking(self, booking):
        self.bookingList.append(booking)

    def getAllBookings(self):
        return self.bookingList

    def getSpaBookings(self):
        spaList = []
        for i in self.bookingList:
            if i.getBookingType() == "Spa Booking":
                spaList.append(i)
        return spaList

    def getRestaurantBookings(self):
        restList = []
        for i in self.bookingList:
            if i.getBookingType() == "Restaurant Booking":
                restList.append(i)
        return restList

    def getRoomBookings(self):
        roomList = []
        for i in self.bookingList:
            if i.getBookingType() == "Room Booking":
                roomList.append(i)
        return roomList


class Booking:
    def __init__(self, bookingType):
        self.bookingType = bookingType
        self.name = ""

    def getBookingType(self):
        return self.bookingType

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class SpaBooking(Booking):
    def __init__(self, bookingType):
        super().__init__(bookingType)
        self.massageLocation = None
        self.massageType = None
        self.extra = False
        self.price = 0
        self.dateTime = None

    def setMassageLocation(self, massageLocation):
        self.massageLocation = massageLocation

    def getMassageLocation(self):
        return self.massageLocation

    def setMassageType(self, massageType):
        self.massageType = massageType

    def getMassageType(self):
        return self.massageType

    def setExtra(self, extra):
        self.extra = extra

    def getExtra(self):
        return self.extra

    def addPrice(self, price):
        self.price += price

    def getPrice(self):
        return self.price

    def setDateTime(self, time):
        self.dateTime = time

    def getDateTime(self):
        return self.dateTime


class RoomBooking(Booking):
    def __init__(self, roomType, bookingType):
        super().__init__(bookingType)
        self.roomType = roomType
        self.startDate = None
        self.endDate = None
        self.price = 0

    def getRoomType(self):
        return self.roomType

    def setStarDate(self, date):
        self.startDate = date

    def getDateTime(self):
        return self.startDate

    def setEndDate(self, date):
        self.endDate = date

    def getEndDate(self):
        return self.endDate

    def addPrice(self, price):
        self.price += price

    def getPrice(self):
        return self.price


class RestaurantBooking(Booking):
    def __init__(self, bookingType):
        super().__init__(bookingType)
        self.restaurantBookingType = None
        self.dateTime = None

    def setRestaurantBookingType(self, restaurantBookingType):
        self.restaurantBookingType = restaurantBookingType

    def getRestaurantBookingType(self):
        return self.restaurantBookingType

    def setDateTime(self, time):
        self.dateTime = time

    def getDateTime(self):
        return self.dateTime


def openMenu():
    menuWindow = Toplevel(master)
    menuWindow.title("New Window")
    menuWindow.geometry("700x500")
    menuWindow.configure(bg="#abdbe3")
    menu_img = Image.open("menu.jpeg")
    resizedmenu_image = menu_img.resize((700, 500), Image.ANTIALIAS)
    newmenu_image = ImageTk.PhotoImage(resizedmenu_image)
    newmenu_image.image = newmenu_image
    place = Label(master=menuWindow, image=newmenu_image)
    place.grid(column=0, row=0)


def openSpaMenu():
    spaWindow = Toplevel(master)
    spaWindow.title("Spa Portal Window")
    spaWindow.geometry("550x700")
    spaWindow.configure(bg="#abdbe3")

    def submitSpaBooking():
        message = ""
        if e1.get() == "":
            message = "Error! Please insert a valid name. "
            bg = "#d53f52"
        elif cal.get_date() < dt.datetime.now().date():
            message = "Error! Please insert a valid date. "
            bg = "#d53f52"
        elif v1.get() == 0:
            message = "Please select a massage location. "
            bg = "#d53f52"
        elif v2.get() == 0:
            message = "  Please select a massage type.   "
            bg = "#d53f52"
        elif e2.get() == "":
            message = "Error! Please insert a valid time."
            bg = "#d53f52"
        else:
            message = "         Success! Booking has been set.          "
            bg = "#3fd571"
            try:
                dt_string = str(cal.get_date()) + " " + e2.get()
                format = "%Y-%m-%d %H:%M"
                dt.datetime.strptime(dt_string, format)
            except ValueError:
                message = "Error! Please insert a valid time."
                bg = "#d53f52"
        if message == "         Success! Booking has been set.          ":
            newSpaBooking = SpaBooking("Spa Booking")
            newSpaBooking.setName(e1.get())
            newSpaBooking.setDateTime(dt_string)
            if v1.get() == 1:
                newSpaBooking.setMassageLocation("Full Body")
                newSpaBooking.addPrice(150)
            elif v1.get() == 2:
                newSpaBooking.setMassageLocation("Back")
                newSpaBooking.addPrice(90)
            else:
                newSpaBooking.setMassageLocation("Face")
                newSpaBooking.addPrice(70)
            if v2.get() == 1:
                newSpaBooking.setMassageType("Hot Stone")
            elif v2.get() == 2:
                newSpaBooking.setMassageType("Anti-Stress")
            elif v2.get() == 3:
                newSpaBooking.setMassageType("Anti-Cellulite")
            else:
                newSpaBooking.setMassageType("Hawaiian Lomi-Lomi")
            if v3.get() == 1:
                newSpaBooking.addPrice(25)
                newSpaBooking.setExtra(True)
            bookingList.addBooking(newSpaBooking)

        Label(spaWindow, text=message, bg=bg, font=("Arial", 14)).grid(row=18, column=1)

    Label(spaWindow, text="\n   - Welcome to the Spa portal -   \n", bg="#5b779a", fg="white", font=("Arial", 18)).grid(
        row=0,
        column=1)
    Label(spaWindow, text="\n", bg="#abdbe3").grid(row=1, column=1)
    tkinter.Label(spaWindow, text="Full Name: ", bg="#abdbe3", font=("Arial", 13)).grid(row=2, column=0)
    e1 = tkinter.Entry(spaWindow)
    e1.grid(row=2, column=1)
    Label(spaWindow, text="\nSelect your massage location:", bg="#abdbe3", font=("Arial", 14)).grid(row=3, column=1)
    v1 = IntVar()
    Radiobutton(spaWindow, text='Full Body\n$150', variable=v1, value=1, bg="#abdbe3", font=("Arial", 13)).grid(row=4,
                                                                                                                column=0)
    Radiobutton(spaWindow, text='Back\n$90', variable=v1, value=2, bg="#abdbe3", font=("Arial", 13)).grid(row=4,
                                                                                                          column=1)
    Radiobutton(spaWindow, text='Face\n$70', variable=v1, value=3, bg="#abdbe3", font=("Arial", 13)).grid(row=4,
                                                                                                          column=2)
    Label(spaWindow, text="\nSelect your massage type:", bg="#abdbe3", font=("Arial", 14)).grid(row=5, column=1)
    v2 = IntVar()
    Radiobutton(spaWindow, text='Hot Stone Massage', variable=v2, value=1, bg="#abdbe3", fg="#c61515",
                font=("Arial", 13)).grid(row=6,
                                         column=1)
    Radiobutton(spaWindow, text='Anti-Stress Massage', variable=v2, value=2, bg="#abdbe3", fg="#2f0a97",
                font=("Arial", 13)).grid(
        row=7, column=1)
    Radiobutton(spaWindow, text='Anti-Cellulite Massage', variable=v2, bg="#abdbe3", value=3, fg="#399370",
                font=("Arial", 13)).grid(
        row=8, column=1)
    Radiobutton(spaWindow, text='Hawaiian Lomi-Lomi Massage', variable=v2, bg="#abdbe3", value=4, fg="#d610ad",
                font=("Arial", 13)).grid(row=9, column=1)
    Label(spaWindow, text="\nInclude Therapeutic Oils (25$)", bg="#abdbe3", font=("Arial", 14)).grid(row=10, column=1)
    v3 = IntVar()
    Checkbutton(spaWindow, text='Yes', variable=v3, bg="#abdbe3", font=("Arial", 13)).grid(row=11, column=1)
    Label(spaWindow, text="\nSelect a date:", bg="#abdbe3", font=("Arial", 14)).grid(row=13, column=1)
    v4 = DateEntry()
    cal = DateEntry(spaWindow, width=30, bg="dark-blue", variable=v4, fg="white", year=2022)
    cal.grid(row=14, column=1)
    tkinter.Label(spaWindow, text="Time: ", bg="#abdbe3", font=("Arial", 13)).grid(row=15, column=0)
    e2 = tkinter.Entry(spaWindow)
    e2.grid(row=15, column=1)
    Label(spaWindow, text="\n", bg="#abdbe3", font=("Arial", 14)).grid(row=16, column=1)
    SubmitButton = tkinter.Button(spaWindow, width=20, text="Submit Booking", command=submitSpaBooking)
    SubmitButton.grid(row=17, column=1)


def openRestaurantMenu():
    restaurantWindow = Toplevel(master)
    restaurantWindow.title("New Window")
    restaurantWindow.geometry("600x350")
    restaurantWindow.configure(bg="#abdbe3")

    def submitRestaurantBooking():
        message = ""
        if e1.get() == "":
            message = "Error! Please insert a valid name."
            bg = "#d53f52"
        elif cal.get_date() < dt.datetime.now().date():
            message = "Error! Please insert a valid date."
            bg = "#d53f52"
        elif v1.get() == 0 and v2.get() == 0:
            message = "Error! Please food, drink or both."
            bg = "#d53f52"
        else:
            message = " Success! Booking has been set.  "
            bg = "#3fd571"
            try:
                dt_string = str(cal.get_date()) + " " + e2.get()
                format = "%Y-%m-%d %H:%M"
                dt.datetime.strptime(dt_string, format)
            except ValueError:
                message = "Error! Please insert a valid time."
                bg = "#d53f52"
        if message == " Success! Booking has been set.  ":
            if v1.get() == 1 and v2.get() == 1:
                bookingType = "Food and Drink"
            elif v1.get() == 1:
                bookingType = "Food"
            else:
                bookingType = "Drink"
            newRestaurantBooking = RestaurantBooking("Restaurant Booking")
            newRestaurantBooking.setName(e1.get())
            newRestaurantBooking.setRestaurantBookingType(bookingType)
            newRestaurantBooking.setDateTime(dt_string)
            bookingList.addBooking(newRestaurantBooking)

        Label(restaurantWindow, text=message, bg=bg, font=("Arial", 14)).grid(row=18, column=1)

    menu = tkinter.Button(restaurantWindow, text="Show Menu", command=openMenu)
    menu.grid(row=1, column=1)
    Label(restaurantWindow, text="\n   - Welcome to the Restaurant portal -   \n", bg="#5b779a", fg="white",
          font=("Arial", 18)).grid(row=0, column=1)
    Label(restaurantWindow, text="\n", bg="#abdbe3").grid(row=1, column=0)
    tkinter.Label(restaurantWindow, text="Full Name: ", bg="#abdbe3", font=("Arial", 13)).grid(row=2, column=0)
    e1 = tkinter.Entry(restaurantWindow)
    e1.grid(row=2, column=1)
    v1 = IntVar()
    Checkbutton(restaurantWindow, text='Food', variable=v1, bg="#abdbe3", fg="#399370", font=("Arial", 13)).grid(row=8,
                                                                                                                 column=1)
    v2 = IntVar()
    Checkbutton(restaurantWindow, text='Drink', variable=v2, bg="#abdbe3", fg="#d610ad", font=("Arial", 13)).grid(row=9,
                                                                                                                  column=1)
    v4 = DateEntry()
    tkinter.Label(restaurantWindow, text="Date: ", bg="#abdbe3", font=("Arial", 13)).grid(row=14, column=0)
    cal = DateEntry(restaurantWindow, width=30, bg="dark-blue", variable=v4, fg="white", year=2022)
    cal.grid(row=14, column=1)
    tkinter.Label(restaurantWindow, text="Time: ", bg="#abdbe3", font=("Arial", 13)).grid(row=15, column=0)
    e2 = tkinter.Entry(restaurantWindow)
    e2.grid(row=15, column=1)
    Submit2 = Button(restaurantWindow, text="Submit", width=10, command=submitRestaurantBooking)
    Submit2.grid(row=17, column=1)


def openRoomsMenu():
    roomWindow = Toplevel(master)
    roomWindow.title("New Window")
    roomWindow.geometry("600x350")
    roomWindow.configure(bg="#abdbe3")

    def submitRoomsBooking():
        message = ""
        if e1.get() == "":
            message = "Error! Please insert a valid name."
            bg = "#d53f52"
        elif cal.get_date() < dt.datetime.now().date() or cal2.get_date() < dt.datetime.now().date() or cal.get_date() > cal2.get_date():
            message = "Error! Please insert a valid date."
            bg = "#d53f52"
        elif v3.get() == 0:
            message = "Error! Please select a room type."
            bg = "#d53f52"
        else:
            message = " Success! Booking has been set.  "
            bg = "#3fd571"
        if message == " Success! Booking has been set.  ":
            if v3.get() == 1:
                roomType = "Suit"
                price = 140
            elif v3.get() == 2:
                roomType = "Double"
                price = 260
            else:
                roomType = "Standard"
                price = 620
            newRoomBooking = RoomBooking(roomType, "Room Booking")
            newRoomBooking.setName(e1.get())
            newRoomBooking.setStarDate(str(cal.get_date()))
            newRoomBooking.setEndDate(str(cal2.get_date()))
            newRoomBooking.addPrice(price)
            bookingList.addBooking(newRoomBooking)

        Label(roomWindow, text=message, bg=bg, font=("Arial", 14)).grid(row=19, column=1)

    Label(roomWindow, text="\n   - Welcome to the Rooms portal -   \n", bg="#5b779a", fg="white",
          font=("Arial", 18)).grid(row=0, column=1)
    Label(roomWindow, text="\n", bg="#abdbe3").grid(row=1, column=1)
    tkinter.Label(roomWindow, text="Full Name: ", bg="#abdbe3", font=("Arial", 13)).grid(row=2, column=0)
    e1 = tkinter.Entry(roomWindow)
    e1.grid(row=2, column=1)
    v3 = IntVar()
    tkinter.Radiobutton(roomWindow, text='Standard  |  140$', variable=v3, bg="#abdbe3", value=1, fg="#d610ad",
                        font=("Arial", 13)).grid(row=9, column=1)
    tkinter.Radiobutton(roomWindow, text='Double  |  260$', variable=v3, bg="#abdbe3", value=2, fg="#399370",
                        font=("Arial", 13)).grid(row=8, column=1)
    tkinter.Radiobutton(roomWindow, text='Suite  |  620$', variable=v3, value=3, bg="#abdbe3", fg="#c61515",
                        font=("Arial", 13)).grid(row=6, column=1)
    v43 = DateEntry()
    tkinter.Label(roomWindow, text="Start Date: ", bg="#abdbe3", font=("Arial", 13)).grid(row=16, column=0)
    cal = DateEntry(roomWindow, width=30, bg="dark-blue", variable=v43, fg="white", year=2022)
    cal.grid(row=16, column=1)
    tkinter.Label(roomWindow, text="End Date: ", bg="#abdbe3", font=("Arial", 13)).grid(row=17, column=0)
    cal2 = DateEntry(roomWindow, width=30, bg="dark-blue", variable=v43, fg="white", year=2022)
    cal2.grid(row=17, column=1)
    Submit3 = Button(roomWindow, text="Submit", width=10, command=submitRoomsBooking)
    Submit3.grid(row=18, column=1)


def openSearchPanel():
    adminWindow = Toplevel(master)
    adminWindow.title("New Window")
    adminWindow.geometry("650x600")
    adminWindow.configure(bg="#abdbe3")

    def getClient():
        name = sub_entry.get()
        index1 = 1
        index2 = 5
        added = 0
        Label(adminWindow, text="                                                                             ",
              fg="#5b779a", bg="#abdbe3",
              font=("Arial", 14)).grid(row=index2, sticky=W, column=1)
        for i in bookingList.getAllBookings():
            if i.getName() == name:
                added = 1
                Label(adminWindow, text=str(index1) + ". " + i.getBookingType() + " " + i.getDateTime(), fg="#5b779a",
                      bg="#abdbe3",
                      font=("Arial", 14)).grid(row=index2, sticky=W, column=1)
                index1 += 1
                index2 += 2
        if added == 0:
            Label(adminWindow, text="Couldn't find any bookings under this name.", fg="#5b779a", bg="#abdbe3",
                  font=("Arial", 14)).grid(row=index2, sticky=W, column=1)

    Label(adminWindow, text="\n   - Search Panel -   \n", bg="#5b779a", fg="white",
          font=("Arial", 18)).grid(row=0, column=1)
    Label(adminWindow, text="                                                                             ",
          fg="#5b779a", bg="#abdbe3",
          font=("Arial", 14)).grid(row=5, sticky=W, column=1)
    Label(adminWindow, text="\n", bg="#abdbe3").grid(row=1, column=1)
    tkinter.Label(adminWindow, text="Your Full Name: ", bg="#abdbe3", font=("Arial", 13)).grid(row=2, column=0)
    sub_entry = tkinter.Entry(adminWindow)
    sub_entry.grid(row=2, column=1)
    tkinter.Label(adminWindow, text="Your Bookings: ", bg="#abdbe3", font=("Arial", 13)).grid(row=3, column=0)
    admin = tkinter.Button(adminWindow, text="SEARCH", command=getClient)
    admin.grid(row=4, column=1)


def openAdminPanel():
    username = input("Insert username: ")
    password = input("Insert password: ")
    if username == "admin" and password == "1234":
        ch1 = ""
        while ch1 != "5":
            print("\x1b[0m")
            print("1.Get Spa Bookings")
            print("2.Get Restaurant Bookings")
            print("3.Get Room Bookings")
            print("4.Get All Bookings")
            print("5.Cancel")
            ch1 = input("Please select an action: ")
            print("\x1b[93m")
            if ch1 == "1":
                index = 1
                for i in bookingList.getSpaBookings():
                    print(
                        str(index) + ". " + "Name: " + i.getName() + " | " + "Location: " + i.getMassageLocation() + " | "
                        + "Types: " + i.getMassageType() + " | " + "Extras: " + str(i.getExtra()) + " | " + "Price: $"
                        + str(i.getPrice()) + " | " + "Date: " + str(i.getDateTime()))
                    index += 1
                if index == 1:
                    print("No Spa Bookings found.")
            elif ch1 == "2":
                index = 1
                for i in bookingList.getRestaurantBookings():
                    print(
                        str(index) + ". " + "Name: " + i.getName() + " | " + "Type: " + i.getRestaurantBookingType() + " | " + "Date: " + str(
                            i.getDateTime()))
                    index += 1
                if index == 1:
                    print("No Restaurant Bookings found.")
            elif ch1 == "3":
                index = 1
                for i in bookingList.getRoomBookings():
                    print(
                        str(index) + ". " + "Name: " + i.getName() + " | " + "Type: " + i.getRoomType() + " | " +
                        "Start Date: " + str(i.getDateTime()) + " | " + "End Date: " + str(i.getDateTime()) + " | " +
                        "Price: $" + str(i.getPrice()))
                    index += 1
                if index == 1:
                    print("No Room Bookings found.")
            elif ch1 == "4":
                index = 1
                for i in bookingList.getAllBookings():
                    print(
                        str(index) + ". " + "Name: " + i.getName() + " | " + "Type: " + i.getBookingType() + " | " +
                        "Start Date: " + str(i.getDateTime()))
                    index += 1
                if index == 1:
                    print("No Bookings found.")
            elif ch1 == "5":
                print("\x1b[91mExiting Admin Panel\x1b[0m\n")
            else:
                print("\x1b[91mInvalid choice! Please try Again.\x1b[0m\n")
    else:
        print("\x1b[91mInvalid username or password! Please try Again.\x1b[0m\n")


master = tkinter.Tk()
master.title("Welcome to your Last Resort")
master.geometry("600x500")
master.configure(bg="#abdbe3")

button1 = tkinter.Button(master, text="SPA", command=openSpaMenu)
Spa_img = Image.open("spa.png")
resized_image = Spa_img.resize((140, 90), Image.ANTIALIAS)
new_image1 = ImageTk.PhotoImage(resized_image)
lab1 = Label(image=new_image1)
button1.grid(row=5, column=0)
lab1.grid(row=6, column=0)

button2 = tkinter.Button(master, text="RESTAURANT", command=openRestaurantMenu)
Restaurant_img = Image.open("restaurant.png")
resized_image2 = Restaurant_img.resize((140, 90), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(resized_image2)
lab2 = Label(image=new_image2)
button2.grid(row=5, column=1)
lab2.grid(row=6, column=1)

button3 = tkinter.Button(master, text="ROOMS", command=openRoomsMenu)
Rooms_img = Image.open("rooms.png")
resized_image3 = Rooms_img.resize((140, 90), Image.ANTIALIAS)
new_image3 = ImageTk.PhotoImage(resized_image3)
lab3 = Label(image=new_image3)
button3.grid(row=5, column=2)
lab3.grid(row=6, column=2)
Label(master, text="\n", bg="#abdbe3").grid(row=15, column=1)
admin = tkinter.Button(master, text="SEARCH BOOKING", command=openSearchPanel)
admin.grid(row=16, column=1)
Label(master, text="\n", bg="#abdbe3").grid(row=17, column=1)
tkinter.Button(master, text="ADMIN OPTIONS", font=("Arial", 7), command=openAdminPanel).grid(row=18, column=1)

Label(master, text="\n   - Welcome to the Last Resort -   \n", bg="#28aaa2", fg="white", font=("Arial", 15)).grid(row=0,
                                                                                                                  column=1)
Resort_img = Image.open("resort.png")
resized_image = Resort_img.resize((250, 140), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
lab = Label(image=new_image)
lab.grid(row=1, column=1)
Label(master, text="",bg="#abdbe3").grid(row=4, column=1)
var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
var3 = tkinter.IntVar()
bookingList = BookingList()
master.mainloop()
