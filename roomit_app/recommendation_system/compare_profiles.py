from datetime import date
from users.models import Profile


# todo: add consideration for idk answers and no answer
# returns number of similar fields and the number of fields compared
def compare_profiles(profile1: Profile, profile2: Profile):
    counter, total_fields = 0, 9
    if profile1.profile_status == profile2.profile_status:
        if abs(calculate_age(profile1.birthdate) - calculate_age(profile2.birthdate)) < 3:
            counter += 1
        if profile1.gender == profile2.gender:
            counter += 1
        if profile1.occupation == profile2.occupation:
            counter += 1
        if profile1.smoker == profile2.smoker:
            counter += 1
        if profile1.diet == profile2.diet:
            counter += 1
        if profile1.status == profile2.status:
            counter += 1
        if profile1.hospitality == profile2.hospitality:
            counter += 1
        if profile1.kosher == profile2.kosher:
            counter += 1
        if profile1.expense_management == profile2.expense_management:
            counter += 1
    return counter, total_fields


# return the age from a given date of birth
# assumes type of dob is date (from datetime)
def calculate_age(dob):
    today = date.today()
    # check that birthday is of type date
    if type(dob) is not date:
        raise TypeError("Birthday must be a date")

    # check that the birthdate has past
    if dob > today:
        raise ValueError("Birthday must be a date from the past")

    # calculate age from given birthdate
    age = today.year - dob.year - ((today.month, today.day) <
         (dob.month, dob.day))
    return age



