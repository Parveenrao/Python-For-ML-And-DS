# "a" -----> this mode is to used to append  file , typicallly writing the file into last

f = open("demo.txt", "a")

f.write("\nThen i will move to the Reinforcement Learnning")

f.close()


# if we write inot a file that is not exist , so it  create a new file of tha name

f = open("database.txt" , "w")
f.close()

