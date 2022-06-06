# fastapi-app-template

This project is a base template for creating a _FastAPI_ application with _poetry_.

A basic configuration for tools like _mypy_, _flake8_, _bandit_, _isort_, and _black_ is set.

Dependencies for testing are included.

## Containerizing the application

_Paketo_ buildpack is able to containerize the application from the _pyproject.toml_ file:

```bash
pack build my-app --buildpack paketo-buildpacks/python --builder paketobuildpacks/builder:base
```

After creating the image, the application runs with:

```bash
docker run --rm -p 8000:8000 my-app
```

## TODO

- Get _version_ from _pyproject.toml_ instead of hardcoding it in _app.\_\_init\_\_.py_.

- Set the configuration of _flake8_ in _pyproject.toml_ when the tool supports it.
