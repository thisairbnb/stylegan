def convert(st):
    if not st.endswith(" "): st = "%s " % st
    keys = ["d", "h", "m", "s"]
    nums = [0,0,0,0]
    for i, key in enumerate(keys):
        r = st.split("%s "%key)

        if len(r) > 1:
            x, st = r
            nums[i] = int(x)
        else:
            st = r[0]
    return nums[0] * 3600 * 24 + nums[1] * 3600 + nums[2] * 60 + nums[3]

def parse_line(l):
    if "time" in l:
        _, d = l.split("time ")
        r = d.split(" sec")
        d = r[0]
    else:
        d = x
    return d

import sys
if __name__ == "__main__":
    x = sys.argv[1]
    for line in open(x):
        d = parse_line(line.strip())
        print(convert(d)) 
