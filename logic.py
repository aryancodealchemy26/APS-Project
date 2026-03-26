# We use a Dictionary to store weights. 
# This makes it easy to add 'Semi-Urban' later!
LOCATION_WEIGHTS = {
    "Urban": 0,
    "Rural": 15,
    "Semi-Urban": 7
}

def get_readiness_score(prof_level, area_type):
    # Base calculation
    base_sc = prof_level * 20
    
    # We 'Look up' the weight from our dictionary
    # .get() is safer than ['key'] because it won't crash if the key is missing
    weight = LOCATION_WEIGHTS.get(area_type, 0)
    
    final_sc = base_sc + weight
    
    # Clamping logic (Ensuring valid range)
    return min(final_sc, 100)

# def get_readiness_score(prof_level, area_type):
#     """
#     prof_level: A number from 1 to 5 (from your survey data)
#     area_type: String "Urban" or "Rural"
#     """
    
#     # ct = current total (starting base)
#     # We multiply by 20 to turn a 1-5 scale into a 0-100 scale
#     ct = prof_level * 20
    
#     # Engineering Concept: 'Contextual Weighting'
#     # If a teacher is Rural, we give a 'bonus' because their 
#     # effort to use tech is higher due to infrastructure gaps.
#     if area_type == "Rural":
#         final_score = ct + 15
#     else:
#         final_score = ct
        
#     # 'Clamping' Logic: Ensure score never goes above 100
#     if final_score > 100:
#         final_score = 100
        
#     return final_score

def get_category(score):
    # Logic to give a professional label based on the score
    if score >= 80:
        return "AI Innovator"
    elif score >= 50:
        return "Emerging Explorer"
    else:
        return "AI Curious"