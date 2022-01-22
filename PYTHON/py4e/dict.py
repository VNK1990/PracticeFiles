dict_name = dict()
name = 'ffasdhkahfhgcubasdnhubkfnknbafnksncbundNIAHNASDHIHDASNHIFHIASofweoijiwhdiojoqdjojaodjoasjdasjdoh8hfiwefishifhsdi'
for word in name:
    dict_name[word] = dict_name.get(word,0) + 1 ;
for word in dict_name:
    print(word,dict_name[word])
