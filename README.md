## For installation of Python virtual Environment:-

```
python -m venv fastvenv
```

## To activate the Virtual Environment:-
```
fastvenv\Scripts\activate.bat
```

## Uvicorn:-
Uvicorn is the FAST API server

For uvicorn Installation:-
```
pip install "uvicorn[standard]"
```


## Path Parameters:
the way for us to be able to locate in FASTAPI where we want an application to run and it's just overall path or the URL

```
uvicorn books:app --reload
```
