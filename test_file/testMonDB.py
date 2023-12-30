const { MongoClient } = require('mongodb');
const uri = "mongodb://username:password@host:port";
const client = new MongoClient(uri);

async function run() {
    try {
        await client.connect();
        const database = client.db('myWMS');
        const bol = database.collection('bol');
        const item = database.collection('item');

        // Create
        const newBol = { bol_info: "BOL Information" };
        const bolResult = await bol.insertOne(newBol);
        const newItem = { item_info: "Item Information", bol_id: bolResult.insertedId };
        await item.insertOne(newItem);

        // Read
        const query = { bol_info: "BOL Information" };
        const bolData = await bol.findOne(query);

        // Update
        const updateDoc = { $set: { bol_info: "Updated BOL Information" }};
        await bol.updateOne(query, updateDoc);

        // Delete
        await bol.deleteOne(query);
    } finally {
        await client.close();
    }
}
run().catch(console.dir);
