v1 = [float(a) for a in version1.split('.')]
        v2 = [float(a) for a in version2.split('.')]
        i = 0
        while i < len(v1) or i < len(v2):
            if i >= len(v1):
                v1.append(0)
            if i >= len(v2):
                v2.append(0)
            if v1[i] < v2[i]:
                return -1
            if v1[i] > v2[i]:
                return 1
            i += 1
        return 0