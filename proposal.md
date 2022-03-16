### Greek Vase Proposal

#### Question/need:

**What is the framing question of your analysis, or the purpose of the model/system you plan to build?**

I plan to build a model that will predict the date and provenance of ancient greek pottery. If this is too difficult, I will instead aim to predict the style and coloring of the pottery. 

**Who benefits from exploring this question or building this model/system?**

This would be useful to archaeologists who wanted to get a quick view as to the possible date or provenance of a shard of ancient greek pottery.

#### Data Description:

**What dataset(s) do you plan to use, and how will you obtain the data?**

I plan to use the Beazley Archive Pottery Database. I will scrape the pottery images from the database and use the provided metadata as targets.

**What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?**

I expect to work with images of shards of pottery. The individual prediction would be (image of shard of vase or whole vase) -> (vase date, vase provenance).
 
**If modeling, what will you predict as your target?**

See above.

#### Tools:

**How do you intend to meet the tools requirement of the project?**

I plan to use the Keras API of Tensorflow to train the machine learning model. I will also probably use a library like pillow or opencv to resize and preprocess the images.
 
**Are you planning in advance to need or use additional tools beyond those required?**

I don't know whether other tools will be required.

#### MVP Goal

**What would a [minimum viable product (MVP)](./mvp.md) look like for this project?**

The minimum viable product would be a machine learning model that can predict some feature of ancient greek pots, using pictures of the pods and / or pictures of the shards of the pots with some level of accuracy.
