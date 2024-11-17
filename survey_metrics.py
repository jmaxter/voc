# metrics.py

def normalize_nps(nps_score):
    """
    Normalize NPS from the range [-100, 100] to [0, 100].
    """
    return (nps_score + 100) / 2

def normalize_csat(csat_score, max_score=5):
    """
    Normalize CSAT score to a [0, 100] scale.
    Assumes CSAT is rated on a scale from 0 to max_score (default 5).
    """
    return (csat_score / max_score) * 100

def normalize_ces(ces_score, max_score=5):
    """
    Normalize CES score to a [0, 100] scale.
    Assumes CES is rated on a scale from 0 to max_score (default 5).
    """
    return (ces_score / max_score) * 100

def calculate_composite_score(nps_score, csat_score, ces_score, weights=(0.33, 0.33, 0.34)):
    """
    Calculate the composite score from normalized NPS, CSAT, and CES.
    
    Args:
        nps_score (float): NPS score in range [-100, 100].
        csat_score (float): CSAT score in its original scale (default [0, 5] or [0, 10]).
        ces_score (float): CES score in its original scale (default [0, 5] or [0, 10]).
        weights (tuple): Weights for NPS, CSAT, and CES scores (must sum to 1).

    Returns:
        float: Composite score in the range [0, 100].
    """
    # normalized_nps = normalize_nps(nps_score)
    # normalized_csat = normalize_csat(csat_score)
    # normalized_ces = normalize_ces(ces_score)
    
    #composite_score = (
    #    weights[0] * normalized_nps +
    #    weights[1] * normalized_csat +
    #    weights[2] * normalized_ces
    #)
    
    #return composite_score

def assign_traffic_light(composite_score):
    """
    Assign a traffic light color based on composite score.
    
    Args:
        composite_score (float): Composite score in the range [0, 100].

    Returns:
        str: "Green", "Yellow", or "Red" based on the thresholds.
    """
    if composite_score >= 80:
        return "Green"
    elif 60 <= composite_score < 80:
        return "Yellow"
    else:
        return "Red"

#### REAL CODE ####
def nps_traffic_light(nps_score):
    if nps_score >= 80:
        return "Green"
    elif 60 <= nps_score < 80:
        return "Yellow"
    else:
        return "Red"

def csat_traffic_light(csat_score):
    if csat_score >= 80:
        return "Green"
    elif 60 <= csat_score < 80:
        return "Yellow"
    else:
        return "Red"

def ces_traffic_light(ces_score):
    if ces_score >= 80:
        return "Green"
    elif 60 <= ces_score < 80:
        return "Yellow"
    else:
        return "Red"



# **********************
# EXAMPLE USAGE
# Example data
# nps_score = 20  # Example NPS score in range [-100, 100]
# csat_score = 4  # Example CSAT score on a scale of 0-5
# ces_score = 3   # Example CES score on a scale of 0-5

# Calculate composite score
# composite_score = calculate_composite_score(nps_score, csat_score, ces_score)

# Get traffic light indicator
# traffic_light = assign_traffic_light(composite_score)

# print(f"Composite Score: {composite_score:.2f}")
# print(f"Traffic Light: {traffic_light}")

# **********************
# MAIN CALCULATION
# metrics.py

def calculate_nps(promoters, detractors, total_respondents):
    """
    Calculate the NPS score.

    Args:
        promoters (int): Number of promoters (scores 9-10).
        detractors (int): Number of detractors (scores 0-6).
        total_respondents (int): Total number of respondents.

    Returns:
        float: NPS score in the range [-100, 100].
    """
    if total_respondents == 0:
        return 0  # Avoid division by zero
    promoter_percentage = (promoters / total_respondents) * 100
    detractor_percentage = (detractors / total_respondents) * 100
    return promoter_percentage - detractor_percentage

def calculate_csat(csat_high_scores, total_respondents):
    """
    Calculate the CSAT score.

    Args:
        csat_high_scores (int): Number of respondents who gave high satisfaction scores (e.g., 4 or 5).
        total_respondents (int): Total number of respondents.

    Returns:
        float: CSAT score in the range [0, 100].
    """
    if total_respondents == 0:
        return 0
    return (csat_high_scores / total_respondents) * 100

def calculate_ces(ces_high_scores, total_respondents):
    """
    Calculate the CES score.

    Args:
        ces_high_scores (int): Number of respondents who gave high ease scores (e.g., 4 or 5).
        total_respondents (int): Total number of respondents.

    Returns:
        float: CES score in the range [0, 100].
    """
    if total_respondents == 0:
        return 0
    return (ces_high_scores / total_respondents) * 100

# *******
# Survey data
total_respondents = 100
promoters = 30       # NPS: score of 9-10
detractors = 20       # NPS: score of 0-6
csat_high_scores = 68 # CSAT: score of 4-5
ces_high_scores = 56  # CES: score of 4-5

# Calculate NPS, CSAT, and CES scores
nps_score = calculate_nps(promoters, detractors, total_respondents)
csat_score = calculate_csat(csat_high_scores, total_respondents)
ces_score = calculate_ces(ces_high_scores, total_respondents)

# Assign traffic light
#composite_score = calculate_composite_score(nps_score, csat_score, ces_score)
nps_indicator = nps_traffic_light(nps_score)
csat_indicator = csat_traffic_light(csat_score)
ces_indicator = ces_traffic_light(ces_score)

# Output results
print(f"NPS Score: {nps_score:.2f}")
print(f"CSAT Score: {csat_score:.2f}")
print(f"CES Score: {ces_score:.2f}")
# print(f"Composite Score: {composite_score:.2f}")
print(f"NPS Traffic Light Indicator: {nps_indicator}")
print(f"CSAT Traffic Light Indicator: {csat_indicator}")
print(f"CES Traffic Light Indicator: {ces_indicator}")
