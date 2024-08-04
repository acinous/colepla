# find the 6 best courses given the current credits completed

from credits import current_credits

def hasPrereqs(course, completed):
    if not set(course.prerequisites) & set(current_credits):
        return True
    return False