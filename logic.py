def get_readiness_score(prof_level, area_type):
    """
    prof_level: A number from 1 to 5 (from your survey data)
    area_type: String "Urban" or "Rural"
    """
    
    # ct = current total (starting base)
    # We multiply by 20 to turn a 1-5 scale into a 0-100 scale
    ct = prof_level * 20
    
    # Engineering Concept: 'Contextual Weighting'
    # If a teacher is Rural, we give a 'bonus' because their 
    # effort to use tech is higher due to infrastructure gaps.
    if area_type == "Rural":
        final_score = ct + 15
    else:
        final_score = ct
        
    # 'Clamping' Logic: Ensure score never goes above 100
    if final_score > 100:
        final_score = 100
        
    return final_score

def get_category(score):
    # Logic to give a professional label based on the score
    if score >= 80:
        return "AI Innovator"
    elif score >= 50:
        return "Emerging Explorer"
    else:
        return "AI Curious"