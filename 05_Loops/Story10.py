users=[
    {"id":1,"total":100,"coupon":"p20"},
    {"id":2,"total":150,"coupon":"p21"},
    {"id":3,"total":80,"coupon":"p22"}
]
discount={
    "p20":(0.2,0),
    "p21":(0.5,0),
    "p22":(0,10)
}
for user in users:
    percent, fixed= discount.get(user["coupon"],(0,0))
    dis=user["total"]*percent
    print(f"{user["id"]} paid {user["total"]}")