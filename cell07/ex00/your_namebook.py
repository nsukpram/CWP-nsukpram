def array_of_names(a) :
    result = []
    for firstn,lastn in a.items() :
        Full_name = f"{firstn.capitalize()} {lastn.capitalize()}"
        result.append(Full_name)
    return result

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))