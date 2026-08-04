# Keyword arbitrary argument
# keyword arg =info(name="monika", age=18, hobby="playing")
def info_person(**kwargs):
    #dict. (key and value )
    for k,v in kwargs.items():
        print(k,v)
info_person(name="mona",age=35,department="computer")
info_person(name="senorita",age=25,)
info_person(name="rita",department="sci")