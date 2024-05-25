number = [1, 3, 5]
doubled = [num * 2 for num in number]

friends = ["For", "The", "Love", "Sof", "loops"]
starts_with = [friend for friend in friends if friend.startswith("S")]

print(starts_with)