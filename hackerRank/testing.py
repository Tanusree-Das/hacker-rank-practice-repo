#import antigravity

if __name__=="__main__":
    dict_for_testing={'sep':'= '}
    list_for_testing=['tanusree das','dipesh singh','motababy das']
    print(*list_for_testing,**dict_for_testing)
    a=19
    b=19
    print(id(a),id(b))

    c='uiui'
    d='uiui'
    print(id(c),id(d))

    string_list_of_numbers=['1','2','3']
    print('old list->',string_list_of_numbers)
    new_lambda_function=map(lambda n:int(n),string_list_of_numbers)
    print('converted list->',list(new_lambda_function))