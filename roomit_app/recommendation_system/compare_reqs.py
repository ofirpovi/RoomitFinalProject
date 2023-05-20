from roomit_app.models import RequirementsP, RequirementsR


# check if reqP1 fields are within the bounds or equal to reqP2
# todo: add calculations like in range req
# todo: add consideration for idk answers and no answer
# returns number of similar fields and the number of fields compared
def compare_reqP(reqP1: RequirementsP, reqP2: RequirementsP):
    counter, total_fields = 0, 11
    if reqP1.Country == reqP2.Country \
            and reqP1.City == reqP2.City:
        if reqP1.Neighborhood == reqP2.Neighborhood:
            counter += 1
        if reqP1.Neighborhood == reqP2.Neighborhood:
            counter += 1
        if reqP1.MinRent >= reqP2.MinRent \
                and reqP1.MaxRent <= reqP2.MaxRent:
            counter += 1
        if reqP1.MinRooms >= reqP2.MinRooms \
                and reqP1.MaxRooms <= reqP2.MaxRooms:
            counter += 1
        if reqP1.MinRoommates >= reqP2.MinRoommates \
                and reqP1.MaxRoommates <= reqP2.MaxRoommates:
            counter += 1
        if reqP1.MinToilets >= reqP2.MinRoommates:
            counter += 1
        if reqP1.MinShowers >= reqP2.MinShowers:
            counter += 1
        if reqP1.Renovated == reqP2.Renovated:
            counter += 1
        if reqP1.ShelterInside == reqP2.ShelterInside:
            counter += 1
        if reqP1.ShelterNearby == reqP2.ShelterNearby:
            counter += 1
        if reqP1.Furnished == reqP2.Furnished:
            counter += 1
        if reqP1.SharedLivingRoom == reqP2.SharedLivingRoom:
            counter += 1
    return counter, total_fields


# todo: add calculations like in range req
# todo: add consideration for idk answers and no answer
# returns number of similar fields and the number of fields compared
def compare_reqR(reqR1: RequirementsR, reqR2: RequirementsR):
    counter, total_fields = 0, 9
    if reqR1.Occupation == reqR2.Occupation:
        counter += 1
    if reqR1.MinAge >= reqR2.MinAge \
            and reqR1.MaxAge <= reqR2.MaxAge:
        counter += 1
    if reqR1.Gender == reqR2.Gender:
        counter += 1
    if reqR1.Smoker == reqR2.Smoker:
        counter += 1
    if reqR1.Diet == reqR2.Diet:
        counter += 1
    if reqR1.Kosher == reqR2.Kosher:
        counter += 1
    if reqR1.Status == reqR2.Status:
        counter += 1
    if reqR1.Expense_Management == reqR2.Expense_Management:
        counter += 1
    if reqR1.Hospitality == reqR2.Hospitality:
        counter += 1
    return counter, total_fields
