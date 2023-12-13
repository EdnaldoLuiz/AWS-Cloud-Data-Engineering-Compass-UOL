actors = []
total_gross = []
num_movies = []
avg_per_movie = []
top_movie = []
top_movie_gross = []

def split_line(line):
    fields = []
    field = ''
    in_quotes = False

    for char in line:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            fields.append(field.strip())
            field = ''
        else:
            field += char

    fields.append(field.strip())  
    return fields

with open('sprint-3\\exercicios\\exercicio-ETL\\actors.csv', 'r') as file:
    lines = file.readlines()[1:] 
    for line in lines:
        fields = split_line(line)
        actors.append(fields[0])
        total_gross.append(float(fields[1]))
        num_movies.append(int(fields[2]))
        avg_per_movie.append(float(fields[3]))
        top_movie.append(fields[4])
        top_movie_gross.append(float(fields[5]))

file.close()

max_num_movies = max(num_movies)
max_num_movies_actor = actors[num_movies.index(max_num_movies)]

avg_gross = sum(top_movie_gross) / len(top_movie_gross)

max_avg_per_movie = max(avg_per_movie)
max_avg_per_movie_actor = actors[avg_per_movie.index(max_avg_per_movie)]

top_movie_counts = {movie: top_movie.count(movie) for movie in set(top_movie)}
top_movie_counts_sorted = sorted(top_movie_counts.items(), key=lambda x: (-x[1], x[0]))

actors_total_gross_sorted = sorted(zip(actors, total_gross), key=lambda x: -x[1])

with open('sprint-3\\exercicios\\exercicio-ETL\\etapas\\etapa-1.txt', 'w') as file:
    file.write(f'{max_num_movies_actor} - {max_num_movies}\n')

with open('sprint-3\\exercicios\\exercicio-ETL\\etapas\\etapa-2.txt', 'w') as file:
    file.write(f'{avg_gross}\n')

with open('sprint-3\\exercicios\\exercicio-ETL\\etapas\\etapa-3.txt', 'w') as file:
    file.write(f'{max_avg_per_movie_actor} - {max_avg_per_movie}\n')

with open('sprint-3\\exercicios\\exercicio-ETL\\etapas\\etapa-4.txt', 'w') as file:
    for i, (movie, count) in enumerate(top_movie_counts_sorted, start=1):
        file.write(f'{i} - O filme {movie} aparece {count} vez(es) no dataset\n')

with open('sprint-3\\exercicios\\exercicio-ETL\\etapas\\etapa-5.txt', 'w') as file:
    for actor, gross in actors_total_gross_sorted:
        file.write(f'{actor} - {gross}\n')

file.close()