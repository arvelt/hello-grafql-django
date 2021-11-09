HELLO-GRAFQL-DJANGO
---

From https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain


```
python manage.py runserver
```

Go to localhost:8000/graphql and type your first query!

```
query {
  allIngredients {
    id
    name
  }
}
```
