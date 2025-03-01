def total_calc (billamount,tippercentage):
    total=billamount*(1+0.01*tippercentage)
    total=round(total,2)
    print(f"please pay ${total}")
total_calc(150,20)