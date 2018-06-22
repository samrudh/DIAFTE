from .mt103_new import MT103

def get_updated_dataframe(df):
    df['Message Text'] = df['Message Text'].apply(lambda x: MT103(x).get_all_fields())
    new_df = df['Message Text'].apply(pd.Series)
    return pd.concat([df,new_df],axis=1)

