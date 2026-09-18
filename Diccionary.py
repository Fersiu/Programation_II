me = {
    "name": "lia",
    "age": 22,
    "a_student": True,
    }

me_list =["lia,22,True"]
print(me_list[0])
print(me["name"])

#modificar un elemento 
me_list[0]="LiaGrisales"
print(me_list)
me["name"]= "LiaGrisales"
print(me)

#agregar un elemento 
me.append(3017988046)
me["Direccion"] = "Cra 7J #88-34"
me["telefono"] = "3017988046"
#para agregar mas informacion
me_2 = ("Rh","0+","profession","data of scientist")

#update
me_2 = {"Rh": "o+","profession": "data of scientist"}
me.update(me_2)
print(me)

#eliminar un elemento 
eliminado = me.popitem("Rh")
eliminado = me.popitem("profession")
print(eliminado)
print("="*50)
print = me 

