install:
	uv sync

uninstall:
	uv tool uninstall hexlet-code

brain-games:
	uv run brain-games
  
build:
	uv build

package-install:
	uv tool install dist/*.whl
	
lint:
	uv run ruff check brain_games

lint-fis:
	uv run ruff check brain_games --fix
	
brain-even:
	uv run brain-even
	
