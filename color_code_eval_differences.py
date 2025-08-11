#!/usr/bin/env python3
"""
Color-code evaluation differences based on move quality categories
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

def get_quality_color(eval_drop: float) -> str:
    """
    Determine color based on evaluation drop (absolute value)
    Based on the site's move quality categories
    """
    abs_eval = abs(eval_drop)
    
    if abs_eval <= 0.05:  # Very small eval drop
        return BLUE  # Best
    elif abs_eval <= 0.20:  # Small eval drop
        return GREEN  # Excellent
    elif abs_eval <= 0.50:  # Moderate eval drop
        return LIGHT_GREEN  # Good
    elif abs_eval <= 1.00:  # Larger eval drop
        return YELLOW  # Inaccuracy
    elif abs_eval <= 2.00:  # Significant eval drop
        return ORANGE  # Mistake
    else:  # Very large eval drop
        return RED  # Blunder

def color_code_eval_differences():
    """Color-code evaluation differences from the old analysis"""
    
    print("=== COLOR-CODED EVALUATION DIFFERENCES ===")
    print("Colors: Blue=Best, Green=Excellent, Light Green=Good, Yellow=Inaccuracy, Orange=Mistake, Red=Blunder")
    print()
    
    with open('repeated_moves_stockfish_analysis_with_images_fixed.csv', 'r') as f:
        reader = csv.DictReader(f)
        count = 0
        
        for row in reader:
            if count >= 20:  # Show first 20 examples
                break
                
            eval_drop = float(row['Original_Eval_Drop'])
            color = get_quality_color(eval_drop)
            quality = row['Original_Move_Quality']
            move = row['Move']
            
            print(f"{move}: {color}{eval_drop:.3f}{RESET} ({quality})")
            count += 1

if __name__ == "__main__":
    color_code_eval_differences() 