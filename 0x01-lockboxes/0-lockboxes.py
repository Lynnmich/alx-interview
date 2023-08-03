def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    stack = [0]  

    while stack:
        box = stack.pop()
        unlocked[box] = True

        for key in boxes[box]:
            if not unlocked[key]:
                stack.append(key)

    return all(unlocked)
