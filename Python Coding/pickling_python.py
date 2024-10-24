# when python objects are converted into bytes streams , this process is called picking
# when bytes stream are converted into python objects are called unpicking

# pickling ---> serialization , flattening , marshalling
# unpickling ---> deserialization

#  use ----> to trasfer python objects into one server / system/ application to another

# important point

# picking file can be any format
# we have built in module pickle

# Disadvantage

# do not unpicked data when received from any intrusted source as they may have secuirty threats

# pickle module has no way to identy the security and threat

# --------------------------------------------------------------------------------------------------------

# we have four function
""" 1) dump() ----> py. objects ----> byte streams(store into file)
    2) load() ----> byte streams ------> py.objects(read from files)
    3) dumps()-----> py. objects  -----> byte-streams
    4) loads()------> byte-strems -----> python objects








"""