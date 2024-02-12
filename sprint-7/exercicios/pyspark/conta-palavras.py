# Código para contar as palavras do README dentro do container do pyspark

text_file = sc.textFile("/home/README.md")  # Esse é meu caminho que copiei o README dentro do container
counts = (
    text_file.flatMap(lambda line: line.split(" "))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)
counts.collect()
