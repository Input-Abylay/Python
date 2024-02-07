from diction import movies
movies = movies()
def sub(movies):
    s = []
    for i in movies:
        if i["imdb"] >= 5.5:
            s.append(i)
    return s
print(sub(movies))