import movie_metadata
import movie_controller

def main():
     print('1.View the movies sorted just by ratings:')
     print('2.View movies only over a certain rating:')
     print('3.View movies sorted by Genre:')
     print('4.View movies sorted by Rating and Genre:')
     print('5.search movie title:')
     print('6. GO BACK')
     choice = input('Enter your choice : ')
     if choice == '1':
         movie_controller.movieratings()
     elif choice == '2':
         movie_controller.user_rating()

     elif choice == '3':
           movie_controller.genre()
     elif choice == '4':
         movie_controller.rating_genre()
     elif choice == '5':
         movie_controller.check_title()
     elif choice == '6':
         print("thank you for visiting")

     else:
        print("enter valid choice")


if __name__ == '__main__':
     main()
