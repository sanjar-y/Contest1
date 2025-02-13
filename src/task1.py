def kwargsAcceptFun(**args):
    for key, value in args.items():
        print(f"{key}: {value}")

kwargsAcceptFun(name="Alice", age=25, city="New York")
