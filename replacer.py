# replacer texts with python

# requires: pip install aspose-words

#import api
import aspose.words as aw

# load Word document
doc = aw.Document("pdf-to-word.docx")

# replace text
doc.range.replace("MR", "Anel Magico", aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

# save the modified document
doc.save("updated.docx")