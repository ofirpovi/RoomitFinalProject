from datetime import date
from users.models import Profile


# todo: add consideration for idk answers and no answer
# returns number of similar fields and the number of fields compared
def compare_profiles(profile1: Profile, profile2: Profile):
    counter, total_fields = 0, 9

    def check_and_increment(var1, var2):
        nonlocal counter, total_fields
        if not_none(var1, var2):
            if var1 == var2:
                counter += 1
        elif var1 is None and var2 is None:
            total_fields -= 1

    if profile1.profile_status == profile2.profile_status:
        if not_none(profile1.birthdate, profile2.birthdate):
            if abs(calculate_age(profile1.birthdate) - calculate_age(profile2.birthdate)) < 3:
                counter += 1
        elif profile1.birthdate is None and profile2.birthdate is None:
            total_fields -= 1

        check_and_increment(profile1.gender, profile2.gender)

        check_and_increment(profile1.occupation, profile2.occupation)

        check_and_increment(profile1.smoker, profile2.smoker)

        check_and_increment(profile1.diet, profile2.diet)

        check_and_increment(profile1.status, profile2.status)

        check_and_increment(profile1.hospitality, profile2.hospitality)

        check_and_increment(profile1.kosher, profile2.kosher)

        check_and_increment(profile1.expense_management, profile2.expense_management)

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



def not_none(var1, var2):
    return var1 is not None and var2 is not None


def one_None(var1, var2):
    return var1 is None or var2 is None
