# UV Setup

This project can be managed with `uv`.

## Install uv

```bash
python3 -m pip install --user uv
```

## Add uv to PATH

Add `uv` to your `PATH` in `~/.bashrc`:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Check that `uv` works:

```bash
uv --version
```

## Install a Python Version

Install a specific Python version, for example `3.11.10`:

```bash
uv python install 3.11.10
```

## Create a Virtual Environment

Create a virtual environment in the repository root with the default name `.venv`:

```bash
uv venv --python 3.11.10
```

Create a virtual environment with a custom name:

```bash
uv venv myenv --python 3.11.10
```

The virtual environment directory is created in the path you provide. For example, `uv venv myenv --python 3.11.10` creates `./myenv` in the current directory.

## Activate and Use the Environment

Activate the default virtual environment:

```bash
source .venv/bin/activate
```

Activate a custom virtual environment:

```bash
source myenv/bin/activate
```

Install packages when needed:

```bash
uv pip install pytest
```

Deactivate the environment:

```bash
deactivate
```

This repository already has a `.venv` created with `uv`.
