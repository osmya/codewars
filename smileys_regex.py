import re

def count_smileys(arr):
    count = 0
    for face in arr:
        if re.match('[:;][-~]?[)D]', face):
            count += 1
    return count
    
    
# alternatives

# from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
    
    
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count
