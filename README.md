# Installing and Running!

This is a pretty simple exercise, in order to execute you need to have `pytest` package on your environment. You can do this installing like:

```bash
pip install -U pytest
```
Or creating a local environment and installing on it! I personally recommend `venv` for simplicity sake. You can check out the library [here](https://docs.python.org/3/library/venv.html). But here is an exemple using it in a linux environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pytest
```

After installing pytest, you'll need to just run the `pytest` command at the terminal
```bash
pytest
```
