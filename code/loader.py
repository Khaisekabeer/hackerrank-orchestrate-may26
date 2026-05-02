import os
from pathlib import Path

def extract_product_area(path):
    parts = Path(path).parts

   
    if len(parts) >= 3:
        return parts[2]  

    return "general"

def load_docs():
    docs =[]

    for company in ["claude","hackerrank","visa"]:
         base = f"data/{company}"


         for root, _,files in os.walk(base):
              for file in files:
                   if file.endswith(".md") and file not in ["index.md", "support.md"]:
                        path = os.path.join(root,file)

                        with open(path,"r", encoding ="utf-8") as f:
                             content = f.read()
                        product_area = extract_product_area(path)
                        docs.append({
                             "company":company,
                             "text" :content,
                             "path":path,
                             "product_area":product_area
                        })
    print(f"Loaded {len(docs)} documnets")
    return docs
                   
