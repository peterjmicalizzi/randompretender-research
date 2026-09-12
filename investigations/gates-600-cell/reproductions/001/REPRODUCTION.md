# Reproduction: 2I word enumeration by matrix closure

Record ID: `rp:execution:2i-words-matrix-closure:001`
Reproduces: `rp:execution:2i-words:001` at commit `7ee2ee0ed85c84a716a8b9b7da72cf19186f6774`

## What was reproduced

The starter experiment lists 120 coordinates in Q(√5), multiplies them as quaternions,
checks closure over all 14,400 ordered products, and finds shortest words in the alphabet
`a, A, b, B` by breadth-first search. Its result is `experiments/result.json`.

This reproduction reaches the same result by a different construction, working from
`BRIEF.md` and `result.json` only:

- The group is built as the **closure of the two generators** under multiplication, not
  from a coordinate list. The closure has exactly 120 elements, is closed under inverse
  and under all 14,400 products, and every element has determinant 1.
- The operation is **2×2 complex matrix multiplication** over Q(√5)(i), using the
  correspondence stated in the brief, `a+bi+cj+dk → [[a+bi, c+di], [−c+di, a−bi]]`.
- The brief asks for that correspondence to be verified. It is a **homomorphism on all
  14,400 ordered pairs** when compared against a Hamilton product written from the
  textbook formula, independently of the starter's helper.
- The closure **equals the recorded coordinate set** under that map. The record keeps
  `q` and `−q` distinct, as the brief's SU(2) convention requires.
- Shortest words by breadth-first search over right multiplication give the **identical
  histogram** `{0:1, 1:4, 2:12, 3:25, 4:24, 5:24, 6:18, 7:10, 8:2}` with maximum length 8.
  Every recorded shortest word **replays in matrices to its recorded endpoint**, and every
  recorded word **is minimal** for its endpoint.
- The recorded collision `aA = identity` holds.

Sixteen checks, all passed. The script, its JSON report and the execution record are in
this directory, `investigations/gates-600-cell/reproductions/001/`. Replaying the starter
script itself also reproduces `result.json` exactly.

## What was not checked

- Whether the chosen generators or conventions are the *right* ones for any physical or
  circuit interpretation. The brief is explicit that it does not claim this either.
- Any correspondence to the website's vertex numbering. None is claimed by the brief and
  none is established here.
- Any statement about golden gates, Clifford+T, or hardware cost. The reproduction covers
  the finite calculation as recorded, nothing beyond it.

## Shared dependencies

A reviewer weighing this reproduction should know what the two runs have in common:

- Both rely on exact `Fraction` arithmetic in Q(√5). A defect in that shared assumption
  would not be caught.
- The generators, the coordinate encoding and the multiplication convention are read from
  the brief and the record. An error in those definitions would be shared, not detected.
- The brief's matrix correspondence is taken as the definition of the matrix side and then
  checked to be a homomorphism; it is not derived independently.
- **Separately implemented using matrix multiplication and generator closure, with
  different AI tools under the same human direction.** The starter was prepared with
  Codex (GPT-6); this reproduction with Claude Fable 5.1. Different tools do not
  establish independent reasoning or uncorrelated errors. The shared definitions and
  arithmetic dependencies are the items above. External reproduction remains open: a
  reproduction by someone outside the project is the task the brief lists, and this
  record does not close it.

## Environment

Python 3.13.3, CPython, Windows, AMD64, standard library only. Runtime about 3.5 seconds.

One footnote for anyone replaying either script on Windows: output redirected from
`python … > file` gains CRLF line endings, and the raw file hash differs from the recorded
one until the line endings are normalised to LF. The recorded hashes are of LF output.
The JSON content is identical either way.

## Attribution

Reproduction prepared with Claude Fable 5.1 under the direction of Peter Micalizzi, who
also directed the starter. No independent human reviewer is attached. Inclusion in the
library records that this comparison was made; it does not certify the mathematics.
