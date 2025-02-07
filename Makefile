install:
	uv sync

uninstall:
	uv tool uninstall hexlet-code

brain-games:
	uv run brain-games
	
brain-even:
	uv run brain-even
	
brain-calc:
	uv run brain-calc
	
brain-gcd:
	uv run brain-gcd

brain-prg:
	uv run brain-prg
	
brain-prime:
	uv run brain-prime
  
build:
	uv build

package-install:
	uv tool install dist/*.whl
	
lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check brain_games --fix
