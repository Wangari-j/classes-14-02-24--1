class County:
    coName = " "
    coPop = 0

    def slogan(self):
        print("Welcome to the land of opportunities.")

    def fact(self):
        print("Lake Victoria is found in this county.")

    def fact2(self):
        print(coName1.coName + " is a beautiful town at the foot of Mount Kenya.")



coName1 = County()
coName2 = County()

coName1.coName = "Embu"
print(coName1.coName)

coName2.coName = "Kisumu"
print(coName2.coName)

coName2.coPop = 685,000
coName1.coPop = 750,905

print(coName2.coPop)
print(coName1.coPop)

coName2.slogan()
coName2.fact()
coName1.fact2()

