
Run app locally:

uvicorn app:app --reload

docker build -t rest-fast-apis-python .
docker run -p 5000:8000 rest-fast-apis-python
