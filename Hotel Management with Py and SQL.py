# Firsty, We have to connect the Python with MySQL.
import mysql.connector as star
mycon=star.connect(host="localhost", user="root", password="root1234", database="RiturajPro12")
cursor=mycon.cursor()
choice="Y"
# Now, We create a Menu for the Hotel Management.
while choice=="Y":
    print(" ******** Pyro Palace ********")
    print("         We Welcome You       ")
    print("1.List of Rooms Available")# Availablity of the Rooms can be checked out here.
    print("2.Member's List") # Current Members in the Hotel Premises.
    print("3.Enter Customer Data")# New Customers can add up the data here and it would be stoered in the Active Table till Checkout.
    print("4.Total Bill ") # Total Amount to be Paid by the Client to the Hotel Management
    print("5.Checkout Here") #Here Add Checkout information and that would be stored in a seperate Table in the Database.
    print("6.Exit")
    
    ch=int(input("Enter Your Choice :"))

    if ch==1:
        cursor.execute("SELECT * FROM ROOMS")
        data=cursor.fetchall()
        for row in data:
            print(row)

    elif ch==2:
        cursor.execute("SELECT * FROM MEMBERS")
        data=cursor.fetchall()
        for row in data:
            print(row)

    elif ch==3:
        # Taking some inputs from the user.
        mid=input("Enter the MemberID :")
        mn=input("Enter the Name :")
        rno=int(input("Enter the Room No :"))
        print("Enter the Dates as YYYY-MM-DD Format")
        checkin=input("Enter the Checkin Date :")
        checkout=input("Enter the Expected Checkout :")
        st="INSERT INTO MEMBERS(MemberID, MemberName, RoomNo, CheckinDate, CheckoutDate)\
         values('{}','{}',{},'{}','{}')".format(mid,mn,rno,checkin,checkout)
        cursor.execute(st)

    elif ch==4:
        # To get the Per Day Bill of the stay at the Hotel "PYRO PALACE".
        cursor.execute("SELECT MemberID, MemberName, Price+0.23*Price FROM MEMBERS, ROOMS WHERE ROOMS.RoomNo=MEMBERS.RoomNo")
        data=cursor.fetchall()
        for row in data:
            print(row)
        print("What was your Per Day Bill? Round it Off and use")
        print("Don't Worry just get the Total Bill Below")
        pdb=int(input("Enter the Per Day Bill :"))
        sd=int(input("Enter the No of Days You Stayed Here :"))
        total_b= pdb*sd
        print(total_b)

    elif ch==5:
        mid=input("Enter the MemberID")
        mn=input("Enter the Memeber Name")
        print("Enter the Dates as YYYY-MM-DD Format")
        checkin=input("Enter the Checkin Date")
        checkout=input("Enter the Checkout Date")
        st="INSERT INTO REGISTER(MemberID, MemberName, CheckinDate, CheckoutDate)\
         values('{}','{}','{}','{}')".format(mid,mn,checkin,checkout)
        cursor.execute(st)
        
        cursor.execute("SELECT * FROM REGISTER") # It will help to keep a saved copy of all checked out customer's data for Future Reference.
        data=cursor.fetchall()
        for row in data:
            print(row)
            
        tx="DELETE FROM MEMBERS WHERE MemberName='{}'".format(mn)
        cursor.execute(tx)
        mycon.commit()
        
    elif ch==6:
        print("Thanks for Visiting")
        break
 

