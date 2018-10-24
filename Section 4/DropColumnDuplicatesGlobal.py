import pandas as pd

data = {'key1': [1, 2, 2, 3, 3],
        'key2': [2, 2, 2, 1, 1],
        'data': [5, 6, 2, 2, 2]}

frame = pd.DataFrame(data, columns=['key1', 'key2', 'data'])

print("--------------Original--------------:\n", frame)

globalDuplicates = frame[frame.duplicated(['key1', 'key2', 'data'], keep='first')
                         | frame.duplicated(['key1', 'key2', 'data'])]

print("--------------GlobalDuplicates--------------:\n", globalDuplicates)


