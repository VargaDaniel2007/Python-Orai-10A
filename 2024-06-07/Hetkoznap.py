hetkoznap = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']

maganhangzok = ['a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű']


stat = dict()
for h in hetkoznap:
    for b in h:
        if b in maganhangzok:
            if h in stat.keys():
                stat[h] += 1
            else:
                stat[h] = 1

legtobb = hetkoznap[0]
for h in hetkoznap[1:]:
    if stat[h] > stat[legtobb]:
        legtobb = h

print(f'A legtöbb magánhangzó a {legtobb}-ben van!')