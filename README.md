# Artificial Intelligence

Lab work and practical implementations for the Artificial Intelligence (CMPG 313) module at North-West University. Each lab folder is a self-contained exercise exploring a different core AI concept, from classical search algorithms to clustering and modern language models.

## Repository Structure

```
Artifial-Intelligence
Lab1    # Computer vision basics (image & video processing)
Lab2    # K-Means clustering
Lab3    # ELIZA chatbot vs. modern LLM comparison
Lab4    # Uninformed search (BFS, DFS, IDDFS)
Lab5     # Informed search (A*)
```

## Labs

### Lab 1 - Computer Vision Basics
Introductory work with image and video input using OpenCV, including still-image processing and webcam/video capture tests.
- `lab_1.py` - main script
- Sample media: market and road-traffic images, webcam test footage

### Lab 2 - K-Means Clustering
Applies K-Means clustering to network/point data at different values of *k* (k=3 and k=7), visualising cluster assignments and surface smoothing.
- `kmeans.py` - main script
- Output visualisations comparing clustered networks and smoothed surfaces across k=3 and k=7

### Lab 3 - ELIZA vs. Modern LLM Comparison
Implements the classic ELIZA chatbot and compares its rule-based responses against a modern LLM on the same set of prompts, evaluating differences in conversational quality.
- `eliza.py` - rule-based ELIZA implementation
- `LLM.py` - modern LLM query script
- `chat_comparison.py` - side-by-side comparison logic
- Output screenshots of ELIZA and LLM test prompts, plus comparison experiment results

### Lab 4 - Uninformed Search
Implements and compares uninformed search strategies over a graph/road-network problem.
- `bfs.py` - Breadth-First Search
- `dfs.py` - Depth-First Search
- `id-dfs.py` - Iterative Deepening DFS
- `uninformed_test.py` - test harness comparing all three algorithms
- `Figure_1.png` - output/result visualisation

### Lab 5 - Informed Search (A*)
Extends the search problem from Lab 4 with A*, an informed search algorithm using heuristics to find optimal paths more efficiently.
- `A_star_search.py` - A* implementation
- `A_star_search_testcase.py` - test cases validating the algorithm
= `Output.png`  result visualisation

## Tech Stack
- **Language:** Python 3
- **Libraries used across labs:** OpenCV (image/video), scikit-learn (K-Means), standard Python data structures for search algorithms

