
import ayoub_visualisation as ayoub_visualisation
import youness_visualisation as youness_visualisation
import mohamed_visualisation as mohamed_visualisation
import yamin_visualisation as yamin_visualisation
import ali_visualisation as ali_visualisation

def show_menu():
    print('------------The Option-------------')
    print("Press : 1 for Ayoub's visualization code")
    print("Press : 2 for Youness's visualization code")
    print("Press : 3 for Mohamed's visualization code")
    print("Press : 4 for Yamin's visualization code")
    print("Press : 5 for Ali's visualization code")
        
show_menu()

while True: 
        code = int(input('Select option: '))
        
        if code == 1:
            ayoub_visualisation.Ay_visualisation()
            
        elif code == 2:
            youness_visualisation.Yo_visualisation()
            
        elif code == 3:
            mohamed_visualisation.Mo_visualisation()
            
        elif code == 4:
            yamin_visualisation.Ya_visualisation()
            
        elif code == 5:
            ali_visualisation.Al_visualisation()
                
        else:
            print('Invalid option. Please enter a number between 1 and 5.')
        
        show_menu()
