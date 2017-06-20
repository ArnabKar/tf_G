import tensorflow as tf
import numpy as np
from src.graph.graph_constructor import GraphConstructor
from src.pagerank.numeric_algebraic_pagerank import NumericAlgebraicPageRank
from src.pagerank.numeric_iterative_pagerank import NumericIterativePageRank
from src.utils.datasets import DataSets


def main():
    beta = 0.85
    convergence = 0.001

    wiki_vote_edges_np = DataSets.wiki_vote()
    followers_edges_np = DataSets.followers()

    with tf.Session() as sess:
        writer = tf.summary.FileWriter('logs/.')

        g_followers = GraphConstructor.empty(sess, "Gfollowers",
                                                  7, writer)
        pr_followers = NumericIterativePageRank(sess, "PRfollowers",
                                                g_followers, beta)

        for r in followers_edges_np:
            g_followers.append(r[0],r[1])
        print(g_followers)
        print(pr_followers.ranks(convergence=convergence))
        '''
        # gs_followers = g_followers.sparsifier(alpha=0.9)

        print(GraphConstructor.unweighted_random(sess, "GRandom", 10 ** 2,
                                                 10 ** 3, writer=writer))
     
        g_wiki_vote = Graph(sess, "Gwikivote", edges_np=wiki_vote_edges_np,
                            writer=writer)
        pr_wiki_vote = NumericIterativePageRank(sess, "PRwikivote",
                                                g_wiki_vote, beta)
        print(g_wiki_vote)
        print(pr_wiki_vote.ranks(convergence=convergence))
        '''

        writer.add_graph(sess.graph)


if __name__ == '__main__':
    main()
