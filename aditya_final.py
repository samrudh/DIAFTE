"""
Author: Aditya Kumar
Email: aditya1@dbs.com
Description:
Project: DIAFTE-master 2
Date Created: 6/23/18 6:18 AM
"""
import pandas as pd
import codecs
import re
import numpy as np
from cleanco import cleanco
from fuzzywuzzy import fuzz
watch_list = '/Users/aditya1/Downloads/DIAFTE-master 2/data/CSSol-2/WatchListEntries.csv'

df_person = pd.DataFrame()
df_org = pd.DataFrame()


def entity_parse():
    with codecs.open(watch_list, 'r', encoding='utf-16') as f:
        lines = f.read().splitlines()
        lines = list(map(lambda x: x.split('|'), lines))
        person_lines = [i for i in lines if i[0] == 'PERSON']
        # print(person_lines)
        org_lines = [i for i in lines if i[0] == 'ORGANIZATION']
        cols = ['ENTRY_TYPE', 'ENTRY_FIRST_NAME', 'ENTRY_MIDDLE_NAME', 'ENTRY_LAST_NAME', 'ENTRY_FULL_NAME', 'DECEASED', \
               'DECEASED_DATE', 'GENDER', 'ID_SET', 'NATIONALITY_COUNTRY_SET', 'DATE_OF_BIRTH_SET', 'PLACE_OF_BIRTH_SET', 'CATEGORY_SET', 'ALIAS_SET', 'ADDRESS_SET', 'CITIZENSHIP', 'AGE']
        df_person = pd.DataFrame(person_lines, columns=cols)
        df_org = pd.DataFrame(org_lines, columns=cols)
        print(df_person.shape)
        print(df_org.shape)
        return df_person, df_org


def clean_beneficiary(x):
    return re.sub('[\n\r]+', ' ', re.sub('/[X]*[\n\r]*', '', x))


def get_score(check, word_dict):
    try:
        check = check.split()
        check = [i for i in check if len(i) > 4]
        if len(check) >= 4:
            check = check[:4]
        score = []
        for w in check:
            try:
                for i in word_dict[w[0]]:
                    aa = fuzz.token_sort_ratio(w, i)
                    score.append(aa)
                    if aa > 60:
                        break
                    # score.append(max([fuzz.token_sort_ratio(w, i) for i in word_dict[w[0]]]))
            except:
                score.append(0)
                continue
        return np.mean(score)
    except:
        return 0


def main(train_df):
    df_person, df_org = entity_parse()
    xx = list(df_person.ENTRY_FULL_NAME.unique())
    yy = list(df_org.ENTRY_FULL_NAME.unique())
    tokens = []
    for i in xx:
        dd = i.split()
        for d in dd:
            tokens.append(d)
    tokens = list(set(tokens))
    final_tokens = [i for i in tokens if len(i) > 4]

    o_tokens = []
    for i in yy:
        dd = i.split()
        for d in dd:
            o_tokens.append(d)
    o_tokens = list(set(o_tokens))
    o_final_tokens = [i for i in o_tokens if len(i) > 4]

    word_dict = {}
    final_tokens = [i.lower() for i in final_tokens]

    o_word_dict = {}
    o_final_tokens = [i.lower() for i in o_final_tokens]

    final_tokens = [re.sub('[^a-z]', '', i) for i in final_tokens]
    o_final_tokens = [re.sub('[^a-z]', '', i) for i in o_final_tokens]
    for i in final_tokens:
        if i:
            try:
                word_dict[i[0]].append(i)
            except:
                word_dict[i[0]] = [i]
    for i in o_final_tokens:
        if i:
            try:
                o_word_dict[i[0]].append(i)
            except:
                o_word_dict[i[0]] = [i]
    # train_df = pd.read_csv('/Users/aditya1/Downloads/DIAFTE-master 2/updated_test.csv')
    train_df.clean_beneficiary = train_df.clean_beneficiary.apply(lambda x: str(x).lower())
    train_df = train_df[train_df.AlertStatus != 'PASS']
    train_df['pscore'] = train_df.clean_beneficiary.apply(lambda x: get_score(x, word_dict))
    train_df['oscore'] = train_df.clean_beneficiary.apply(lambda x: get_score(x, o_word_dict))
    return train_df


if __name__ == '__main__':
    train_path = '/Users/aditya1/Downloads/DIAFTE-master 2/data/CSSol-2/NewData/whole_train_new.csv'
    test_path = '/Users/aditya1/Downloads/DIAFTE-master 2/data/CSSol-2/NewData/whole_test_new.csv'

    test_df = pd.read_csv(test_path)
    train_df = pd.read_csv(train_path)

    # If don't want to reset index
    train_df = train_df[train_df.columns[1:]]
    test_df = test_df[test_df.columns[1:]]

    train_df['clean_beneficiary'] = train_df.beneficiary.apply(lambda x: clean_beneficiary(str(x)))
    test_df['clean_beneficiary'] = test_df.beneficiary.apply(lambda x: clean_beneficiary(str(x)))

    train_df['clean_beneficiary'] = train_df.clean_beneficiary.apply(lambda x: cleanco(str(x)).clean_name())
    test_df['clean_beneficiary'] = test_df.clean_beneficiary.apply(lambda x: cleanco(str(x)).clean_name())
    train_df = main(train_df)
    print(train_df)
    # test_df = main(test_df)
    # train_df.to_csv('updated_train_new.csv', index=False)
    # test_df.to_csv('updated_test_new.csv', index=False)
