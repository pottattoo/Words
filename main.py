words = {
    "лол" : "что то смешное",
    "сигма" : "уверенный",
    "кринж" : "стыд",
    "агро" : "злой",
}
while True:
    word = input ("введите слово:").lower()
    if word in words:
        print(words [word])
    else:
        print("слово не найдено")
