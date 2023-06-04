from roomit_app.models import RequirementsP, RequirementsR

# check if reqP1 fields are within the bounds or equal to reqP2
# todo: add calculations like in range req
# todo: add consideration for idk answers and no answer
# returns number of similar fields and the number of fields compared
def compare_reqP(reqP1: RequirementsP, reqP2: RequirementsP):
    counter, total_fields = 0, 9

    def check_and_increment(var1, var2):
        nonlocal counter, total_fields
        if not_none(var1, var2):
            if var1 >= var2:
                counter += 1
        elif var1 is None and var2 is None:
            total_fields -= 1

    def check_both_and_increment(var11, var12, var21, var22):
        nonlocal counter, total_fields
        if not_none(var11, var12) and not_none(var21, var22):
            if var11 >= var12 \
                    and var21 <= var22:
                counter += 1
        elif not_none(var11, var12):
            if var11 >= var12:
                counter += 1
        elif not_none(var21, var22):
            if var21 >= var22:
                counter += 1
        else:
            total_fields -= 1

    check_both_and_increment(reqP1.MinRent, reqP2.MinRent, reqP1.MaxRent, reqP2.MaxRent)

    check_both_and_increment(reqP1.MinRooms, reqP2.MinRooms, reqP1.MaxRooms, reqP2.MaxRooms)

    check_both_and_increment(reqP1.MinRoommates, reqP2.MinRoommates, reqP1.MaxRoommates, reqP2.MaxRoommates)

    check_and_increment(reqP1.MinToilets, reqP2.MinToilets)

    check_and_increment(reqP1.MinShowers, reqP2.MinShowers)

    if not_none(reqP1.Renovated, reqP2.Renovated):
        if reqP1.Renovated == reqP2.Renovated:
            counter += 1

    if not_none(reqP1.ShelterInside, reqP2.ShelterInside):
        if reqP1.ShelterInside == reqP2.ShelterInside:
            counter += 1

    if not_none(reqP1.ShelterNearby, reqP2.ShelterNearby):
        if reqP1.ShelterNearby == reqP2.ShelterNearby:
            counter += 1

    if not_none(reqP1.Furnished, reqP2.Furnished):
        if reqP1.Furnished == reqP2.Furnished:
            counter += 1

    if not_none(reqP1.SharedLivingRoom, reqP2.SharedLivingRoom):
        if reqP1.SharedLivingRoom == reqP2.SharedLivingRoom:
            counter += 1

    return counter, total_fields


# todo: add calculations like in range req
# todo: add consideration for idk answers and no answer
# returns number of similar fields and the number of fields compared
def compare_reqR(reqR1: RequirementsR, reqR2: RequirementsR):
    counter, total_fields = 0, 9

    def check_and_increment(var1, var2):
        nonlocal counter, total_fields
        if not_none(var1, var2):
            if var1 == var2:
                counter += 1
        elif var1 is None and var2 is None:
            total_fields -= 1

    def check_both_and_increment(var11, var12, var21, var22):
        nonlocal counter, total_fields
        if not_none(var11, var12) and not_none(var21, var22):
            if var11 >= var12 \
                    and var21 <= var22:
                counter += 1
        elif not_none(var11, var12):
            if var11 >= var12:
                counter += 1
        elif not_none(var21, var22):
            if var21 >= var22:
                counter += 1
        else:
            total_fields -= 1

    check_and_increment(reqR1.Occupation, reqR2.Occupation)

    check_both_and_increment(reqR1.MinAge, reqR2.MinAge, reqR1.MaxAge, reqR2.MaxAge)

    check_and_increment(reqR1.Gender, reqR2.Gender)

    check_and_increment(reqR1.Smoker, reqR2.Smoker)

    check_and_increment(reqR1.Diet, reqR2.Diet)

    check_and_increment(reqR1.Kosher, reqR2.Kosher)

    check_and_increment(reqR1.Status, reqR2.Status)

    check_and_increment(reqR1.Expense_Management, reqR2.Expense_Management)

    check_and_increment(reqR1.Hospitality, reqR2.Hospitality)

    return counter, total_fields


def not_none(var1, var2):
    return var1 is not None and var2 is not None


def one_None(var1, var2):
    return var1 is None or var2 is None
