data = {'id': [1, 2, 2, 3, 3],
        'name': ["Tom", "Janet", "Janet", "Billy", "Billy"],
        'age': [25, 32, 32, 42, 42]}

duplicates = set()
count = 0


def count(x):
    global count
    if duplicates.__contains__(x.id):
        return

    duplicates.add(x.id)
    count += 1
