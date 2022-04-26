

# def do_it(a,b, *args):
#     print(a,b, args)

def do_it(a,b=8,c=9, *args, **kwargs):
    print(a,b,c, args, kwargs)

do_it(1,c=2,d=7,e=2)