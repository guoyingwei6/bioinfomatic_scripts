import click

def p_list(list):
    f=open(list,'r')
    list_data={}
    for line in f:  
        line=line.strip().split()
        for ll in line:	
            if str(int(float(ll)/5.0)*5)+"-"+str(int((float(ll)/5.0)+1)*5) in list_data :
                list_data[str(int(float(ll)/5.0)*5)+"-"+str(int((float(ll)/5.0)+1)*5)] += 1
            else:
                list_data[str(int(float(ll)/5.0)*5)+"-"+str(int((float(ll)/5.0)+1)*5)] = 1
    return list_data

@click.command()
@click.argument('list_file')
@click.argument('outfile')
def tmp(list_file,outfile):
    ff=open(outfile,'w+')
    for key,value in p_list(list_file).items():
        ff.write(str(key)+"\t"+str(value)+"\n")


if __name__ == '__main__':
    tmp()
