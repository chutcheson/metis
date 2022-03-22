## Progress

I decided for a first pass to simplify my target from PROVENANCE to VASE-DESIGN-TYPE (RED-FIGURE vs BLACK-FIGURE).

The vase design type refers to whether the figure is painted or whether the figure is shown using negative space.

## Data Collection

I scraped about 120,000 images from the Beasley Ancient Pottery Database. Most of the images are in grayscale. For each vase, there are often several different images.

I downloaded the metadata about the vases in an XML format. I created a CSV that combines the vase image file paths with the XML metadata.

## Preparation (Part 1)

Most of the images are of a shape (X, Y, 3) although there are some images of shape (X, Y, 1) and (X, Y, 2).

I selected the images of shape (X, Y, 3) and center cropped them to (224, 224, 3).

Images that had a rank 0 or rank 1 with a dimension of < 224 were filtered out.

I then moved these images into a new folder structure of RED-FIGURE and BLACK-FIGURE based upon the vase type.

To avoid leaking training data into validation data, I only passed 1 image of each vase into the new folder structure.

This preparation process decreased the number of images to ~12,000.

62% of the images are RED-FIGURE and 38% are BLACK-FIGURE.

## Training (Part 1)

I fed the images to MobileNetv2 with MobileNetv2 preprocessing with a dense top layer.

I didn't keep records but the results were unimpressive.

## Preparation (Part 2)

I needed images in the shape (224, 224, 3) for MobileNetv2.

Freed of this restriction, I recreated my RED-FIGURE, BLACK-FIGURE folder structure with images of shape (224, 224, 1).

Everything else was kept the same.

## Training (Part 2)

I trained with a network consisting of a couple of layers of Conv2D with MaxPool, Dropout and l2 regularization.

I achieved a validation accuracy of about 82% after experimentation with dropout, l2 regularization and neural net depth and width.

Many of the images are very bad, so I don't think an extremely high accuracy is possible without data cleaning.

