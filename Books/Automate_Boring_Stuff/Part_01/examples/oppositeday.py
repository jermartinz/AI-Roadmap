today_is_opposite_day = True

if today_is_opposite_day:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

if today_is_opposite_day:
    say_it_is_opposite_day = not say_it_is_opposite_day

if say_it_is_opposite_day:
    print("Today is Opposite Day.")
else:
    print("Today is not Opposite Day.")
