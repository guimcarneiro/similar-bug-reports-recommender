import pymongo

import dateutil

from utils import deconvert_from_binary

class MongoDataLoader():
    def __init__(self, database='', host='', port=27017):
        DATABASE_URL = f"mongodb://{host}:{port}/"

        print(f'starting connection with database at: {DATABASE_URL}{database}')
        self.client = pymongo.MongoClient(DATABASE_URL)
        self.bugs = self.client[database]["bug"]

    def __to_final_format(self, db_bug_report):
        return {
            "bg_number"       : str(db_bug_report["bg_number"]),
            "summary"         : db_bug_report["summary"],
            "description"     : db_bug_report["description"],
            "product"         : db_bug_report["product"],
            "component"       : db_bug_report["component"],
            "platform"        : db_bug_report["platform"],
            "type"            : db_bug_report["type"],
            "tfidf_vector"    : deconvert_from_binary(db_bug_report["tfidf_vector"]),
            "bert_embeddings" : deconvert_from_binary(db_bug_report["embeddings_vector"]),
            "creation_time"   : db_bug_report["creation_time"],
            "assigned_to"     : db_bug_report["assigned_to"],

            #debug
            "when_changed_to_resolved" : db_bug_report["when_changed_to_resolved"]
        }

    # recupera bug reports em que o horário de resolução é maior que a data de criação da query, e que possuem vetores atribuidos
    def retrieve_open_reports(self, extra_filters={}):
        search_filter = {
            "tfidf_vector": {
                "$exists": True
            },
            "embeddings_vector": {
                "$exists": True
            }
        }

        if extra_filters:
            for k in extra_filters.keys():
                search_filter[k] = extra_filters[k]

        res = self.bugs.find(search_filter)

        return [ self.__to_final_format(br) for br in res ]

def parse_iso_date(str_date):
        return dateutil.parser.parse(str_date)

if __name__ == "__main__":
    x = MongoDataLoader(database="bug_reports_db", host="localhost")

    test = x.retrieve_open_reports(
        extra_filters={
            "when_changed_to_resolved": { "$gt": parse_iso_date("2010-01-27T01:30:16Z") }
        }
    )

    for t in test[:10]:
        print(f'id: {t["bg_number"]}, summary: {t["summary"]}, assigned_to: {t["assigned_to"]}, date: {t["creation_time"]}')
        
        


