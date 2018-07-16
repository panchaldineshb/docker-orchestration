from pymongo import MongoClient
from random import randint

#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.sarabi

#Step 2: Create sample data
for x in xrange(429, 501):

        product_id =  13860429 + x
        value = 45.78 + randint(1, 5)

        #Step 3: Insert business object directly into MongoDB via isnert_one
        product_doc = {                                   # Creating Json dynamically / aggregating it for response
            'product_id': product_id,
            'current_price': {
                'currency_code': 'USD',
                'value': value
            }
        }

        result = db.product.insert_one(product_doc)

        #Step 4: Print to the console the ObjectID of the new document
        print('Created {0} of 100 as {1}'.format(x,result.inserted_id))

#Step 5: Tell us that you are done
print('finished creating 100 product')
