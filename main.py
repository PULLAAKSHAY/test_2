def to_upper(name):
    return name.upper()

def say_hello(name):
    upper_name = to_upper(name)
    return f"Hello, {upper_name}!"

if __name__ == "__main__":
    print(say_hello("world"))   # This will output: Hello, WORLD!
    print(say_hello("Alice"))   # This will output: Hello, ALICE!
    