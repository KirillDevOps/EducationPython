name=["Ваня","Миша","Петя"]
print (name)
print (f"Не сможет прийти {name[1]}")
del name[1]
name.insert(1,"Коля")
print (f"Добавился {name[1]}")
print (f"Приглашаю тебя, {name[0]}")
print (f"Приглашаю тебя, {name[1]}")
print (f"Приглашаю тебя, {name[2]}")
name.insert(0,"Оля")
name.insert(2,"Маша")
name.append("Катя")
print (f"Добавятся 3 гостя: {name[0],name[2],name[-1]}")
print (f"Приглашаю тебя, {name[0]}")
print (f"Приглашаю тебя, {name[1]}")
print (f"Приглашаю тебя, {name[2]}")
print (f"Приглашаю тебя, {name[3]}")
print (f"Приглашаю тебя, {name[4]}")
print (f"Приглашаю тебя, {name[5]}")
print("На обед приглашаются только 2 гостя, стол не привезут")
a=name.pop()
print(f"Сожалею, что не получится пригласить {a}")
a=name.pop()
print(f"Сожалею, что не получится пригласить {a}")
a=name.pop()
print(f"Сожалею, что не получится пригласить {a}")
a=name.pop()
print(f"Сожалею, что не получится пригласить {a}")
print (f"Приглашение в силе для {name[0]}")
print (f"Приглашение в силе для {name[1]}")
del name[0]
del name[0]
print(name)