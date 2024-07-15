import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
pillarcracker = customtkinter.CTk()
pillarcracker.title("Pillarseed Cracker")
pillarcracker.geometry("480x480")

pillarimage = customtkinter.CTkImage(dark_image=Image.open("./Pillars.png"), size=(480, 480))
pillarshower = customtkinter.CTkLabel(pillarcracker, image=pillarimage)
pillarshower.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

input1 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input1.place(x=230, y=100)

input2 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input2.place(x=130, y=100)

input3 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input3.place(x=330, y=100)

input4 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input4.place(x=355, y=200)

input5 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input5.place(x=70, y=200)

input6 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input6.place(x=375, y=290)

input7 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input7.place(x=40, y=290)

input8 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input8.place(x=230, y=392)

input9 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input9.place(x=155, y=362)

input10 = customtkinter.CTkEntry(pillarcracker, height=20, width=37.5)
input10.place(x=300, y=352)

class Random:
    def __init__(self, seed):
        self.seed = (seed ^ 0x5DEECE66D) & ((1 << 48) - 1)

    def next(self, bits):
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)
        return self.seed >> (48 - bits)
    def nextInt(self, bound):
        if bound <= 0:
            raise ValueError("Invalid bound")
        if (bound & (bound - 1)) == 0:
            return (bound * self.next(31)) >> 31
        bits = self.next(31)
        val = bits % bound
        while (bits - val + bound - 1) < 0:
            bits = self.next(31)
            val = bits % bound
        return val


def shuffling(seed, liste):
    r = Random(seed)
    for i in range(len(liste) - 1, 0, -1):
        j = r.nextInt(i + 1)
        liste[i], liste[j] = liste[j], liste[i]
    return liste


def match_pillars(seed, pillar_liste):
    liste = list(range(10))
    shuffling(seed, liste)
    for i in range(10):
        if pillar_liste[i] != "u" and (76 + liste[i] * 3) != int(pillar_liste[i]):
            return False
    return True


def find_pillar_seeds(pillar_liste):
    possible_seeds = []
    for seed in range(0, 2 ** 16):
        if match_pillars(seed, pillar_liste):
            possible_seeds.append(seed)
    return possible_seeds


def crack_pillarseed():
    inputs = [
        input8.get(), input9.get(), input7.get(),
        input5.get(), input2.get(), input1.get(),
        input3.get(), input4.get(), input6.get(),
        input10.get()
    ]
    inputs = [int(i) if i.isdigit() else "u" for i in inputs]

    try:
        possible_seeds = find_pillar_seeds(inputs)
        if possible_seeds:
            output.configure(text="Possible Pillarseeds: " + ", ".join(map(str, possible_seeds)))
        else:
            output.configure(text="No valid seeds found!")
    except ValueError as e:
        output.configure(text="Invalid input!")


crackbutton = customtkinter.CTkButton(pillarcracker, width=30, height=20, command=crack_pillarseed,
                                      text="Crack Pillarseed")
crackbutton.place(x=220, y=230)
output = customtkinter.CTkLabel(pillarcracker, width=100, height=20, text="Possible Pillarseeds: ", wraplength=230)
output.place(x=150, y=260)
info = customtkinter.CTkLabel(pillarcracker, width=480, height=20,text="Note: If you use this cracker from a screenshot make sure that only 1 of each")
info.place(x=0, y=0)
info2 = customtkinter.CTkLabel(pillarcracker, width=480, height=20,text="of the 10 following values will be the valid y levels you can input: 76, 79, 82,")
info2.place(x=0, y=20)
info3 = customtkinter.CTkLabel(pillarcracker, width=480, height=20, text="85, 88, 91, 94, 97, 100, 103,")
info3.place(x=0, y=40)
info3 = customtkinter.CTkLabel(pillarcracker, width=480, height=20, text='Input Pillarheights, use "u" if unsure')
info3.place(x=0, y=60)
info4 = customtkinter.CTkLabel(pillarcracker, width=100, height=20, text="Platform is here", font=("Arial", 20))
info4.place(x=240, y=450)
pillarcracker.mainloop()
