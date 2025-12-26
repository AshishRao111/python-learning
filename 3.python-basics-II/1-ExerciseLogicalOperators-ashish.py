is_magician = False
is_expert = True

# check if magician And expert: "you are a master magician"
if is_magician and is_expert:
    print("you are a master magician")
# check if magician but not expert: "atleast you're getting there"
if is_magician and not is_expert:
    print("atleast you're getting there")
# if you are not a magician: "you need magic powers"
if not is_magician:
    print("you need magic powers")
