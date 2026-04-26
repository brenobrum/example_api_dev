local:
	uvicorn main:app --reload

test:
	uv run pytest -v