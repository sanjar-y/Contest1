def typeBasedTransformer(**args):
    transformed = {}

    for key, value in args.items():
        if isinstance(value, (int, float)):
            transformed[key] = value ** 2
        elif isinstance(value, str):
            transformed[key] = value[::-1]
        elif isinstance(value, bool):
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed[key] = type(value)(value[::-1])
        elif isinstance(value, dict):
            if len(set(value.values())) == len(value.values()):
                transformed[key] = {v: k for k, v in value.items()}
            else:
                transformed[key] = value
        else:
            transformed[key] = value

    return transformed

result = typeBasedTransformer(
    number=4,
    decimal=2.5,
    text="Hello",
    flag=True,
    items=[1, 2, 3],
    nums_tuple=(10, 20, 30),
    mapping={"a": 1, "b": 2},
    unsupported=set([1, 2, 3])
)

print(result)