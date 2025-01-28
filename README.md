class person:
    name = "sahil"
    occupation = "software engineer"
    def info(self):
        print(f"The name is {self.name} and occupation is {self.occupation}")
        

a = person()
print(a.name)
print(a.info())
b =person()
b.name = "harry"
b.occupation="youtuber"
b.info()
 
