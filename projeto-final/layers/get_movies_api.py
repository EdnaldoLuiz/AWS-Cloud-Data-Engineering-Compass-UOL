import datetime
import json
import requests
import boto3

def lambda_handler(event, context):

    region_name="us-east-1"
    s3 = boto3.client("s3", region_name=region_name)
    api_key = "e4f6fca45b95d5b6b44904d806c9fe0d"
    nome_bucket = "desafios-etl"
    data_processamento = datetime.datetime.now().strftime('%Y/%m/%d')
    url_discover = "https://api.themoviedb.org/3/discover/movie"
    url_movie = "https://api.themoviedb.org/3/movie/"
    querystring = {
        "api_key": api_key,
        "language": "pt-BR",
        "sort_by": "vote_average.desc",
        "include_adult": "false",
        "include_video": "false",
        "primary_release_date.gte": "2000-01-01",
        "primary_release_date.lte": str(datetime.datetime.today()),
        "vote_count.gte": "500",
        "with_genres": "18,10749",
    }

    all_movies = []
    for page in range(1, 400):
        querystring["page"] = str(page)
        response_discover = requests.request("GET", url_discover, params=querystring)
        data_discover = response_discover.json()

        for result in data_discover["results"]:
            querystring["append_to_response"] = "credits"
            response_movie = requests.request(
                "GET", url_movie + str(result["id"]), params=querystring
            )
            data_movie = response_movie.json()
            movie_details = {
                "id": data_movie["id"],
                "title": data_movie["title"],
                "revenue": data_movie["revenue"],
                "budget": data_movie["budget"],
                "vote_average": data_movie["vote_average"],
                "vote_count": data_movie["vote_count"],
                "release_date": data_movie["release_date"],
                "main_actor": next(
                    (
                        cast["name"]
                        for cast in data_movie["credits"]["cast"]
                        if cast["order"] == 0
                    ),
                    None,
                ),
                "director": next(
                    (
                        crew["name"]
                        for crew in data_movie["credits"]["crew"]
                        if crew["job"] == "Director"
                    ),
                    None,
                ),
            }
            all_movies.append(movie_details)

    chunks = [all_movies[i : i + 100] for i in range(0, len(all_movies), 100)]

    for i, chunk in enumerate(chunks):
        s3.put_object(
            Body=json.dumps(chunk, indent=4, ensure_ascii=False),
            Bucket=nome_bucket,
            Key=f"Raw/tmdb/json/{data_processamento}/filmes_{i+1:02}.json",
            ContentType='application/json'
        )

    return {"statusCode": 200, "body": json.dumps("Dados gravados com sucesso no S3!")}