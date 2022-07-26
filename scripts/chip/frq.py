hu_d = {}
cn_d = {}
swa_d = {}
afr_d = {}
eur_d = {}
hu_ale_d = {}
fo = open('final.sites1.frq', 'w')
with open('HU.frq') as hu, open('CN.frq') as cn, open('SWA.frq') as swa, open('AFR.frq') as afr, open('EUR.frq') as eur:
    for line in hu:
        if line.startswith(' CHR'):
            continue
        else:
            lines = line.strip().split()
            name = lines[1]
            allele = lines[2]
            maf = lines[4]
            hu_ale_d[name] = allele
            hu_d[name] = maf

    for lin in cn:
        if lin.startswith(' CHR'):
            continue
        else:
            lins = lin.strip().split()
            if hu_ale_d.get(lins[1], '') == lins[2]:
                cn_d[lins[1]] = float(lins[4])
            else:
                cn_d[lins[1]] = 1 - float(lins[4])
    for lin in swa:
        if lin.startswith(' CHR'):
            continue
        else:
            lins = lin.strip().split()
            if hu_ale_d.get(lins[1], '') == lins[2]:
                swa_d[lins[1]] = float(lins[4])
            else:
                swa_d[lins[1]] = 1 - float(lins[4])
    for lin in afr:
        if lin.startswith(' CHR'):
            continue
        else:
            lins = lin.strip().split()
            if hu_ale_d.get(lins[1], '') == lins[2]:
                afr_d[lins[1]] = float(lins[4])
            else:
                afr_d[lins[1]] = 1 - float(lins[4])
    for lin in eur:
        if lin.startswith(' CHR'):
            continue
        else:
            lins = lin.strip().split()
            if hu_ale_d.get(lins[1], '') == lins[2]:
                eur_d[lins[1]] = float(lins[4])
            else:
                eur_d[lins[1]] = 1 - float(lins[4])
                
fo.write('SNP' + '\t' + 'HU' + '\t' + 'CN' + '\t' +'SWA' + '\t' + 'AFR' + '\t' + 'EUR' + '\n')    
for k in hu_d:
    l = [k, str(hu_d[k]), str(cn_d[k]), str(swa_d[k]), str(afr_d[k]), str(eur_d[k])]
    fo.write('\t'.join(l) + '\n')
