def make_greeting(language):

    def greet(name):
        if language=="Gujrati":
            print("kem cho,",name)
        elif language=="English":
            print("Hello,",name)
        else:
            print("Hii,",name)
    return greet

Gujrati_greet=make_greeting("Gujrati")
English_greet=make_greeting("English")

Gujrati_greet("Aksha")
English_greet("Aksha")