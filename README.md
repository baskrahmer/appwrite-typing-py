# Type hints for your Appwrite Python functions

Whenever I develop an Appwrite function, I am left wondering what all these Flask abstractions mean since they are not from an installable package. Wonder no more!

```python
from appwrite_typing.py310.server import Context

def main(context: "Context"):  # <-- we actually know what this means now!
    return context.res.send("Hello World!")

def test_main():
    response = main(Context())  # <-- we can actually test with real objects
    assert response["body"] == "Hello World!"
```