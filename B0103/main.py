nama_hero = "Julius"
level = 80
hp = 150.5
is_alive = True
inventory = ["panah","pedang","perisai"]
atribut = {"kekuatan":95, "kelincahan":70}

print("--profile hero--")
print("nama",nama_hero)
print("level",80)
print("hp",150.5)
print("is_alive",True)
print(inventory)
print({"kekuatan":95,"kelincahan":70})

print("--Tipe Data Hero--")
print("nama",type (nama_hero))
print("level",type(80))
print("hp",type(150.5))
print("is_alive",type(True))
print("inventory",type(inventory))
print("kekuatan","kelincahan",type(9570))

tambahkan_inventory = "ramuan hp"
level_baru = float (80*0.5)
inventory.append(tambahkan_inventory)

print ("--profile hero baru--")
print("nama",nama_hero)
print("level",level_baru)
print("hp",150.5)
print("is_alive",True)
print(inventory)
print({"kekuatan":95,"kelincahan":70})