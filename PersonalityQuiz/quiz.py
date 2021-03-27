
print('Hello, Contosoville!')

activity = input(
    'How would you like to spend your evening?\n(A)Reading a book\n(B)Attending a party\n')
if activity == 'A':
    print('Reading a book, nice choice!')
elif activity == 'B':
    print('Attending a party? Sounds fun!')
else:
    print('You must type A or B, let\'s just say you like to read')
    activity = 'A'

job = input(
    'What\'s your dream job?\n(A)Curator at the Smithsonian\n(B)Running a business\n')
if job == 'A':
    print('Curator, nice choice!')
elif job == 'B':
    print('Running a business? Sounds fun!')
else:
    print('You must type A or B, let\'s just say you want to be a curator at the Smithsonian')
    job = 'A'

value = input('What\'s more important?\n(A)Money\n(B)Love\n')
if value == 'A':
    print('Money, nice choice!')
elif value == 'B':
    print('Love? Sounds fun!')
else:
    print('You must type A or B, let\'s just say money is more important for you')
    value = 'A'

decade = input('What\'s your favourite decade?\n(A)1910s\n(B)2010s\n')
if value == 'A':
    print('1910s, nice choice!')
elif value == 'B':
    print('2010s? Sounds fun!')
else:
    print('You must type A or B, let\'s just say the 1910s is your favourite decade')
    decade = 'A'

travel = input(
    'What\'s your favourite way to travel?\n(A)Driving\n(B)Flying\n')
if travel == 'A':
    print('Driving, nice choice!')
elif travel == 'B':
    print('Flying? Sounds fun!')
else:
    print('You must type A or B, let\'s just say your favourite way to travel is by driving')
    travel = 'A'

print(
    f'You choose {activity}, then {job}, then {value}, then {decade}, then {travel}.')


sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

if activity == 'A':
    sam_like += 2
    indy_like += 2
    kai_like += 2
else:
    cam_like += 1
    indy_like += 1

if job == 'A':
    sam_like += 2
    indy_like += 2
    cam_like -= 1
else:
    sam_like -= 1
    kai_like += 2
    indy_like += 1

if value == 'A':
    sam_like -= 1
    kai_like += 1
else:
    sam_like += 2
    cam_like += 2
    indy_like += 1

if decade == 'A':
    cam_like += 2
    sam_like += 2
else:
    kai_like += 1
    indy_like += 2

if travel == 'A':
    sam_like -= 2
    kai_like += 1
    indy_like -= 1
else:
    sam_like += 1
    cam_like += 1
    kai_like -= 1

if sam_like >= 3:
    print('You\'re must like Sharp-Eyed Sam!')
elif cam_like >= 3:
    print('You\'re must like Curious Man!')
elif kai_like >=3:
    print('You\'re must like Keen Kai!')
else:
    print('You\'re must like Inquisitive Indy')

    
