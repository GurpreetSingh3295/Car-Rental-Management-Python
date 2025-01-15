import booking
import billing
import search
import managebooking
import display

# ======== Main Menu ========
def main():
    print('====================================================================================================================================')
    print('\n','\t\t\t\t\t\t' ' +===== MAIN MENU ====+')
    print('''\t\t\t\t\t\t |====================|
\t\t\t\t\t\t |  1.    Booking     |
\t\t\t\t\t\t |  2. Manage Booking |
\t\t\t\t\t\t |  3. Search Booking |
\t\t\t\t\t\t |  4.   Return Car   |
\t\t\t\t\t\t +====================+''')
    menu = int(input('\t\t\t\t\t\tEnter your choice:'))

#============================= Booking =======================================
    if menu == 1:
        print()
        opt=input('\t\t\t\tAre you sure you want to book a car? (y/n)')
        print()
        if opt in 'yY':
            print('\t========================================  BOOKING  ============================================')
            booking.Add()
            main()
        else:
            main()

#===========================  Updation ========================================

    elif menu==2:
        print()
        print('\t===========================================  MANAGE BOOKING  ============================================')
        print()
        print('\t\t\t\t\t1.Cancel booking\n\t\t\t\t\t2.update booking\n\t\t\t\t\t\t===press 0 to exit===')
        opt=int(input('\t\t\t\t\tEnter your choice-'))
        print()
        if opt==1:
            managebooking.Cancel()
            main()
        elif opt==2:
            managebooking.Update_Days()
            main()
        elif opt==0:
            main()
        
#============================  Searching  ===================================

    elif menu==3:
        print()
        print('\t\t====================================== SEARCHING ============================================')
        print()
        print('\t\t\t\t\t1.Search Booking using Username\n\t\t\t\t\t2.Search Booking using Booking Number\n\t\t\t\t\t\t=======press 0 to exit======')
        print()
        opt=int(input('\t\t\t\t\tEnter your choice'))
        if opt==1:
            search.name()
            main()
        elif opt==2:
            search.Book()
            main()
        if opt==0:
            main()
        
#========================= Car Return =========================

    elif menu==4:
        print()
        print('\t\t======================================= RETURN ============================================')
        print()
        print('\t\t\t\t\t1.Return Car\n\t\t\t\t\t\t======== press 0 to exit=========')
        query=int(input('\t\t\t\t\tEnter your choice'))
        print()
        if query==1:
            opt=input('\t\t\t\t\tAre you sure you want to return the car? (y/n)')
            print()
            if opt in 'yY':
                billing.Bill()
                main()
            else:
                main()
        else:
            main()

#=========================== Exit ==============================

    elif menu==0:
        print('\n\t\t\t\t==================== THANK YOU FOR VISITING US! =========================')
        exit

    else:
        print("\t\t\t\t\tError: Invalid Choice! Try Again!")
        conti=int(input("\t\t\t\t\tPress any key to continue:"))
        main()


if __name__=='__main__':
    # ======== Title ========
    print('''\t\t\t\t\t                               
\t\t\t\t                   ___ __ _ _ __ ___        ______
\t\t\t\t                  / __/ _` | '__/ __|      /|_||_\`.__ 
\t\t\t\t                 | (_| (_| | |  \__ \     (   _    _ _\\n            
\t\t\t\t                  \___\__,_|_|  |___/     =`-(_)--(_)-'

         
\t\t\t\t  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗██████╗░███████╗██████╗░██╗███╗░░██╗░██████╗░
\t\t\t\t  ░██║░░██╗░░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██╔══██╗██║████╗░██║██╔════╝░
\t\t\t\t  ░╚██╗████╗██╔╝███████║██╔██╗██║██║░░██║█████╗░░██████╔╝██║██╔██╗██║██║░░██╗░
\t\t\t\t  ░░████╔═████║░██╔══██║██║╚████║██║░░██║██╔══╝░░██╔══██╗██║██║╚████║██║░░╚██╗
\t\t\t\t  ░░╚██╔╝░╚██╔╝░██║░░██║██║░╚███║██████╔╝███████╗██║░░██║██║██║░╚███║╚██████╔╝
\t\t\t\t  ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░

\t\t\t\t\t  ░██╗░░░░░░░██╗██╗░░██╗███████╗███████╗██╗░░░░░░██████╗
\t\t\t\t\t  ░██║░░██╗░░██║██║░░██║██╔════╝██╔════╝██║░░░░░██╔════╝
\t\t\t\t\t  ░╚██╗████╗██╔╝███████║█████╗░░█████╗░░██║░░░░░╚█████╗░
\t\t\t\t\t  ░░████╔═████║░██╔══██║██╔══╝░░██╔══╝░░██║░░░░░░╚═══██╗
\t\t\t\t\t  ░░╚██╔╝░╚██╔╝░██║░░██║███████╗███████╗███████╗██████╔╝
\t\t\t\t\t  ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═════╝░
                                                                                    ''')  

    print('=====================================================================================================================================')
    print('=============================================== WELCOME TO WANDERING WHEELS! ========================================================')
    print('=====================================================================================================================================')
    print('                                                 "YOU NEED NOT THINK TWICE!"                                     ')
                                                                                                                           
                                                                                                                                                                                            

main()
