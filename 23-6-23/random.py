families={
    'praneeth':
    {
        'abhi':{'pan','abhina'},
        'jhonny':{'loya','lavvau'}
    },
    'ajay':
    {
        'rahul':{'sone','rome'},
        'mai':{'iron','man'}
    },
    'nithin':
    {
        'privijth':{'poorna','liya'},
        'shiva':{'chadhu','avi'}}
    }
for parent,children in families.items():
    print(f"{parent} has {len(children)} kid(s):")
    print(f"{', and '.join([str(child) for child in [*children]])}")