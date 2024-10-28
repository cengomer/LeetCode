roadmap = {
    'San Diego': ['San Francisco', 'Los Angeles', 'Las Vegas'],
    'San Francisco': ['San Diego', 'Los Angeles'],
    'Los Angeles': ['San Diego', 'San Francisco', 'Las Vegas'],
    'Las Vegas': ['San Diego', 'Los Angeles']
}

roadmap['Seattle'] = []
roadmap['San Diego'].append('Seattle')    # Adds an edge between San Diego and Seattle.
print(roadmap)