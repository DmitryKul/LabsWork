users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

unique_users = len(set(users))

dict_ = {
    "Общее количество": len(users),
    "Уникальные посещения": unique_users

} # TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

print(dict_)