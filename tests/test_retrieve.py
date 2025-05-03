import json
import math
import os
import random
import re
import shutil
import sys
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import numpy as np

import requests
from loguru import logger

url = "http://localhost:9441/retrieve"
logger.add(Path(__file__).with_suffix('.log'), mode='w', encoding='utf-8', level='DEBUG')

def main():
    """Test the retrieval system.

    class QueryRequest(BaseModel):
        queries: List[str]
        topk: Optional[int] = None
        return_scores: bool = False
    """
    queries = [
        "total number of death row inmates in the us?",
        'Who wrote "To Kill a Mockingbird"?',
        "What is the largest planet in our solar system?",
    ]
    topk = 3
    return_scores = True
    payload = {"queries": queries, "topk": topk, "return_scores": return_scores}
    # Send the request to the server
    response = requests.post(url, json=payload, timeout=60)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # logger.info the results
        with open("tests/retrieval_results.json", "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        for query, results in zip(queries, data["result"]):
            logger.info(f"Query: {query}")
            for result in results:
                logger.info(f"  - {result['document']['contents']} (score: {result['score']})")
    else:
        logger.info(f"Error: {response.status_code} - {response.text}")
    logger.info("end")


if __name__ == "__main__":
    main()
