class Movie:
    def __init__(self, title , mins , hero):
        self.title = title
        self.mins = mins
        self.hero = hero
        
    def display(self):
         print(f"The title of movie is {self.title} and total duration of movie is {self.mins} and the hero in movie is {self.hero}")   
         
list_of_movies = []

while True:
    title = input("Enter the title  movie name")
    mins = int(input('Enter the duration of movie'))
    hero = input('Enter the name of the hero')
    mo = Movie(title , mins , hero)
    list_of_movies.append(mo)
    
    print(f'movie added to the list')
    ans = input("Do you want to continue(y/n)")
    if ans!= 'y':
       break            
   
   


for mo in list_of_movies:
    mo.display()