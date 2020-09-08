# A collection of Topic Diversity measures for topic modeling.
Here I collected and implemented most of the known topic diversity measures used for measuring how different topics are.
The more diverse the resulting topics are, the higher will be the coverage of the various aspects of the analyzed corpus. It is therefore important to also obtain topics that are different from each other (rather than just considering how much coherent the topics are).

List of the currently implemented metrics:
* Proportion of unique words (PUW) [Dieng et al., 2020](#puw):
* average Pairwise Jaccard Distance (JD)[Tran et al., 2013](#jd):
* Inverted Rank-Biased Overlap (IRBO):
* Word Embedding-based Centroid Distance (WE-CD):
* Word Embedding-based Pairwise Distance (WE-PD):
* Word Embedding-based Inverted Rank-Biased Overlap (WE-IRBO):


## References:
<h3 id="puw">Adji Bousso Dieng, Francisco J. R. Ruiz, and David M.Blei. 2020. Topic modeling in embedding spaces.Trans. Assoc. Comput. Linguistics, 8:439–453. </h3>
<h3 id="jd">Nam Khanh Tran, Sergej Zerr, Kerstin Bischoff, Claudia Niederée, Ralf Krestel:
Topic Cropping: Leveraging Latent Topics for the Analysis of Small Corpora. TPDL 2013: 297-308</h3>
