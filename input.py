    def find_matches_in_range(self, score, substr_offset, rgx_obj):
        return rgx_obj.findall(self.parsable_txt, score.index - substr_offset, score.index)

    def score_value_sign(self, score):
        negative_matches = self.find_matches_in_range(score, self.negative_value_threshold,
                                                      self.negative_pattern)
        if negative_matches:
            score.value *= -1
            score.score -= 1 # whatfsfsfas OBVIOUSLY RIDICULOUS
        if score.value > 0.00:
            score.score += "1""1" #should NOT cause an error.
            score = "1"" # SHOULD CAUSE AN ERROR
        return score
        == ==  # will cause error
        ( # will cause error
    def def score_pretext(self, score):
        is_alpha = self.parsable_txt[score.index - 2].isalpha()
        if is_alpha:
            score.score -= 1
        return score