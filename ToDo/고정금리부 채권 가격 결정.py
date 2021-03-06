# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:06:45 2021

@author: njjwa
"""


# http://gouthamanbalaraman.com/blog/quantlib-bond-modeling.html
# Modeling Fixed Rate Bonds in QuantLib Python

print(3/pow(1+0.005, 0.5) + (100 + 3)/(1+0.007))
print(105.27653992490681)

import QuantLib as ql
todaysDate = ql.Date(15, 1, 2015)
ql.Settings.instance().evaluationDate = todaysDate
spotDates = [ql.Date(15, 1, 2015), ql.Date(15, 7, 2015), ql.Date(15, 1, 2016)]
spotRates = [0.0, 0.005, 0.007]
dayCount = ql.Thirty360()
calendar = ql.UnitedStates()
interpolation = ql.Linear()
compounding = ql.Compounded
compoundingFrequency = ql.Annual
spotCurve = ql.ZeroCurve(spotDates, spotRates, dayCount, calendar, interpolation, compounding, compoundingFrequency)
spotCurveHandle = ql.YieldTermStructureHandle(spotCurve)

issueDate = ql.Date(15, 1, 2015)
maturityDate = ql.Date(15, 1, 2016)
tenor = ql.Period(ql.Semiannual)
calendar = ql.UnitedStates()
bussinessConvention = ql.Unadjusted
dateGeneration = ql.DateGeneration.Backward
monthEnd = False
schedule = ql.Schedule (issueDate, maturityDate, tenor, calendar, bussinessConvention,
                            bussinessConvention , dateGeneration, monthEnd)
print(list(schedule))


dayCount = ql.Thirty360()
couponRate = .06
coupons = [couponRate]

# Now lets construct the FixedRateBond
settlementDays = 0
faceValue = 100
fixedRateBond = ql.FixedRateBond(settlementDays, faceValue, schedule, coupons, dayCount)

# create a bond engine with the term structure as input;
# set the bond to use this bond engine
bondEngine = ql.DiscountingBondEngine(spotCurveHandle)
fixedRateBond.setPricingEngine(bondEngine)

# Finally the price
print(fixedRateBond.NPV())

