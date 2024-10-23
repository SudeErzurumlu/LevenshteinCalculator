import numpy as np

class LevenshteinCalculator:
    def __init__(self, deletion_cost=1, insertion_cost=1, substitution_cost=1):
        self.deletion_cost = deletion_cost
        self.insertion_cost = insertion_cost
        self.substitution_cost = substitution_cost

    def calculate(self, A, B):
        A_len, B_len = len(A), len(B)
        dp = np.zeros((A_len + 1, B_len + 1))

        for i in range(A_len + 1):
            dp[i][0] = i * self.deletion_cost
        for j in range(B_len + 1):
            dp[0][j] = j * self.insertion_cost

        for i in range(1, A_len + 1):
            for j in range(1, B_len + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    deletion = dp[i - 1][j] + self.deletion_cost
                    insertion = dp[i][j - 1] + self.insertion_cost
                    substitution = dp[i - 1][j - 1] + self.substitution_cost
                    dp[i][j] = min(deletion, insertion, substitution)

        return dp[A_len, B_len]

    def similarity_ratio(self, A, B):
        max_len = max(len(A), len(B))
        distance = self.calculate(A, B)
        return (max_len - distance) / max_len

    def detailed_comparison(self, A, B):
        distance = self.calculate(A, B)
        ratio = self.similarity_ratio(A, B)
        return {
            "Levenshtein Distance": distance,
            "Similarity Ratio": ratio,
            "Details": {
                "String 1 Length": len(A),
                "String 2 Length": len(B),
                "Max Length": max(len(A), len(B)),
                "Distance with Costs": {
                    "Deletion Cost": self.deletion_cost,
                    "Insertion Cost": self.insertion_cost,
                    "Substitution Cost": self.substitution_cost
                }
            }
        }

if __name__ == "__main__":
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    # Instance of LevenshteinCalculator with custom costs
    calculator = LevenshteinCalculator(deletion_cost=1, insertion_cost=1, substitution_cost=2)

    # Get the detailed comparison between the words
    result = calculator.detailed_comparison(word1, word2)

    print(f"Levenshtein Distance: {result['Levenshtein Distance']}")
    print(f"Similarity Ratio: {result['Similarity Ratio']:.2f}")
    print("Comparison Details:")
    for key, value in result['Details'].items():
        print(f"  {key}: {value}")
