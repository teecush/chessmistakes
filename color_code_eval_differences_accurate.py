#!/usr/bin/env python3
"""
Color-code evaluation differences based on actual move quality categories from the site
"""

import csv

# ANSI escape codes for colors
RESET = "\033[0m"
BLUE = "\033[34m"      # Best
GREEN = "\033[32m"     # Excellent  
LIGHT_GREEN = "\033[92m"  # Good
YELLOW = "\033[33m"    # Inaccuracy
ORANGE = "\033[38;5;208m"  # Mistake
RED = "\033[31m"       # Blunder

def get_quality_color(eval_drop: float, actual_quality: str) -> str:
    """
    Determine color based on the actual quality classification from the site
    """
    if actual_quality == "Best":
        return BLUE
    elif actual_quality == "Excellent":
        return GREEN
    elif actual_quality == "Good":
        return LIGHT_GREEN
    elif actual_quality == "Inaccuracy":
        return YELLOW
    elif actual_quality == "Mistake":
        return ORANGE
    elif actual_quality == "Blunder":
        return RED
    else:
        return RESET

def color_code_eval_differences():
    """Color-code evaluation differences based on actual quality classifications"""
    
    print("=== COLOR-CODED EVALUATION DIFFERENCES (Based on Actual Quality) ===")
    print("Colors: Blue=Best, Green=Excellent, Light Green=Good, Yellow=Inaccuracy, Orange=Mistake, Red=Blunder")
    print()
    
    with open('repeated_moves_stockfish_analysis_with_images_fixed.csv', 'r') as f:
        reader = csv.DictReader(f)
        count = 0
        
        for row in reader:
            if count >= 20:  # Show first 20 examples
                break
                
            eval_drop = float(row['Original_Eval_Drop'])
            quality = row['Original_Move_Quality']
            color = get_quality_color(eval_drop, quality)
            move = row['Move']
            
            print(f"{move}: {color}{eval_drop:.3f}{RESET} ({quality})")
            count += 1

if __name__ == "__main__":
    color_code_eval_differences() 