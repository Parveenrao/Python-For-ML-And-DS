name = "parveen"
name = "Yadav"

# in python one tag cant point two object .. so it allocate memory to yadaav

# and parveen tag has no tag so it is called garbage collector adn it was removed by pyton automatically

# Garbage collection

# python remove objects which have no reference
# it uses two algorithms (reference counting and tracking)

#--------------------------------------------------------------

# Reference counting

# 1) reference count --> no of names pointing to an object
# 2) python keep track using field ref-count
# 3) new refernce created ---> incremented
# 4) Reference removed ---> decremented
# 5) Reference count became 0 ---> call garbage collector

#-------------------------------------------

# what make refernces
# 1) creating object
# 2) giving new name to object
# 3) adding name to data structure
# 4) passing in fucntion

# what remove references

# 1) assignment of new object to name
# 2) when variable goes out to scope

#--------------------------------------

# disadavtages of garbage collection

# 1) space required to store count
# 2) execution overhead , evey time count needs to be updated internally

# 3) cascading effect

