# String concatenation (how to put strings together)
# Create a string that says "Subscribe to ____"
youtuber = "Michael Garcia" #string variable

#few ways to do this
#print("Subscribe to " + youtuber)
#print("Subscribe to {}".format(youtuber))
#print(f"Subscribe to {youtuber}")
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlibs = f"Computer prgramming is so {adj}! It \
makes me so excited all the time because I love \
to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlibs)