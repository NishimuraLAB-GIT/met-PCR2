def classification(sequence, C_index):
    ret = ["CG","CHG","CHH"]
    if sequence[C_index+1] == "G":
        return ret[0]
    elif sequence[C_index+2] == "G":
        return ret[1]
    else:
        return ret[2]