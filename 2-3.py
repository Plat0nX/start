#Из нарнийского чата Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов в сутки. Если режим сна Ани удовлетворяет рекомендациям Сергея, выведите “Это нормально”. Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”. Получаемое число A всегда меньше либо равно B (то есть это проверять не надо).
rec = float(input("Сколько часов порекомендовали спать Ане?"))
offset = float(input("Какие отклонения допустимы?"))
result = float(input("Сколько часов удалось поспать?"))
if rec-offset > result:
    print ("Недосып")
elif result > rec+offset:
    print ("Пересып")
else:
    print ("Все окей")