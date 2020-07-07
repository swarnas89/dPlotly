from home.Semantic_Similarity.WikiLink_Measure.Wiki import wikisim
from home.Semantic_Similarity.Word_Embedding.IMsim import calculate_similarity
from home.getdata import concatTitleAndAbstract

def getSimilarityScores():

    s = concatTitleAndAbstract()[0]

    t = concatTitleAndAbstract()[1]

    sim_scores = calculate_similarity(s, t)

# sim_scores = wikisim(s,t)
# This method uses wikipeida API and will take a longer time to compute, not recommended


    print(sim_scores)
    return sim_scores

