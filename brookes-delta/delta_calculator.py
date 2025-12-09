"""
Brookes' Δ (Delta) Categorical Dispersion Calculator - CORRECTED VERSION
Author: Ayman Eldakroury
For: Brookes' Categorical Dispersion Measure Paper
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Union
import matplotlib.pyplot as plt

class BrookesDeltaCalculator:
    """
    Implementation of Brookes' Measure of Categorical Dispersion (Δ)
    
    Parameters:
    -----------
    categories : List[str]
        Names of subject categories
    frequencies : List[int]
        Corresponding publication frequencies
    """
    
    def __init__(self, categories: List[str], frequencies: List[int]):
        """
        Initialize calculator with categories and their frequencies
        """
        self.categories = categories
        self.frequencies = frequencies
        self.total_publications = sum(frequencies)
        
        # Validate input
        if len(categories) != len(frequencies):
            raise ValueError("Categories and frequencies must have same length")
        if any(f < 0 for f in frequencies):
            raise ValueError("Frequencies cannot be negative")
    
    def calculate_delta(self) -> Dict[str, Union[float, pd.DataFrame, str]]:
        """
        Calculate Brookes' Δ with full statistical details
        
        Returns:
        --------
        dict containing:
            - 'delta': The Δ value (0 to 1)
            - 'm': Mean of frequency-rank distribution
            - 'table': Complete calculation table
            - 'interpretation': Textual interpretation
        """
        # Step 1: Calculate percentages
        percentages = [(f / self.total_publications * 100) 
                      for f in self.frequencies]
        
        # Step 2: Create dataframe
        df = pd.DataFrame({
            'Category': self.categories,
            'Frequency': self.frequencies,
            'Percentage': percentages
        })
        
        # Step 3: Sort by percentage DESCENDING (highest first)
        df = df.sort_values('Percentage', ascending=False).reset_index(drop=True)
        df['Rank'] = range(1, len(df) + 1)
        
        # Step 4: Calculate 100n = Frequency / Percentage * 100
        df['100n'] = df['Frequency'] / df['Percentage'] * 100
        
        # Step 5: Calculate DESCENDING RANK (assign rank 1 to highest percentage, but for calculation we need special handling)
        # For Brookes' formula, we need rank values where highest percentage gets highest rank number
        # If we have n categories, highest percentage gets rank n, second gets n-1, etc.
        n_categories = len(df)
        df['Desc_Rank'] = list(range(n_categories, 0, -1))  # n, n-1, n-2, ..., 1
        
        # Step 6: Calculate m = Σ(f × Desc_Rank) / Σf
        df['f_x_DescRank'] = df['Frequency'] * df['Desc_Rank']
        sum_f_x_desc = df['f_x_DescRank'].sum()
        m = sum_f_x_desc / self.total_publications
        
        # Step 7: Calculate Δ = (m - 1) / (T - 1) where T = n_categories
        T = n_categories
        delta = (m - 1) / (T - 1) if T > 1 else 0
        
        # Step 8: Interpretation (Δ should be between 0 and 1)
        interpretation = self._interpret_delta(delta)
        
        return {
            'delta': round(delta, 3),
            'm': round(m, 3),
            'T': T,
            'total_publications': self.total_publications,
            'table': df,
            'interpretation': interpretation
        }
    
    def _interpret_delta(self, delta: float) -> str:
        """Provide textual interpretation of Δ value"""
        # Clamp delta to [0, 1] for interpretation
        clamped_delta = max(0, min(1, delta))
        
        if clamped_delta >= 0.8:
            return "Very high thematic concentration (highly specialized field)"
        elif clamped_delta >= 0.6:
            return "High thematic concentration (specialized with clear paradigms)"
        elif clamped_delta >= 0.4:
            return "Moderate thematic dispersion (balanced field)"
        elif clamped_delta >= 0.2:
            return "High thematic dispersion (interdisciplinary field)"
        else:
            return "Very high thematic dispersion (highly interdisciplinary/diverse)"
    
    def compare_fields(self, other_calculator: 'BrookesDeltaCalculator') -> Dict:
        """
        Compare Δ values between two fields
        """
        results1 = self.calculate_delta()
        results2 = other_calculator.calculate_delta()
        
        delta_diff = abs(results1['delta'] - results2['delta'])
        
        return {
            'field1_delta': results1['delta'],
            'field2_delta': results2['delta'],
            'difference': delta_diff,
            'comparison': f"Field 1 is {'more concentrated' if results1['delta'] > results2['delta'] else 'more dispersed'} than Field 2",
            'effect_size': delta_diff / max(results1['delta'], results2['delta']) if max(results1['delta'], results2['delta']) > 0 else 0
        }
    
    def visualize(self, save_path: str = None):
        """
        Create visualization of the distribution
        """
        results = self.calculate_delta()
        df = results['table']
        
        # Create plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Plot 1: Bar chart of percentages
        bars = ax1.bar(df['Category'], df['Percentage'])
        ax1.set_title('Percentage Distribution Across Categories')
        ax1.set_ylabel('Percentage (%)')
        ax1.set_xlabel('Category')
        ax1.tick_params(axis='x', rotation=45, ha='right')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%', ha='center', va='bottom', fontsize=9)
        
        # Plot 2: Δ value display
        ax2.axis('off')
        ax2.text(0.5, 0.7, f'Δ = {results["delta"]:.3f}', 
                ha='center', va='center', fontsize=24, fontweight='bold')
        
        # Show warning if Δ is outside [0, 1]
        if results['delta'] < 0 or results['delta'] > 1:
            ax2.text(0.5, 0.5, "⚠️ WARNING: Δ outside [0,1] range\nCheck calculation!", 
                    ha='center', va='center', fontsize=12, color='red', wrap=True)
        else:
            ax2.text(0.5, 0.5, results['interpretation'], 
                    ha='center', va='center', fontsize=12, wrap=True)
        
        plt.suptitle(f"Brookes' Δ Analysis")
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
        return fig

def test_example() -> Dict:
    """
    Test function with Computational Linguistics example from the paper
    
    Returns:
    --------
    dict with calculation results
    """
    print("=" * 60)
    print("TESTING BROOKES' Δ CALCULATOR - CORRECTED")
    print("Example from paper: Computational Linguistics")
    print("=" * 60)
    
    # Example from the paper (Page 62 of your document)
    categories = ["NLP Applications", "Semantics", "Resources", 
                  "Syntax", "Discourse", "Morphology", "Phonology"]
    frequencies = [280, 220, 180, 120, 100, 70, 30]
    
    # Create calculator
    calculator = BrookesDeltaCalculator(categories, frequencies)
    
    # Calculate Δ
    results = calculator.calculate_delta()
    
    print(f"\nTotal Publications: {results['total_publications']}")
    print(f"Number of Categories (T): {results['T']}")
    print(f"Mean frequency-rank (m): {results['m']}")
    print(f"Brookes' Δ: {results['delta']}")
    print(f"\nInterpretation: {results['interpretation']}")
    
    print("\n" + "=" * 60)
    print("CALCULATION TABLE")
    print("=" * 60)
    print(results['table'][['Category', 'Frequency', 'Percentage', 'Rank', 'Desc_Rank']].to_string(index=False))
    
    # Verify Δ is between 0 and 1
    if 0 <= results['delta'] <= 1:
        print(f"\n✅ VALIDATION: Δ = {results['delta']:.3f} is within valid range [0, 1]")
    else:
        print(f"\n❌ ERROR: Δ = {results['delta']:.3f} is OUTSIDE valid range [0, 1]")
    
    return results

def verify_with_paper_example():
    """
    Verify the calculation matches the example in your paper (Page 62)
    """
    print("\n" + "=" * 60)
    print("VERIFICATION WITH PAPER EXAMPLE")
    print("=" * 60)
    
    # From your paper's table on page 62
    categories = ["مو", "ف", "ر", "ن", "ت تنازليًا", "ت تنازليًا × ت"]
    
    # This is the table data from your paper
    t = [1, 2, 3, 4, 5, 6, 7]
    percentages = [24.0, 18.6, 15.0, 12.8, 11.1, 9.8, 8.7]  # مو
    frequencies = [30, 12, 18, 10, 8, 15, 7]  # ف
    
    calculator = BrookesDeltaCalculator(categories[:len(frequencies)], frequencies)
    results = calculator.calculate_delta()
    
    print(f"Paper example Δ (should be 0.80): {results['delta']}")
    
    if abs(results['delta'] - 0.80) < 0.01:
        print("✅ MATCHES PAPER RESULT (Δ = 0.80)")
    else:
        print(f"❌ DOES NOT MATCH PAPER (expected 0.80, got {results['delta']})")
    
    return results

if __name__ == "__main__":
    print("Brookes' Δ Categorical Dispersion Calculator - CORRECTED")
    print("=" * 50)
    
    # Run verification first
    verify_with_paper_example()
    
    # Run the example test
    results = test_example()
    
    print("\n" + "=" * 60)
    print("QUICK SANITY CHECK")
    print("=" * 60)
    
    # Test with simple known cases
    print("\nTest 1: Perfect equality (should give Δ ≈ 0)")
    test1 = BrookesDeltaCalculator(["A", "B", "C", "D"], [25, 25, 25, 25])
    res1 = test1.calculate_delta()
    print(f"  Δ = {res1['delta']} (should be close to 0)")
    
    print("\nTest 2: Maximum concentration (should give Δ ≈ 1)")
    test2 = BrookesDeltaCalculator(["A", "B", "C", "D"], [100, 0, 0, 0])
    res2 = test2.calculate_delta()
    print(f"  Δ = {res2['delta']} (should be close to 1)")