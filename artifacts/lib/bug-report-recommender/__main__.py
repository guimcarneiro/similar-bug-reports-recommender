import pymongo
from recommender import SimilarBugReportsRecommendationSystem;
from data_loader import DataLoader;

TEST_DATABASE = 'dump_test_br'
TEST_DATABASE_HOST = 'localhost'
PORT = 27017

K = 10

def get_mongo_conn(MONGO_URL, MONGO_DATABASE):
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DATABASE]
    return db

def retrieve_sample_bug_report(db):
    x = db["bug"].find_one({
        "sample_set": True
    }, {
        "bg_number"     : True,
        "summary"       : True,
        "description"   : True,
        "product"       : True,
        "component"     : True,
        "platform"      : True,
        "type"          : True,
        "creation_time" : True,
        "assigned_to"   : True,
    })

    return x

# Demonstrating the use the recommender as lib

def main():
    db = get_mongo_conn(MONGO_URL=TEST_DATABASE_HOST, MONGO_DATABASE=TEST_DATABASE)

    data_loader = DataLoader(database=TEST_DATABASE, host=TEST_DATABASE_HOST, port=PORT)

    recommender = SimilarBugReportsRecommendationSystem(data_loader=data_loader);

    print('-'*50)

    example = retrieve_sample_bug_report(db)

    print('Querying the following input:')
    print(f'[INPUT] id={example["bg_number"]}, summary={example["summary"]}')

    print('-'*50)

    print('requesting recommendations...')
    results = recommender.get_recommendations(
        query=example,
        K=K
    )

    print('RESULTS:')
    for i, result in enumerate(results):
        print(f'[{i+1}] id={result["item"]["bg_number"]} - score={result["score"]} : summary={result["item"]["summary"]}')
        print('-'*50)

if __name__ == '__main__':
    main()
